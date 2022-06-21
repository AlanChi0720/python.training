import mysql.connector

connection= mysql.connector.connect(
    host= 'localhost',
    port= '3306',
    user= 'root',
    password= 'Alan@860720',
    database= 'sql_tutorial'
)
cursor= connection.cursor()

cursor.execute("SELECT * FROM `branch`;")

records= cursor.fetchall()
for i in records:
    print(i)

cursor.close()
connection.close()