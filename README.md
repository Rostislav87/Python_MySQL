# Project Python MySQL

## Terminal commands on Linux:

- Virtual environment:
'''
$ python -m venv [name]
'''

- Download and install 'MySQL Connector":
'''
$ pip install mysql-connector-python
'''

- Import MySQL connector:
'''
import mysql.connector
'''

- Create connection:
'''
mydb = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    password="yourpassword"
)