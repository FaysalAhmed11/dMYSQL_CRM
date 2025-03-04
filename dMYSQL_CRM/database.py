import mysql.connector

data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password321',
    )

#prepare the cursor object
cursor_object = data_base.cursor()

#create a database
cursor_object.execute("CREATE DATABASE garments")

print("hey, it's done !")