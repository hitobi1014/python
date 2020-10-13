import os
import sys
import urllib.request
client_id = "Lu6xJQWzHIlKmx0vzb4T"
client_secret = "Ryv55ePo9S"
encText = urllib.parse.quote("대전 용문동 맛집")
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