class Animal:
    def __init__(self):
        self.age = 0
    def getOlder(self):
        self.age += 1
        
class Bird():        
    def __init__(self):
        self.fly = 5
    def flying(self,meter):
        self.fly += meter
        
class Human(Animal,Bird):
    def __init__(self):
        Animal.__init__(self)
#         super().__init__()
        Bird.__init__(self)
        self.name="이재용"
    def changeName(self,name):
        self.name = name
        
if __name__ == '__main__':
#     ani= Animal()
#     print(ani.age)
#     ani.getOlder()
#     print(ani.age)
    hum = Human()
    print(hum.name)
    hum.changeName("강지우")
    print(hum.name)
    print("age 호출: {}".format(hum.age))
    hum.getOlder()
    print("getOlder호출 후 나이 : {}".format(hum.age))
    print("fly 기본 값 : {}".format(hum.fly))
    hum.flying(10)
    print("flying 후 fly값 : {}".format(hum.fly))
    
