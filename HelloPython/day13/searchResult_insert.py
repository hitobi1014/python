from bs4 import BeautifulSoup
import requests
import sqlite3
from day13.my_crawling06 import encText
    
url = "https://openapi.naver.com/v1/search/local.xml?display=5&query=" + encText # xml 결과
data = requests.get(url)
xml = data.text

conn = sqlite3.connect("naverSearchDB.db")
soup = BeautifulSoup(xml,"html.parser")

print(soup.find_all("channel"))
for item in soup.find_all("item"):
    title = item.find("title").string
    link = item.find("link").string
    category = item.find("category").string
    description = item.find("description").string
    telephone = item.find("telephone").string
    address = item.find("address").string
    roadAddress = item.find("roadAddress").string
    mapx = item.find("mapx").string
    mapy = item.find("mapy").string
     
    cur = conn.cursor()
#     sql = "INSERT INTO searchResult VALUES (?,?,?,?,?,?,?,?,?)"
#     data2 = (title,link,category,description,telephone,address,roadAddress,mapx,mapy)
#     cur.execute(sql,data2)
    cur.execute("INSERT INTO searchResult VALUES (?,?,?,?,?,?,?,?,?)",(title,link,category,description,telephone,address,roadAddress,mapx,mapy))
    conn.commit()
 
cur = conn.cursor()
cur.execute("select * from searchResult")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()

