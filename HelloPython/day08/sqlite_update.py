import sqlite3

conn = sqlite3.connect("C:/Users/404-01/Desktop/mydb.db")
cur = conn.cursor()
sql="update mytable set col01=? ,col02=? ,col03=? where col01=?"
cur.execute(sql, ('5','6','7','2'))

conn.commit()

conn.close()
