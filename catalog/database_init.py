from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from Data_Setup import *

engine = create_engine('sqlite:///medicines.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete BykesCompanyName if exisitng.
session.query(MedicineCompanyName).delete()
# Delete BykeName if exisitng.
session.query(MedicineName).delete()
# Delete User if exisitng.
session.query(User).delete()

# Create sample users data
User1 = User(
    name="satya kowlini nandigama", email="satyakowlini123@gmail.com",
    picture='http://www.enchanting-costarica.com/wp-content/'
    'uploads/2018/02/jcarvaja17-min.jpg')
session.add(User1)
session.commit()
print ("Successfully Add First User")
# Create sample medicine companys
MedicineCompany1 = MedicineCompanyName(name="cipla", user_id=1)
session.add(MedicineCompany1)
session.commit()

MedicineCompany2 = MedicineCompanyName(name="Dr.Reddy's", user_id=1)
session.add(MedicineCompany2)
session.commit

MedicineCompany3 = MedicineCompanyName(name="Lupin Limited", user_id=1)
session.add(MedicineCompany3)
session.commit()

MedicineCompany4 = MedicineCompanyName(name="Sun pharmaceuticals", user_id=1)
session.add(MedicineCompany4)
session.commit()

MedicineCompany5 = MedicineCompanyName(name="Ranbaxy", user_id=1)
session.add(MedicineCompany5)
session.commit()

MedicineCompany6 = MedicineCompanyName(name="Mylan", user_id=1)
session.add(MedicineCompany6)
session.commit()

# Populare a bykes with models for testing
# Using different users for bykes names year also
MedicineName1 = MedicineName(
    name="Escitalopram", medicinetype="anti-deppressant", price="200",
    description="cures depression adnot use without prescription",
    date=datetime.datetime.now(),
    medicinecompanynameid=1,
    user_id=1)
session.add(MedicineName1)
session.commit()

MedicineName2 = MedicineName(
    name="Lamivudine", medicinetype="anti-retroviral", price="600",
    description="cures viral diseases",
    date=datetime.datetime.now(), medicinecompanynameid=2, user_id=1)
session.add(MedicineName2)
session.commit()

MedicineName3 = MedicineName(
    name="Acemuc", medicinetype="respiratory treatement", price="800",
    description="take the prescribed dosage orally",
    date=datetime.datetime.now(), medicinecompanynameid=3, user_id=1)
session.add(MedicineName3)
session.commit()

MedicineName4 = MedicineName(
    name="Aceclobeta", medicinetype="anti-infective", price="300",
    description="cures infections", date=datetime.datetime.now(),
    medicinecompanynameid=4, user_id=1)
session.add(MedicineName4)
session.commit()

MedicineName5 = MedicineName(
    name="Amablez", medicinetype="Hormone replacement", price="5000",
    description="cures for  the category of hormone replacement",
    date=datetime.datetime.now(), medicinecompanynameid=5, user_id=1)
session.add(MedicineName5)
session.commit()

MedicineName6 = MedicineName(
    name="Doxy cicline", medicinetype="antibiotic", price="400",
    description="only fro oral suspension", date=datetime.datetime.now(),
    medicinecompanynameid=6, user_id=1)
session.add(MedicineName6)
session.commit()

print("Your medicines database has been inserted!")
