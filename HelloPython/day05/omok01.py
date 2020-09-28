import sys

from PyQt5 import uic
from PyQt5.QtGui import *  # qPixmap을 사용하기 위해 임포트
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from spyder.app.tests.script import arr


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok01.ui")[0]
arr = [[0 for col in range(10)] for row in range(10)]
msg ="33"
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.ie =QIcon("0.jpg")
        self.iw =QIcon("1.jpg")
        self.ib =QIcon("2.jpg")
        
        for i in range(10):
            for j in range(10):
                self.pb = QPushButton('', self)
                self.pb.setIcon(self.ie)
                self.pb.setGeometry(i*75,j*75,75,75)
                self.pb.setIconSize(QtCore.QSize(75,75))
                self.pb.setText(str(i)+","+str(j))
                global arr
                arr[i][j] = self.pb.text()
#                 global msg
#                 msg = "테스트"
                self.pb.clicked.connect(self.myclick)
#                 print(arr[i][j])
                
    def myclick(self):
        print(arr[i][j])
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()