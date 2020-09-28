from random import *
# 랜덤함수 
# i = randint(1,100)
# print(i)

# print("숫자 입력")

i=randint(1,2)
if(i==1):
    com="홀"
else:
    com="짝"
    
mine = input("홀짝을 입력하세요")

if(com==mine):
    print("이겼습니다")
else:
    print("졌습니다")
    
print("컴퓨터 :"+com+" / 사용자 :"+mine)
