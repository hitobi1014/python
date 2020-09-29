import sys

from PyQt5 import QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtGui import *  # qPixmap을 사용하기 위해 임포트
from PyQt5.QtWidgets import *


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok01.ui")[0]
# arr = [[0 for col in range(10)] for row in range(10)]
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.ie =QIcon("0.jpg")
        self.iw =QIcon("1.jpg")
        self.ib =QIcon("2.jpg")
        self.int2d = [
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,1,0,0,0, 0,0,0,0,0],
                        [0,0,2,0,0, 0,0,0,0,0],
                        [0,0,0,2,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0]
                    ]
        self.arr2d = []
        for i in range(10):
            arr = []
            arr.append(object)
            
        for i in range(10):
            arr = []
            for j in range(10):
                pb = QPushButton('', self)
                pb.setIcon(self.ie)
                pb.setGeometry(i*75,j*75,75,75)
                pb.setIconSize(QtCore.QSize(75,75))
                pb.setWhatsThis("{},{}".format(i,j))
                pb.clicked.connect(self.myclick)
                arr.append(pb)
            self.arr2d.append(arr)
        self.mydraw()
                
    def myclick(self):
        print(self.sender().whatsThis())
        self.myshow2d()
        self.mydraw()
    
    def myshow2d(self):
        for arr in self.int2d:
            print(arr)
            
    def mydraw(self):
        ii = 0
        for line in self.arr2d:
            jj = 0
            for item in line:
                if self.int2d[ii][jj] == 0:
                    item.setIcon(self.ie)
                if self.int2d[ii][jj] == 1:
                    item.setIcon(self.iw)
                if self.int2d[ii][jj] == 2:
                    item.setIcon(self.ib)
                jj +=1
            ii +=1
                 
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()