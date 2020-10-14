import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import sqlite3

client_id = "Lu6xJQWzHIlKmx0vzb4T"
client_secret = "Ryv55ePo9S"
encText = urllib.parse.quote("대전 중구청 사쿠사쿠")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/local.xml?display=5&query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
    
# soup = BeautifulSoup(response_body, 'html.parser')
# my_items = soup.select(
#     'item'
#     )
# 
# conn = sqlite3.connect("naverSearchDB.db")
# cur = conn.cursor()
# for item in my_items:
#     title = item.find('title').text
#     link = item.find('link').text
#     category = item.find('category').text
#     description = item.find('description').text
#     telephone= item.find('telephone').text
#     
#     address = item.find('address').text
#     roadAddress = item.find('roadaddress').text
#     telephone= item.find('telephone').text
#     mapx = item.find('mapx').text
#     mapy = item.find('mapy').text
# #     print(roadAddress)
#      
#     cur.execute("INSERT INTO searchResult VALUES (?,?,?,?,?,?,?,?,?)",(title,link,category,description,telephone,address,roadAddress,mapx,mapy))
#     
# conn.commit()
# cur.execute("select * from searchResult")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# conn.close()

