import sqlite3
con = sqlite3.connect('lnm.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS Students')
cur.execute('''CREATE TABLE Students(Roll INT , Name TEXT , Marks INT) ''')
print('Table Students Created..')
cur.execute("INSERT INTO Students VALUES(1,'Aditya',98)")
cur.execute("INSERT INTO Students VALUES(2,'Sonu',99)")
cur.execute("INSERT INTO Students VALUES(3,'Adarsh',85)")
cur.execute("INSERT INTO Students VALUES(4,'Ashu',75)")
cur.execute("INSERT INTO Students VALUES(5,'Ravi',23)")
con.commit()
con.close()
print('Values in table Students inserted..')