import sqlite3

conn = sqlite3.connect("C:/Users/404-01/Desktop/mydb.db")
cur = conn.cursor()

cur.execute("select * from mytable")

rows = cur.fetchall()
for row in rows:
    print(row)