import sqlite3

conn = sqlite3.connect("C:/Users/404-01/Desktop/mydb.db")
cur = conn.cursor()

cur.execute("insert into mytable values (?,?,?)", ('1','2','3'))

conn.commit()

conn.close()