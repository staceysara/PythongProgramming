#class A():
#    def __init__(self,a):
#        self.a = a
#    def show(self):
#        print('show:',self.a)

#class B(A):
#    def __init__(self,b,**arg):
#        super().__init__(**arg)
#        self.b = b
#    def show(self):
#        print('show:',self.b)
#        super().show()

#class C(A):
#    def __init__(self,c,**arg):
#        super().__init__(**arg)
#        self.c = c
#    def show(self):
#        print('show:',self.c)
#        super().show()

#class D(B,C):
#    def __init__(self,d,**arg):
#        super().__init__(**arg)
#        self.d = d
#    def show(self):
#        print('show:',self.d)
#        super().show()

#data = D(a=1,b=2,c=3,d=4)
#data.show()
#-----------------
#class Mapping:
#    def __init__(self, iterable):
#        self.items_list = []
#        self.__update(iterable)

#    def update(self, iterable):
#        for item in iterable:
#            self.items_list.append(item)
        
#    __update = update

#class MappingSubclass(Mapping):
#    def update(self, keys, values):
#        for item in zip(keys,values):
#            self.items_list.append(item)
      
##MappingSubclass객체를 만듬. 
#data = MappingSubclass([1,2,3,4])
#print(data.items_list)
#data.update('7','8')
#list=[9,10]
#print(data.items_list)
#-----------------
#import sys
#number1 = float(input("enter a number:"))
#number2 = float(input("enter a number:"))
#try:
#    result = number1/number2
#    print(result)
#except:
#    error = sys.exec_info()[0]
#    print(error)
#    sys.exit()#이렇게 시스템을 종료시켜줘도 finally까지 수행 하고 종료해줌
#finally:
#    print("Done")
#-------------












