# 86.0.4240.75 크롬 버전정보
from selenium import webdriver as wd 
driver = wd.Chrome(executable_path="chromedriver.exe")
url = "https://www.naver.com" 
driver.get(url)

