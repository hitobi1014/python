import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtGui, QtCore

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok02.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.ie = QIcon("0.png")        #전역 변수
        self.iw = QIcon("1.png")
        self.ib = QIcon("2.png")
        self.flagTurn = True
        self.flagIng = True
        self.int2d = [
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
                    ]
        
        self.arr2d = []

        for i in range(20):
            arr = []
            for j in range(20):
                pb = QPushButton('', self)
                pb.setGeometry(j*40,i*40, 40, 40)
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setIcon(self.ie)
                pb.setWhatsThis("{},{}".format(i,j))
                pb.clicked.connect(self.myclick)
                arr.append(pb)
            self.arr2d.append(arr)   
        self.mydraw()     
                
                
    def myclick(self):
        
        if not self.flagIng:
            return
        
        
        a = self.sender().whatsThis()
        b = a.split(",")
        ii = int(b[0])
        jj = int(b[1])
        
        cnt_stone = 0
        if self.int2d[ii][jj] > 0:
            return
        
        if self.flagTurn :
            self.int2d[ii][jj] = 1
            cnt_stone = 1
        else :
            self.int2d[ii][jj] = 2
            cnt_stone = 2
        self.mydraw()

        up_cnt = self.getUp(ii,jj,cnt_stone)
        dw_cnt = self.getDown(ii,jj,cnt_stone)
        le_cnt = self.getLeft(ii,jj,cnt_stone)
        ri_cnt = self.getRight(ii,jj,cnt_stone)
        upri_cnt = self.getUpRight(ii,jj,cnt_stone)
        uple_cnt = self.getUpLeft(ii,jj,cnt_stone)
        dwri_cnt = self.getDownRight(ii,jj,cnt_stone)
        dwle_cnt = self.getDownLeft(ii,jj,cnt_stone)
        
        cnt5p = [0,0,0,0]
        
        cnt5p[0] = up_cnt + dw_cnt+1
        cnt5p[1] = le_cnt + ri_cnt+1
        cnt5p[2] = upri_cnt + uple_cnt+1
        cnt5p[3] = dwri_cnt + dwle_cnt+1
        
        for i in range(4):
            if cnt5p[i] == 5:
                if self.flagTurn:
                    QMessageBox.about(self,"Qmok" ,"흰돌이 이김")
                else :
                    QMessageBox.about(self,"Qmok" ,"검은돌이 이김")    
        
                self.flagIng=False   
        
        print("up_cnt : {}".format(up_cnt))
        print("dw_cnt : {}".format(dw_cnt))
        print("le_cnt : {}".format(le_cnt))
        print("ri_cnt : {}".format(ri_cnt))
        print("upri_cnt : {}".format(upri_cnt))
        print("uple_cnt : {}".format(uple_cnt))
        print("dwri_cnt : {}".format(dwri_cnt))
        print("dwle_cnt : {}".format(dwle_cnt))
        
        self.flagTurn = not self.flagTurn
        
        
    def getUp(self,ii,jj,cnt_stone):
        cnt = 0
        while (True):
            ii -= 1
            if ii < 0 or ii >=len(self.int2d):
                return cnt
            if jj < 0 or jj >=len(self.int2d):
                return cnt
            
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else :
                break
      
        return cnt
    
    def getDown(self,ii,jj,cnt_stone):
        cnt = 0
        while (True):
            ii += 1
            
            if ii < 0 or ii >=len(self.int2d):
                return cnt
            if jj < 0 or jj >=len(self.int2d):
                return cnt
            
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else :
                break
      
        return cnt
    
    
    def getLeft(self,ii,jj,cnt_stone):
        cnt = 0
        while (True):
            jj -= 1
            
            if ii < 0 or ii >=len(self.int2d):
                return cnt
            if jj < 0 or jj >=len(self.int2d):
                return cnt
            
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else :
                break
      
        return cnt
    
    def getRight(self,ii,jj,cnt_stone):
        cnt = 0
        while (True):
            jj += 1
            
            if ii < 0 or ii >=len(self.int2d):
                return cnt
            if jj < 0 or jj >=len(self.int2d):
                return cnt
            
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else :
                break
      
        return cnt
    
    def getUpRight(self,ii,jj,cnt_stone):
        cnt = 0
        while (True):
            jj += 1
            ii -= 1
            
            if ii < 0 or ii >=len(self.int2d):
                return cnt
            if jj < 0 or jj >=len(self.int2d):
                return cnt
            
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else :
                break
      
        return cnt
    
    def getUpLeft(self,ii,jj,cnt_stone):
        cnt = 0
        while (True):
            jj -= 1
            ii -= 1
            
            if ii < 0 or ii >=len(self.int2d):
                return cnt
            if jj < 0 or jj >=len(self.int2d):
                return cnt
            
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else :
                break
      
        return cnt
               
           
    def getDownLeft(self,ii,jj,cnt_stone):
        cnt = 0
        while (True):
            jj -= 1
            ii += 1
            
            
            if ii < 0 or ii >=len(self.int2d):
                return cnt
            if jj < 0 or jj >=len(self.int2d):
                return cnt
            
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else :
                break
      
        return cnt
    
    def getDownRight(self,ii,jj,cnt_stone):
        cnt = 0
        while (True):
            jj += 1
            ii += 1
            
            
            if ii < 0 or ii >=len(self.int2d):
                return cnt
            if jj < 0 or jj >=len(self.int2d):
                return cnt
            
            if self.int2d[ii][jj] == cnt_stone:
                cnt += 1
            else :
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
                if self.int2d[ii][channel== 0:
                    item.setIcon(self.ie)
                if self.inchannelii][jj] == 1:
                    item.setIcon(self.iw)
                if self.inchannelii][jj] == 2:
                    item.setIcon(self.ib)
                jj += 1
 channel       ii+= 1 
        
                
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()