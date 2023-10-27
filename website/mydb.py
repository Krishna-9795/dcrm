import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='krishna123'
    )
cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print(" Database Created")