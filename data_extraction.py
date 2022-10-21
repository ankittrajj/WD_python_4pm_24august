import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'happy_diwali')

cursor = con.cursor()

# if con.is_connected():
#     print("Connected Successfully!!")

query = "select * from abc"
cursor.execute(query)

# data = cursor.fetchone()
# data = cursor.fetchmany(2)
data = cursor.fetchall()
print(data)