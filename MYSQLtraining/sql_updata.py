import mysql.connector

connection= mysql.connector.connect(
    host= 'localhost',
    port= '3306',
    user= 'root',
    password= 'Alan@860720',
    database= 'sql_tutorial'
)
cursor= connection.cursor()

# cursor.execute("INSERT INTO `branch` VALUES(5, 'qq', NULL);")
# cursor.execute("UPDATE `branch` SET `manager_id` = 209 WHERE `branch_id` = 4;")
cursor.execute("DELETE FROM `branch` WHERE `branch_id` = 5;")


cursor.close()
connection.commit()
connection.close()