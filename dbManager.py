import sqlite3

connection = sqlite3.connect('chinook.db') #สำหรับเชื่อมต่อกับฐานข้อมูล
#print('connect to DB sucess')
cursor = connection.execute("SELECT Firstname, Lastname, Email FROM Customers;") #สร้างตัวแปรเพื่อเก็บข้อมูลที่ได้มาจากฐานข้อมูล
for row in cursor: # For loop ปกติโดยการเปลี่ยน Range เป็นชุดข้อมูลอื่นแทน ในที่นี้คือชุดข้อมูลจากฐานข้อมูลที่เก็บอยู่ในตัวแปร cursor
    print("Customer ID :", row[0], row[1], row[2])
connection.close()






