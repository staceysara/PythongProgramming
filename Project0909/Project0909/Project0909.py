#dic1 = {}
#dic2=dict()
#dic = {'name':'pey','phone':'0119993323','birth':'1118'}
#a = {1:'hi'}
#b = {'a':[1,2,3]}
#print(dic['name'])
#----------
#a = {'name':'pey','phone':'0119993323','birth':'1118'}
#b = a.keys()
#print(b)
#b =list(a.keys())
#print(b)
#b = a.values()
#print(b)
#b = a.items()
#print(b)
#a.get('name')
#-----------
#dic = {"홍길동":{"베테랑":5.0,"암살":4.5},"고길동":{"베테랑":4.0,"암살":3.5}}
##홍길동이 영화 암살을 몇 점을 주었는지
#print(dic.get("홍길동").get("암살"))
#print(dic["홍길동"]["암살"])
#--------------
#answer = input("Would you like express shipping?")
#ans1 = answer.upper()
#if ans1 == "YES":
#    print("That will be an extra $10")
#--------------
#a = [(1,2),(3,4),(5,6)]
#for(first,last)in a:
#    print(first+last)
    #---
#for i in range(2,10):
#    for j in range(1,10):
#        print(i,end="") 
#        print("x",end="")
#        print(j,end="")
#        print("=",end="")
#        print(i*j)
#    print("-------------")
#-------------

#for i in range(2,10):
#    for j in range(1,10):
#        print('%d x %d = %d'%(i,j,i*j)) 

#    print("-------------")
#----------------
#import turtle
#for steps in range(4):#4번동안 아래와 같이 움직일거임
#    turtle.forward(100)
#    turtle.right(90)
#    for moresteps in range(4):
#           turtle.forward(50)
#           turtle.right(90)
#---------------
#import turtle
#nSides=5
#for steps in range(nSides):
#    turtle.forward(100)
#    turtle.right(360/nSides)
#    for moresteps in range(nSides):
#        turtle.forward(50)
#        turtle.right(360/nSides)
#------------------
#import turtle
#for steps in ['red','blue','green','black']:
#    turtle.color(steps)
#    turtle.forward(100)
#    turtle.right(90)       
#-------------------
prompt="""
1.ADD
2.DEL
3.LIST
4.QUIT
Enter number:"""
number=0
while number!=4:
    print(prompt,end="")
    number=int(input())
