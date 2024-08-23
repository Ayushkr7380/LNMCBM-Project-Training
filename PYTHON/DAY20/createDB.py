import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    passsword='mysql'
)
a = conn.cursor()
query = "create database ayush1"
a.execute(query)
conn.commit()
print("Database created.")