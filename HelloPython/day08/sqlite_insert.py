import sqlite3

conn = sqlite3.connect("C:/Users/404-01/Desktop/mydb.db")
cur = conn.cursor()

cur.execute("insert into mytable values (?,?,?)", ('5','6','7'))

conn.commit()