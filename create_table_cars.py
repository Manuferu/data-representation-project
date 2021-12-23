import mysql.connector

db =  mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "",
    database = "datarepresentation"
)

cursor = db.cursor()
sql = "CREATE TABLE cars (plate INT PRIMARY KEY, model VARCHAR(250), year INT, fuel VARCHAR(250))"

cursor.execute(sql)