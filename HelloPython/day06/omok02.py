import sys

from PyQt5 import QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtGui import *  # qPixmap을 사용하기 위해 임포트
from PyQt5.QtWidgets import *


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok02.ui")[0]
# arr = [[0 for col in range(10)] for row in range(10)]
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.ie =QIcon("0.jpg")
        self.iw =QIcon("1.jpg")
        self.ib =QIcon("2.jpg")
        self.flag = True
        self.int2d = [
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
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
                pb.setGeometry(j*75,i*75,75,75)
                pb.setIconSize(QtCore.QSize(75,75))
                pb.setWhatsThis("{},{}".format(i,j))
                pb.clicked.connect(self.myclick)
                arr.append(pb)
            self.arr2d.append(arr)
        self.mydraw()
                
    def myclick(self):
#         print(self.sender().whatsThis())
        a = self.sender().whatsThis()
        b = a.split(",")
        ii = int(b[0])
        jj = int(b[1])
        cnt_stone = 0
        
        if self.int2d[ii][jj]>0:
            return
        
        if self.flag:
            self.int2d[ii][jj]=1
            cnt_stone = 1
        else :
            self.int2d[ii][jj]=2
            cnt_stone = 2
        
#         self.myshow2d()
        self.mydraw()
        
        up_cnt = self.getUp(ii,jj,cnt_stone)
        dw_cnt = self.getDw(ii,jj,cnt_stone)
        le_cnt = self.getLe(ii,jj,cnt_stone)
        ri_cnt = self.getRi(ii,jj,cnt_stone)
        upLe_cnt = self.getUpLe(ii,jj,cnt_stone)
        upRi_cnt = self.getUpRi(ii,jj,cnt_stone)
        dwLe_cnt = self.getDwLe(ii,jj,cnt_stone)
        dwRi_cnt = self.getDwRi(ii,jj,cnt_stone)
#         print("up_cnt:{}".format(up_cnt))
#         print("dw_cnt:{}".format(dw_cnt))
#         print("le_cnt:{}".format(le_cnt))
#         print("Ri_cnt:{}".format(ri_cnt))
#         print("upLe_cnt:{}".format(upLe_cnt))
#         print("upRi_cnt:{}".format(upRi_cnt))
#         print("dwLe_cnt:{}".format(dwLe_cnt))
#         print("dwRi_cnt:{}".format(dwRi_cnt))
        cnt5p = [0 for i in range(4)]
        cnt5p[0] = up_cnt + dw_cnt +1
        cnt5p[1] = le_cnt + ri_cnt +1
        cnt5p[2] = upLe_cnt + dwRi_cnt +1 
        cnt5p[3] = upRi_cnt + dwLe_cnt +1
        for i in len(cnt5p):
            if cnt5p[i] == 5:
                if self.flag:
                    print("흰돌이 이겼습니다")
                else:
                    print("흑돌이 이겼습니다")
        
        self.flag = not self.flag
    
    def getDwRi(self,ii,jj,cnt_stone):
        cnt = 0
        while True:
            ii += 1
            jj += 1
            if ii<0 or ii>=len(self.int2d):
                return cnt
            if jj<0 or jj>=len(self.int2d):
                return cnt
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else:
                break
        return cnt
    
    def getDwLe(self,ii,jj,cnt_stone):
        cnt = 0
        while True:
            ii += 1
            jj -= 1
            if ii<0 or ii>=len(self.int2d):
                return cnt
            if jj<0 or jj>=len(self.int2d):
                return cnt
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else:
                break
        return cnt
    
    def getUpRi(self,ii,jj,cnt_stone):
        cnt = 0
        while True:
            ii -= 1
            jj += 1
            if ii<0 or ii>=len(self.int2d):
                return cnt
            if jj<0 or jj>=len(self.int2d):
                return cnt
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else:
                break
        return cnt
    
    def getUpLe(self,ii,jj,cnt_stone):
        cnt = 0
        while True:
            ii -= 1
            jj -= 1
            if ii<0 or ii>=len(self.int2d):
                return cnt
            if jj<0 or jj>=len(self.int2d):
                return cnt
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else:
                break
        return cnt
    
    def getRi(self,ii,jj,cnt_stone):
        cnt = 0
        while True:
            jj += 1
            if ii<0 or ii>=len(self.int2d):
                return cnt
            if jj<0 or jj>=len(self.int2d):
                return cnt
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else:
                break
        return cnt
    
    def getLe(self,ii,jj,cnt_stone):
        cnt = 0
        while True:
            jj -= 1
            if ii<0 or ii>=len(self.int2d):
                return cnt
            if jj<0 or jj>=len(self.int2d):
                return cnt
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else:
                break
        return cnt
    
    def getDw(self,ii,jj,cnt_stone):
        cnt = 0
        while True:
            ii += 1
            if ii<0 or ii>=len(self.int2d):
                return cnt
            if jj<0 or jj>=len(self.int2d):
                return cnt
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else:
                break
        return cnt
    
    def getUp(self,ii,jj,cnt_stone):
        cnt = 0
        while True:
            ii -= 1
            if ii<0 or ii>=len(self.int2d):
                return cnt
            if jj<0 or jj>=len(self.int2d):
                return cnt
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else:
                break
        return cnt
    
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
