# 가위바위보
from random import* 
com=""
user=""
result=""

i=randint(1,3)
if i==1:
    com="가위"
elif i==2:
    com="바위"
else:
    com="보"

user = input("가위바위보 중 하나를 입력하세요")

if com == user:
    result="비겼습니다"
elif (com=="가위" and user=="바위") or (com=="바위" and user=="보") or (com=="보" and user=="가위"):
    result="이겼습니다"
else:
    result="졌습니다"

print("컴퓨터:{}".format(com))
print("사용자:{}".format(user))
print("결과:{}".format(result))