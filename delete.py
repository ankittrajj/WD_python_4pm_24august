import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'happy_diwali')

cursor = con.cursor()

# if con.is_connected():
#     print("Connected Successfully!!")

name = input("Enter your name")
# age = int(input("Enter your age"))
# marks = int(input("Enter the marks"))

query = "delete from abc where name = '{}'".format(name)
cursor.execute(query)
con.commit()
print("Data Entered successfully!!")