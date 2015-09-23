#class  Terran:
#    def __init__(self, name):
#        self.name = name

#class Tank(Terran):
#    def __init__(self,name,damage):
#        super().__init__(self, name)
#        self.damage = damage

#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(self, name)
#        self.hp = hp

#t1 = Tank("tank",0)
#t2 = Marine("marine",100)

#------------------Terran클래스를 추상클래스로 만들어보자
#Terran으로부터 파생된 애들한테는 공격 기능을 넣고 싶음. 그럼 부모클래스에 넣어놓으면 됨
#Terran은 body를 정의할 수 없음. 그때 abstract메소드로 정의하면 됨
#from abc import ABCMeta, abstractmethod
#class Terran(metaclass=ABCMeta):#class에 대한 부가적인 정보 넣어줌. metaclass에 대한 정보를 ABCMeta라고 
#    def __init__(self, name):
#        self.name = name

#    @abstractmethod
#    def attack(self):
#        pass

#class Tank(Terran):
#    def __init__(self,name,damage):
#        super().__init__(name)
#        self.damage = damage

#    def attack(self):
#        print("탱크를 쏩니다")
#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(name)
#        self.hp = hp

#    def attack(self):
#        print("총을 쏩니다")

#def Attack(terran):
#    terran.attck()

#t1 = Tank("tank",0)
#t2 = Marine("marine",100)

#tlist = [Tank("tank1",0),Marine("marine1",100)]
#for item in tlist:
#    Attack(item)
#Attack(t1)
#Attack(t2)
#-------------
#class MyList(list):#list로부터 파생되어진 클래스를 만들고 싶음
#    name=""
#    def __init__(self, name):#리스트기능도 가지고 있고 이름도 있는걸 만들고싶음
#        super().__init__([])#빈 리스트 하나 생성해줌
#        self.name = name

#list1=MyList("greenjoa")
#list1.append(10)#list에 추가시키는거
#list1.append(50)
#list1.append(60)
#list1.append(80)
#list1.append(100)
#print(list1)#이름도 같이 출력이 되었으면 좋겠으면 연산자 재정의를 통해서 해결할 수 있음
#print(dir(list1))#리스트에 있는 기능들 볼 수 있음 list에서 가질 수 있는 멤버들을 표시해줌
#                    #리스트에 넣은건 name밖에 없음. name이라는 기능이 추가가 되어져있음.

#------------------print할때 출력하는건 string함수를 통해서 출력이 됨. string함수를 재정의 할거임.
class MyList(list):#list로부터 파생되어진 클래스를 만들고 싶음
    name=""
    def __init__(self, name):#리스트기능도 가지고 있고 이름도 있는걸 만들고싶음
        super().__init__([])#빈 리스트 하나 생성해줌
        self.name = name
    def __str__(self):
        return self.name+":"+super().__str__()#list의 str함수가 호출됨. 

list1=MyList("greenjoa")
list1.append(10)#list에 추가시키는거
list1.append(50)
list1.append(60)
list1.append(80)
list1.append(100)
print(list1)#이름도 같이 출력이 되었으면 좋겠으면 연산자 재정의를 통해서 해결할 수 있음

                 