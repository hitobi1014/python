class Animal:
    def __init__(self):
        self.age = 0
    def getOlder(self):
        self.age += 1
        
class Human(Animal):
    def __init__(self):
#         Animal.__init__(self)
        super().__init__()
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
    print(hum.age)
    hum.getOlder()
    print(hum.age)
