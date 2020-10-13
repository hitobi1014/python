import sqlite3

conn = sqlite3.connect("naverSearchDB.db")
cur = conn.cursor()

sql = "SELECT * FROM searchResult"
cur.execute(sql)

rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()