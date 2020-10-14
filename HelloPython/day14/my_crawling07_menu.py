import time
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

# options = Options()
# options.headless = False
# browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
# browser.get("https://map.naver.com/v5/search/%EA%B7%BC%EC%B2%98%EB%A7%9B%EC%A7%91/place/16069633?c=14184384.7033517,4345409.8253195,16,0,0,0,dh")

form_class = uic.loadUiType("hello.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.btn1Function)

        options = Options()
        options.headless = False
        self.browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
        self.browser.get("https://place.map.kakao.com/17733090")
        
#         self.browser.get("http://localhost/HelloWeb/hello.jsp")
    
    def btn1Function(self):
#         time.sleep(3)
#         tag_names = self.browser.find_element_by_css_selector(".rank_top1000_list").find_elements_by_tag_name("li")
        objs = self.browser.find_element_by_class_name('list_menu').find_elements_by_tag_name('li')
        title2 = self.browser.find_element_by_class_name('inner_place').find_element_by_class_name('tit_location')
        for obj in objs:
#             print(tag.text.split("\n"))
#             print(obj.find_element_by_class_name('loss_word').text.split("\n"))
#             menu_name = obj.find_element_by_class_name('loss_word').text.split("\n")
#             menu_price = obj.find_element_by_class_name('price_menu').text.split("\n")
            menu_name = obj.find_element_by_class_name('loss_word').text
            menu_price = obj.find_element_by_class_name('price_menu').text
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
