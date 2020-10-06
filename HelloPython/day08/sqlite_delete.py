import sqlite3

conn = sqlite3.connect("C:/Users/404-01/Desktop/mydb.db")
cur = conn.cursor()

sql = "delete from mytable where col01=?"
cur.execute(sql, ('1'))

conn.commit()

conn.close()