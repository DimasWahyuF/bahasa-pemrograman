import mysql.connector


mydb = mysql.connector.connect(
    host="172.30.142.7",
    port=43306,
    user="root",
    password="p455w0rd",
    database="garden"
)

db = mydb.cursor()

db.execute(
    "CREATE TABLE Anggrek (name VARCHAR(225), beri_air VARCHAR(225), beri_pupuk VARCHAR(255), status VARCHAR(255))"
)
db.execute(
    "CREATE TABLE Mawar (name VARCHAR(225), beri_air VARCHAR(225), beri_pupuk VARCHAR(255), status VARCHAR(255))"
)
db.execute(
    "CREATE TABLE Melati (name VARCHAR(225), beri_air VARCHAR(225), beri_pupuk VARCHAR(255), status VARCHAR(255))"
)