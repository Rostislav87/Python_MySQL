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

doctor_table = '''CREATE TABLE doctor (
                  id SERIAL,
                  name VARCHAR(255),
                  surname VARCHAR(255),
                  address_id INT,
                  phone_number VARCHAR(20),
                  email VARCHAR(255)
               )'''

# Define SQL commands for inserting sample data into the tables
insert_address_data = '''INSERT INTO address (street, street_number, city, zip_code) VALUES'''

insert_doctor_data = '''INSERT INTO doctor (name, surname, address_id, phone_number, email) VALUES'''

# Define sample data for the tables
values_address = [
    ('Doktorská', 1, 'Engetov', '123 00'), 
    ('Pacientská', 1, 'Engetov', '111 11'), 
    ('Pacientská', 2, 'Engetov', '567 89')
    ]

values_doctor = [('Jan', 'Doktor', 1, '+420 123 456 789', 'doktor@engeto.cz')]

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
mycursor.execute(doctor_table)

# Insert sample data into the address table
for value in values_address:
    mycursor.execute(insert_address_data, value)

# Insert sample data into the doctor table
mycursor.execute(insert_doctor_data, values_doctor)

# Commit the changes
mydb.commit()