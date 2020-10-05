import cx_Oracle

conn = cx_Oracle.connect("DAL/java@localhost:1521/xe")
cursor=conn.cursor()
sql = "update mymember set mem_name = :1 where mem_id=:2"
data = ('김가','a001')
cursor.execute(sql,data)
cursor.close()
conn.commit() # 자동으로 커밋해주는게 아니라 직접 써줘야함0 
conn.close()