import sqlite3
Students = [
    (1,'Ayush',56),
    (2,'Anubhav',32),
    (3,'Aarti',34),
    (4,'Ashutosh',98),
    (5,'Ashu',53),
    (6,'Aniket',78),
    (7,'Atul',36),
    (8,'Abhishek',99),
    (9,'Abhi',78),
    (10,'Adarsh',25),
    (11,'Aditya',78),
]

con = sqlite3.connect('lnm.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS Students')
cur.execute('CREATE TABLE Students(Roll INT,Name TEXT,Marks INT)')
cur.executemany("INSERT INTO Students VALUES(?,?,?)",Students)
con.commit()

cur.execute('SELECT * FROM Students')
rows = cur.fetchall()
con.close()
print("Values Inserted")
for row in rows:
    print(row[0],row[1],row[2],sep="|")