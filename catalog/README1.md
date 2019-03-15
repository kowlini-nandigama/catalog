Create a medicine store app where users can add, edit, and delete medicinecompanys and medicines in the medicinecompanys.

Setup and run the project
Prerequisites
Python 2.7
Vagrant
VirtualBox
How to Run
Install VirtualBox and Vagrant
Clone this repository
Unzip and place the Item Catalog folder in your Vagrant directory
Launch Vagrant
$ Vagrant up 
Login to Vagrant
$ Vagrant ssh
Change directory to /vagrant
$ Cd /vagrant
Initialize the database
$ Python Data_Setup.py
Populate the database with some initial data
$ Python database_init.py
Launch application
$ Python main.py
Open the browser and go to http://localhost:2434
JSON endpoints
Returns JSON of all medicinecompanys
/MedicineStore/JSON
Returns JSON of specific medicinecompany
/MedicineStore/MedicineCategories/JSON
Returns JSON of allmedicines of a all companys
/MedicineStore/Medicines/JSON
Returns JSON of medicines of a particular company
/MedicineStore/<path:medicine_name>/Medicines/JSON
Returns JSON of particular medicine of a particular company
/MedicineStore/<path:medicine_name>/<path:edition_name>/JSON