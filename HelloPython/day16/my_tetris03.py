import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt

form_class = uic.loadUiType("tetris.ui")[0]
class Block():
    def __init__(self):
        self.kind =6
        self.status = 1
        self.i = 1
        self.j = 5
    
    def __str__(self):
        return str(self.kind) + "," + str(self.status) + "," + str(self.i) + "," + str(self.j) 
    
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.block2D = []
        self.stack2D = []
        self.scrin2D = []
        self.lbl2D = []
        self.block = Block()
        
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
        print(self.block)
        
    def keyPressEvent(self,e):
        keycode = e.key()
        if keycode==16777235 :
            self.changeBlockStatus()
        if keycode==16777234 : # 왼쪽
            self.block.j -= 1
        if keycode==16777236 : #오른쪽
            self.block.j += 1
        if keycode==16777237 : #아래
            self.block.i += 1
            
        try:
            self.setBlock2DWithBlock()
        except:
            print("예외발생")
            
        self.moveStackBlock2Scrin()
        self.myrender()
        
    def changeBlockStatus(self):
        if self.block.kind == 1:
            pass
        if self.block.kind == 2 or self.block.kind == 3 or self.block.kind == 4:
            if self.block.status == 1: 
                self.block.status = 2
            elif self.block.status == 2:
                self.block.status = 1
        if self.block.kind == 5 or self.block.kind == 6 or self.block.kind == 7:
            if self.block.status == 1:
                self.block.status = 2
            elif self.block.status == 2:
                self.block.status = 3
            elif self.block.status == 3:
                self.block.status = 4
            elif self.block.status == 4:
                self.block.status = 1
                
    def moveStackBlock2Scrin(self):
        for i in range(20):
            for j in range(10):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                self.scrin2D[i][j] = self.stack2D[i][j]+self.block2D[i][j]
                
    def setBlock2DWithBlock(self):
        for i in range(20):
            for j in range(10):
                self.block2D[i][j] = 0
        if self.block.kind == 1:
            self.block2D[self.block.i][self.block.j]=self.block.kind
            self.block2D[self.block.i][self.block.j+1]=self.block.kind
            self.block2D[self.block.i+1][self.block.j]=self.block.kind
            self.block2D[self.block.i+1][self.block.j+1]=self.block.kind
            
        if self.block.kind ==2 :
            if self.block.status == 1:
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i+2][self.block.j]=self.block.kind

            if self.block.status == 2:
                self.block2D[self.block.i][self.block.j-2]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
        
        if self.block.kind == 3:
            if self.block.status == 1:
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j+1]=self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j-1]=self.block.kind
        
        if self.block.kind == 4:
            if self.block.status == 1:
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j-1]=self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i-1][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
        
        if self.block.kind == 5:
            if self.block.status == 1:
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
            if self.block.status == 3:
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
            if self.block.status == 4:
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind

        if self.block.kind == 6:
            if self.block.status == 1:
                self.block2D[self.block.i-1][self.block.j-1]=self.block.kind
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
            if self.block.status == 2:
                self.block2D[self.block.i-1][self.block.j+1]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
            if self.block.status == 3:
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j+1]=self.block.kind
            if self.block.status == 4:
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j-1]=self.block.kind

        if self.block.kind == 7:
            if self.block.status ==1:
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j-1]=self.block.kind
            if self.block.status ==2 :
                self.block2D[self.block.i-1][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
            if self.block.status ==3 :
                self.block2D[self.block.i-1][self.block.j]=self.block.kind
                self.block2D[self.block.i-1][self.block.j+1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i+1][self.block.j]=self.block.kind
            if self.block.status ==4 :
                self.block2D[self.block.i][self.block.j-1]=self.block.kind
                self.block2D[self.block.i][self.block.j]=self.block.kind
                self.block2D[self.block.i][self.block.j+1]=self.block.kind
                self.block2D[self.block.i+1][self.block.j+1]=self.block.kind
            
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