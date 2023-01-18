import mysql.connector

mydb = mysql.connector.connect(
    host="172.30.142.7",
    port=43306,
    user="root",
    password="p455w0rd",
)

db = mydb.cursor()
db.execute("CREATE DATABASE garden")