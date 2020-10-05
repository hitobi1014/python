import cx_Oracle

conn = cx_Oracle.connect("DAL/java@localhost:1521/xe")
cursor=conn.cursor()
sql = "insert into mymember values(:1,:2,:3,:4,:5)"
data = ('a001','테스트','0103030303','대전',3)
cursor.execute(sql,data)
cursor.close()
conn.commit() # 자동으로 커밋해주는게 아니라 직접 써줘야함0 
conn.close()