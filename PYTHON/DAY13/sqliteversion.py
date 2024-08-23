import sqlite3
con = sqlite3.connect('lnm.db')
cur = con.cursor()
cur.execute('SELECT SQLITE_VERSION()')
data = cur.fetchone()
print('SQLite version: ', data)
