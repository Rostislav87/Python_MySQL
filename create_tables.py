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

table_prescription = '''CREATE TABLE prescription (
                        id SERIAL,
                        doctor_id INT,
                        patient_id INT,
                        valid_from DATETIME,
                        valid_to DATETIME,
                        is_released BOOLEAN
                     )'''

table_list_of_medicaments = '''CREATE TABLE list_of_medicaments (
                               prescription_id INT,
                               medicament_id INT,
                               amount INT
                            )'''

# Define SQL commands for inserting sample data into the tables
insert_address_data = '''INSERT INTO address (street, street_number, city, zip_code) VALUES (%s, %s, %s, %s)'''

insert_doctor_data = '''INSERT INTO doctor (name, surname, address_id, phone_number, email) VALUES (%s, %s, %s, %s, %s)'''

insert_patient_data = '''INSERT INTO patient (name, surname, address_id, insurance_company) VALUES (%s, %s, %s, %s)'''

insert_medicament_data = '''INSERT INTO medicament (name, price_insurance, price_patient, unit) VALUES (%s, %s, %s, %s)'''

insert_prescription_data = '''INSERT INTO prescription (doctor_id, patient_id, valid_from, valid_to, is_released) VALUES (%s, %s, %s, %s, %s)'''

insert_list_of_medicaments_data = '''INSERT INTO list_of_medicaments (prescription_id, medicament_id, amount) VALUES (%s, %s, %s)'''

# Define sample data for the tables
values_address = [
    ('Doktorská', 1, 'Engetov', '123 00'), 
    ('Pacientská', 1, 'Engetov', '111 11'), 
    ('Pacientská', 2, 'Engetov', '567 89')
]

values_doctor = ('Jan', 'Doktor', 1, '+420 123 456 789', 'doktor@engeto.cz')

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

values_prescription = [
    (1, 1, '2019-10-06 11:35:12', '2019-10-16 11:35:12', True),
    (1, 2, '2019-10-06 12:00:06', '2019-10-16 12:00:06', False),
    (1, 3, '2019-10-06 14:04:53', '2019-10-16 14:04:53', True),
    (1, 1, '2019-10-08 08:05:40', '2019-10-18 08:05:40', True),
    (1, 1, '2019-11-11 09:12:42', '2019-11-21 09:12:42', False),
    (1, 2, '2019-11-11 10:07:35', '2019-11-21 10:07:35', False)
]

values_list_of_medicaments = [
    (1, 1, 2),
    (1, 4, 100),
    (2, 3, 2),
    (2, 4, 250),
    (3, 1, 1),
    (3, 2, 3),
    (3, 3, 2),
    (4, 3, 1),
    (4, 4, 150),
    (5, 1, 3),
    (5, 2, 1),
    (5, 4, 300),
    (5, 5, 300),
    (6, 2, 4),
    (6, 5, 400)
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

# Create the prescription table
mycursor.execute(table_prescription)

# Create the list of medicaments
mycursor.execute(table_list_of_medicaments)

# Insert sample data into the address table
mycursor.executemany(insert_address_data, values_address)

# Insert sample data into the doctor table
mycursor.execute(insert_doctor_data, values_doctor)

# Insert sample data into patient table
mycursor.executemany(insert_patient_data, values_patient)

# Insert sample data into medicament table
mycursor.executemany(insert_medicament_data, values_medicament)

# Insert sample data into prescription table
mycursor.executemany(insert_prescription_data, values_prescription)

# Insert sample data into list of medicaments table
mycursor.executemany(insert_list_of_medicaments_data, values_list_of_medicaments)
    
# Commit the changes
mydb.commit()