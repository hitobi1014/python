import sys
import threading 
import time

from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


form_class = uic.loadUiType("my_rgb.ui")[0]

    
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        self.index = 0 
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.on_click)
    
    def on_change(self,s,e):
        r = 'background:rgb(255,0,0)'
        g = 'background:rgb(0,255,0)'
        b = 'background:rgb(0,0,255)'
        for _ in range(s,e):
            if self.index % 3 == 0: 
                self.ler.setStyleSheet(r)
                self.leg.setStyleSheet(g)
                self.leb.setStyleSheet(b)
            if self.index % 3 == 1: 
                self.ler.setStyleSheet(b)
                self.leg.setStyleSheet(r)
                self.leb.setStyleSheet(g)
            if self.index % 3 == 2: 
                self.ler.setStyleSheet(g)
                self.leg.setStyleSheet(b)
                self.leb.setStyleSheet(r)
            time.sleep(1)
            self.index += 1
            
    def on_click(self):
        print("on_change")
        t2 = threading.Thread(target=self.on_change, args=(1,10))
        t2.start()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()