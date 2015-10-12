#커맨드명령직접시스템에서 내릴 수 있었음. os에서 직접 시스템명령사용한거
import os
import sys
import pickle
import shutil
#os.system("python test.py a b c")#python이 path에 등록되어져있으면 이렇게 할 수 있음 python이 path에 등록되어있으면아무곳에서나실행가능
##test.py를 만들어서 그 파일을 실행시키는 구문을 만들어보기
##원래 python test.py a b c 이렇게 실행시키잖아
#print(sys.path)
#-------------pickle을 사용해서 txt파일에 쓰고 그대로 불러올거임
#class Student:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#    def show(self):
#        print(self.name,": " ,self.age)

#std1 = Student("greenjoa",23)
#std1.show()# 클래스객체를 저장할거임. 그 객체 그대로의 상태를 저장할거임. 그때 사용하는 모듈이 피클임.
#f = open("test.txt",'wb')
#data = std1
#pickle.dump(data,f)#피클을 사용하면 그대로 불러올 수 있음.
#f.close()

#f = open("test.txt",'rb')
#data = pickle.load(f)
#print(data)

#data.show()
#----------------------------os모듈: os와 관련된 것들과 관련
#print(os.environ)
#chdir: change dir     os.chdir('c:/')
#getcwd:현재 작업하고 있는 디렉토리를 알려줌. os.getcwd()
#print(os.getcwd())
#os.chdir('..')
#print(os.getcwd())
#os.chdir('./Project1012')
#print(os.getcwd())
#------------
#print(list(os.walk('..')))#상위 디렉토리에 있는 경로, 하위디렉토리, 파이릴스트를 반환
#------
#현재디렉토리에서 하위디렉토리까지 다 포함해서 txt //sample이라는 디렉토리를 만들고 거기에 프로젝트에서 만들었던 txt를 sample에 복사하기
#현재디렉토리에 sample디렉토리를 만들고 디렉토리 내에 있었던(하위에 있엇던)파일 중에서 txt파일을 sample디렉토리에 복사
#이거 하다 맘
#print(os.getcwd())
#list = list(os.walk('.'))
#print(list)
#t=0
#for i in list:
#    if i=='sample':
#        os.chdir('./sample')
#        os.rename('../test.txt','./test,txt')
#        t=1
#if t==0:  
#     os.mkdir('./sample')


#os.mkdir('./sample')
#list = os.rename('test.txt','./sample/')
#----------
print(os.path.dirname('c:/python34/python.exe'))
print(os.path.expanduser('~\\python.exe'))
print(os.path.splitext('C:\\Python34\\python.exe'))









