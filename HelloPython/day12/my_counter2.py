import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
import threading 
import time


form_class = uic.loadUiType("my_counter2.ui")[0]



    
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.on_click)
    
    def on_increase(self,start,stop):
        for _ in range(start,stop):
            a = int(self.lbl.text())
            a += 1
            self.lbl.setText(str(a))
            time.sleep(1)
    
    def on_click(self):
        print("on_increase")
        t2 = threading.Thread(target=self.on_increase, args=(1,10))
        t2.start()
#         self.test = TestThread(self)
#         self.test.start()
    
# class TestThread(QThread):
#     def run(self):
#         print(self.lbl.text())
#         a = int(self.lbl.text())
#         a=0
#         for _ in range(10):
#             self.lbl.setText(str(int(self.lbl.text())+1))
#             self.sleep(1)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()