import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

form_class = uic.loadUiType("tetris.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.block2D = []
        self.stack2D = []
        self.scrin2D = []
        self.lbl2D = []
        
        self.initBlock2DStack2DScrin2D()
        self.scrin2D[0][0]=1
        self.scrin2D[0][1]=1
        self.scrin2D[1][1]=1
        self.scrin2D[2][1]=1
        
        for i in range(20):
            for j in range(10):
                lbl = QLabel('',self)
                lbl.setGeometry(j*25, i*25, 24,24)
                lbl.setStyleSheet("background-color : rgb(56,56,56)")
                self.lbl2D[i][j] = lbl
                
        self.myrender()
        self.print2D(self.scrin2D)
        
    def initBlock2DStack2DScrin2D(self):
        for _ in range(20):
            self.block2D.append([0,0,0,0,0 ,0,0,0,0,0])
            self.stack2D.append([0,0,0,0,0 ,0,0,0,0,0])
            self.scrin2D.append([0,0,0,0,0 ,0,0,0,0,0])
            self.lbl2D.append([0,0,0,0,0 ,0,0,0,0,0])
            
    def print2D(self,arr):
        print("--------------------------------")
        for line in arr:
            print(line)
            
    def myrender(self):
        for i in range(20):
            for j in range(10):
                if self.scrin2D[i][j] ==0 :
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(56,56,56)")
                if self.scrin2D[i][j] ==1 :
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(252,252,12)")
                if self.scrin2D[i][j] ==2 :
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(1,239,243)")
                if self.scrin2D[i][j] ==3 :
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(243,1,9)")
                if self.scrin2D[i][j] ==4 :
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(53,243,1)")
                if self.scrin2D[i][j] ==5 :
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(239,1,243)")
                if self.scrin2D[i][j] ==6 :
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(243,130,1)")
                if self.scrin2D[i][j] ==7 :
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(1,77,243)")
                    
                if self.scrin2D[i][j] ==11:
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(252,252,12)")
                if self.scrin2D[i][j] ==12:
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(1,239,243)")
                if self.scrin2D[i][j] ==13:
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(243,1,9)")
                if self.scrin2D[i][j] ==14:
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(53,243,1)")
                if self.scrin2D[i][j] ==15:
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(239,1,243)")
                if self.scrin2D[i][j] ==16:
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(243,130,1)")
                if self.scrin2D[i][j] ==17:
                    self.lbl2D[i][j].setStyleSheet("background-color : rgb(1,77,243)")

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()