from flask import Flask, render_template, url_for
from flask import request, redirect, flash, make_response, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data_Setup import Base, MedicineCompanyName, MedicineName, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests
import datetime

engine = create_engine('sqlite:///medicines.db',
                       connect_args={'check_same_thread': False}, echo=True)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json',
                            'r').read())['web']['client_id']
APPLICATION_NAME = "Medicine Store"

DBSession = sessionmaker(bind=engine)
session = DBSession()
# Create anti-forgery state token
tabl_catal = session.query(MedicineCompanyName).all()


# login
@app.route('/login')
def showLogin():
    state = ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for x in range(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    tabl_catal = session.query(MedicineCompanyName).all()
    tables = session.query(MedicineName).all()
    return render_template('login.html',
                           STATE=state, tabl_catal=tabl_catal, tables=tables)
    # return render_template('myhome.html', STATE=state
    # tabl_catal=tabl_catal,tables=tables)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print ("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px; border-radius: 150px;'
    '-webkit-border-radius: 150px; -moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print ("done!")
    return output


# User Helper Functions
def createUser(login_session):
    User1 = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(User1)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception as error:
        print(error)
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session

#   ####completed
# Home


@app.route('/')
@app.route('/home')
def home():
    tabl_catal = session.query(MedicineCompanyName).all()
    return render_template('myhome.html', tabl_catal=tabl_catal)

#####
# Byke Category for admins


@app.route('/MedicineStore')
def MedicineStore():
    try:
        if login_session['username']:
            name = login_session['username']
            tabl_catal = session.query(MedicineCompanyName).all()
            tabls = session.query(MedicineCompanyName).all()
            tables = session.query(MedicineName).all()
            return render_template('myhome.html', tabl_catal=tabl_catal,
                                   tabls=tabls, tables=tables, uname=name)
    except:
        return redirect(url_for('showLogin'))

######
# Showing medicines based on medicine category


@app.route('/MedicineStore/<int:tablid>/AllMedicineCompanys')
def showMedicines(tablid):
    tabl_catal = session.query(MedicineCompanyName).all()
    tabls = session.query(MedicineCompanyName).filter_by(id=tablid).one()
    tables = session.query(MedicineName).filter_by(
        medicinecompanynameid=tablid).all()
    try:
        if login_session['username']:
            return render_template('showMedicines.html', tabl_catal=tabl_catal,
                                   tabls=tabls, tables=tables,
                                   uname=login_session['username'])
    except:
        return render_template(
            'showMedicines.html',
            tabl_catal=tabl_catal, tabls=tabls, tables=tables)

#####
# Add New medicine


@app.route('/MedicineStore/addMedicineCompany', methods=['POST', 'GET'])
def addMedicineCompany():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        company = MedicineCompanyName(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(company)
        session.commit()
        return redirect(url_for('MedicineStore'))
    else:
        return render_template(
            'addMedicineCompany.html', tabl_catal=tabl_catal)

########
# Edit medicine company


@app.route('/MedicineStore/<int:tablid>/edit', methods=['POST', 'GET'])
def editMedicineCategory(tablid):
    if 'username' not in login_session:
        return redirect('/login')
    editedMedicine = session.query(
        MedicineCompanyName).filter_by(id=tablid).one()
    creator = getUserInfo(editedMedicine.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You cannot edit this Medicine Category."
              "This is belongs to %s" % creator.name)
        return redirect(url_for('MedicineStore'))
    if request.method == "POST":
        if request.form['name']:
            editedMedicine.name = request.form['name']
        session.add(editedMedicine)
        session.commit()
        flash("Medicine Category Edited Successfully")
        return redirect(url_for('MedicineStore'))
    else:
        # tabl_catal is global variable we can them in entire application
        return render_template('editMedicineCategory.html',
                               tabb=editedMedicine, tabl_catal=tabl_catal)

######
# Delete Byke Category


@app.route('/MedicineStore/<int:tablid>/delete', methods=['POST', 'GET'])
def deleteMedicineCategory(tablid):
    if 'username' not in login_session:
        return redirect('/login')
    tabb = session.query(MedicineCompanyName).filter_by(id=tablid).one()
    creator = getUserInfo(tabb.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You cannot Delete this Medicine Category."
              "This is belongs to %s" % creator.name)
        return redirect(url_for('MedicineStore'))
    if request.method == "POST":
        session.delete(tabb)
        session.commit()
        flash("Medicine Category Deleted Successfully")
        return redirect(url_for('MedicineStore'))
    else:
        return render_template(
            'deleteMedicineCategory.html', tabb=tabb, tabl_catal=tabl_catal)

######
# Add New Byke Name Details


@app.route(
    '/MedicineStore/addMedicineCompany/addMedicineDetails/<string:tablname>'
    '/add', methods=['GET', 'POST'])
def addMedicineDetails(tablname):
    if 'username' not in login_session:
        return redirect('/login')
    tabls = session.query(MedicineCompanyName).filter_by(name=tablname).one()
    # See if the logged in user is not the owner of byke
    creator = getUserInfo(tabls.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You can't add new Medicine list"
              "This is belongs to %s" % creator.name)
        return redirect(url_for('showMedicines', tablid=tabls.id))
    if request.method == 'POST':
        name = request.form['name']
        medicinetype = request.form['medicinetype']
        price = request.form['price']
        description = request.form['description']
        medicinedetails = MedicineName(
            name=name, medicinetype=medicinetype, price=price,
            description=description, date=datetime.datetime.now(),
            medicinecompanynameid=tabls.id, user_id=login_session['user_id'])
        session.add(medicinedetails)
        session.commit()
        return redirect(url_for('showMedicines', tablid=tabls.id))
    else:
        return render_template('addMedicineDetails.html',
                               tablname=tabls.name, tabl_catal=tabl_catal)

######
# Edit Byke details


@app.route('/MedicineStore/<int:tablid>/<string:tableename>/edit',
           methods=['GET', 'POST'])
def editMedicine(tablid, tableename):
    if 'username' not in login_session:
        return redirect('/login')
    tabb = session.query(MedicineCompanyName).filter_by(id=tablid).one()
    medicinedetails = session.query(
        MedicineName).filter_by(name=tableename).one()
    # See if the logged in user is not the owner of byke
    creator = getUserInfo(tabb.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You can't edit this Medicine list"
              "This is belongs to %s" % creator.name)
        return redirect(url_for('showMedicines', tablid=tabb.id))
    # POST methods
    if request.method == 'POST':
        medicinedetails.name = request.form['name']
        medicinedetails.price = request.form['price']
        medicinedetails.description = request.form['description']
        medicinedetails.date = datetime.datetime.now()
        session.add(medicinedetails)
        session.commit()
        flash("Medicine details Edited Successfully")
        return redirect(url_for('showMedicines', tablid=tablid))
    else:
        return render_template(
            'editMedicine.html',
            tablid=tablid, medicinedetails=medicinedetails,
            tabl_catal=tabl_catal)

#####
# Delte Byke Edit


@app.route('/MedicineStore/<int:tablid>/<string:tableename>/delete',
           methods=['GET', 'POST'])
def deleteMedicine(tablid, tableename):
    if 'username' not in login_session:
        return redirect('/login')
    tabb = session.query(MedicineCompanyName).filter_by(id=tablid).one()
    medicinedetails = session.query(
        MedicineName).filter_by(name=tableename).one()
    # See if the logged in user is not the owner of byke
    creator = getUserInfo(tabb.user_id)
    user = getUserInfo(login_session['user_id'])
    # If logged in user != item owner redirect them
    if creator.id != login_session['user_id']:
        flash("You can't delete this Medicine list"
              "This is belongs to %s" % creator.name)
        return redirect(url_for('showMedicines', tablid=tabb.id))
    if request.method == "POST":
        session.delete(medicinedetails)
        session.commit()
        flash("Deleted Medicine details Successfully")
        return redirect(url_for('showMedicines', tablid=tablid))
    else:
        return render_template(
            'deleteMedicine.html',
            tablid=tablid, medicinedetails=medicinedetails,
            tabl_catal=tabl_catal)

####
# Logout from current user


@app.route('/logout')
def logout():
    access_token = login_session['access_token']
    print ('In gdisconnect access token is %s', access_token)
    print ('User name is: ')
    print (login_session['username'])
    if access_token is None:
        print ('Access Token is None')
        response = make_response(
            json.dumps('Current user not connected....'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = login_session['access_token']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = \
        h.request(
            uri=url, method='POST', body=None,
            headers={'content-type': 'application/x-www-form-urlencoded'})[0]

    print (result['status'])
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps(
            'Successfully disconnected user..'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("Successful logged out")
        return redirect(url_for('showLogin'))
        # return response
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

#####
# Json


@app.route('/MedicineStore/JSON')
def allMedicinesJSON():
    medicinecategories = session.query(MedicineCompanyName).all()
    category_dict = [c.serialize for c in medicinecategories]
    for c in range(len(category_dict)):
        medicines = [i.serialize for i in session.query(
                 MedicineName).filter_by(
                     medicinecompanynameid=category_dict[c]["id"]).all()]
        if medicines:
            category_dict[c]["medicine"] = medicines
    return jsonify(MedicineCompanyName=category_dict)

####


@app.route('/MedicineStore/MedicineCategories/JSON')
def categoriesJSON():
    medicines = session.query(MedicineCompanyName).all()
    return jsonify(MedicineCategories=[c.serialize for c in medicines])

####


@app.route('/MedicineStore/Medicines/JSON')
def itemsJSON():
    items = session.query(MedicineName).all()
    return jsonify(medicines=[i.serialize for i in items])

#####


@app.route('/MedicineStore/<path:medicine_name>/Medicines/JSON')
def categoryItemsJSON(medicine_name):
    medicineCategory = session.query(MedicineCompanyName).filter_by(
        name=medicine_name).one()
    medicines = session.query(MedicineName).filter_by(
        medicinecompanyname=medicineCategory).all()
    return jsonify(medicineEdition=[i.serialize for i in medicines])

#####


@app.route('/MedicineStore/<path:medicine_name>/<path:edition_name>/JSON')
def ItemJSON(medicine_name, edition_name):
    medicineCategory = session.query(MedicineCompanyName).filter_by(
        name=medicine_name).one()
    medicineEdition = session.query(MedicineName).filter_by(
           name=edition_name, medicinecompanyname=medicineCategory).one()
    return jsonify(medicineEdition=[medicineEdition.serialize])

if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='127.0.0.1', port=2434)
