import sqlite3

conn = sqlite3.connect("C:/Users/404-01/Desktop/mydb.db")
cur = conn.cursor()

cur.execute("delete from mytable where col01=?", ('3'))

conn.commit()