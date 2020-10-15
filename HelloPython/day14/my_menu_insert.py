import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import cx_Oracle

form_class = uic.loadUiType("mymenu.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.btn1Function)
        options = Options()
        options.headless = False
        self.browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
        self.browser.get("https://place.map.kakao.com/17733090")
        
    def btn1Function(self):
        self.conn = cx_Oracle.connect("DAL/java@localhost:1521/xe")
        self.cursor=self.conn.cursor()
        objs = self.browser.find_element_by_class_name('list_menu').find_elements_by_tag_name('li')
        title2 = self.browser.find_element_by_class_name('inner_place').find_element_by_class_name('tit_location').text
        for obj in objs:
            menu_name = obj.find_element_by_class_name('loss_word').text
            menu_price = obj.find_element_by_class_name('price_menu').text
            sql = "insert into MYMENU values(:1,:2,:3)"
            data = (title2,menu_name,menu_price)
            self.cursor.execute(sql,data)
        self.conn.commit() 
        self.cursor.close()
        self.conn.close()
            
    def __del__(self):
        pass

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
            
        





