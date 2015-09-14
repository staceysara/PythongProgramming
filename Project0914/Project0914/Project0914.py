#coding:cp949
#def sum_and_mul(a,b):
#    return a+b, a*b

#sum, mul  = sum_and_mul(10,30)
#print(sum,mul)
#-------------

#def printData(data):
#    for item in data:
#        if isinstance(item,list): #item이 list이면
#            for items in item:
#                print(items)
#        else:
#            print(item)

#data = ["홍길동",["베테랑","암살"],"고길동",["베테랑","명량","뭐"],"김길동",["가","나","다"]]

#printData(data)
#-------------리스트안에 리스트안에 리스트가 들어가있는 경우 위의 예에서 재귀함수를 돌림
#함수인자에 들여쓰기 할 횟수를 넣어줌
#def printData(data,level=0):
#    for item in data:
#        if isinstance(item,list): #item이 list이면
#            printData(item,level+1)
#        else:
#            for i in range(level):
#                print('\t',end='')
#            print(item)

#data = ["홍길동",["베테랑",["류승완","황정민","유아인"]],"고길동",["베테랑","명량","뭐"],"김길동",["가","나","다"]]

#printData(data)
#--------------------헤더파일 정의하듯이 printData함수를 따로 파일로 만들어서 여기서는 import해서 씀
#import printData #printData: 모듈이름

#data = ["홍길동",["베테랑",["류승완","황정민","유아인"]],"고길동",["베테랑","명량","뭐"],"김길동",["가","나","다"]]
#printData.printData(data)#모듈이름, 함수이름 쓰면 됨
#---------------
#import os

#help(os.mkdir)
import os

print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
#print(os.getcwd())
#os.system("python setup.py sdist")
os.system("python setup.py install")