import threading 

def printChar(start, stop):
    pass
    for i in range(start,stop):
        print(chr(i),end='')
        if(i % 100 ==0):
            print()
    
def printNumber(start, stop):
    pass
    for i in range(start, stop):
        print(i,end='')
        if(i % 100 ==0):
            print()

if __name__ == '__main__':
    t = threading.Thread(target=printChar, args=(1,10000))
    t.start()
    t2 = threading.Thread(target=printNumber, args=(1,10000))
    t2.start()
    
    
    
