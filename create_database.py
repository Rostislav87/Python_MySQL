import mysql.connector
from user_values import host, user, password

# Connect to MySQL and create database
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)
mycursor = mydb.cursor()
print("Creating database...")

# Create the prescript database
mycursor.execute("CREATE DATABASE prescript")
print("Database created.")