import mysql.connector
from user_values import host, user, password

# Define SQL commands for creating the tables
table_address = '''CREATE TABLE address (
                   id SERIAL,
                   street VARCHAR(255),
                   street_number INT,
                   city VARCHAR(255),
                   zip_code VARCHAR(6)
                )'''

table_doctor = '''CREATE TABLE doctor (
                  id SERIAL,
                  name VARCHAR(255),
                  surname VARCHAR(255),
                  address_id INT,
                  phone_number VARCHAR(20),
                  email VARCHAR(255)
               )'''

table_patient = '''CREATE TABLE patient (
                   id SERIAL,
                   name VARCHAR(255),
                   surname VARCHAR(255),
                   address_id INT,
                   insurance_company VARCHAR(255)
                )'''

table_medicament = '''CREATE TABLE medicament (
                      id SERIAL,
                      name VARCHAR(255),
                      price_insurance FLOAT,
                      price_patient FLOAT,
                      unit VARCHAR(10)
                      )'''

# Define SQL commands for inserting sample data into the tables
insert_address_data = '''INSERT INTO address (street, street_number, city, zip_code) VALUES'''

insert_doctor_data = '''INSERT INTO doctor (name, surname, address_id, phone_number, email) VALUES'''

insert_patient_data = '''INSERT INTO patient (name, surname, address_id, insurance_company) VALUES'''

insert_data_medicament = '''INSERT INTO medicament (name, price_insurance, price_patient, unit) VALUES'''

# Define sample data for the tables
values_address = [
    ('Doktorská', 1, 'Engetov', '123 00'), 
    ('Pacientská', 1, 'Engetov', '111 11'), 
    ('Pacientská', 2, 'Engetov', '567 89')
]

values_doctor = [('Jan', 'Doktor', 1, '+420 123 456 789', 'doktor@engeto.cz')]

values_patient = [
    ('Petr', 'Pacient', 2, 'Engeto insurance'),
    ('Libor', 'Pacient', 3, 'Engeto insurance'),
    ('Stanislav', 'Pacient', 3, 'State insurance')
]

values_medicament = [
    ('Super Pills', 10.5, 4, 'package'),
    ('Extra Pills', 18.1, 8.2, 'package'),
    ('Common Pills', 5, 6.1, 'package'),
    ('Super Sirup', 12, 8, 'mililiter'),
    ('Extra Sirup', 16.3, 10.3, 'mililiter')
]

# Connect to the database and create the tables
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database='prescript'
)
mycursor = mydb.cursor()

# Create the address table
mycursor.execute(table_address)

# Create the doctor table
mycursor.execute(table_doctor)

# Create the patient table
mycursor.execute(table_patient)

# Create the medicament table
mycursor.execute(table_medicament)

# Insert sample data into the address table
for value in values_address:
    mycursor.execute(insert_address_data, value)

# Insert sample data into the doctor table
mycursor.execute(insert_doctor_data, values_doctor)

# Insert sample data into patient table
for value in values_patient:
    mycursor.execute(insert_patient_data, value)

# Insert sample data into medicament table
for value in values_medicament:
    mycursor.execute(insert_data_medicament, value)

# Commit the changes
mydb.commit()