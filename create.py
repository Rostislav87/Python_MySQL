import mysql.connector
from user_values import host, user, password

mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

mycursor =mydb.cursor()
print("Creating database...")

mycursor.execute("CREATE DATABASE prescript")
print("Database created.")