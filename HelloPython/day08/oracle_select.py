import cx_Oracle

conn = cx_Oracle.connect("DAL/java@localhost:1521/xe")
cursor=conn.cursor()
sql = "select * from buyer"
cursor.execute(sql)

for row in cursor:
    print(row[0],row[1],row[2])

cursor.close()
conn.close()