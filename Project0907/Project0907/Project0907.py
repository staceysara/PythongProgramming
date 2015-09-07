#data = ['a','b','c',['abcd','efg']]
#print(data[0])
#print(data[-1])
#print(data[3])
#print(data[3][1])
#----------------
#a=[]
#b = [1,2,3]
#c =['Life','is','too','short']
#print(b+c)
#f =[]
#f = (b+c)
#print(f)
#print(b*3) 
#________________

#guests = ['a','b','c','d']
#guests[1]=['greenjoa1','greenjoa2']
#print(guests)
#guests[1:2]=['greenjoa1''greenjoa2']
#print(guests)
#_________________

#guests=['a','b','c','d']
#guests.insert(2,'e')
#guests.append('greenjoa2')
#print(guests)
#------------
#id값이 3개 있는 리스트를 만들어볼것
#lists = ['id1','id2','id3']
#lists.insert(1,'password1')
#lists.insert(3,'password2')
#lists.insert(5,'password3')

#print(lists)
#----------------------
#guests = ['a','b','c','d']

#for setps in range(4):
#        print(guests[steps])
#-------------
#data = ['a','b','c',['abcd','efg']]
#for steps in data:
#    print(steps)

#------------range(),for---
#data = ['a','b','c',['abcd','efg']]
#for steps in range(4):
#    print(data[steps])#각각의 원소 하나하나를 접근
#-------------sort(), reverse()--------
#scores =[52,12,45,65,78]
#scores.sort()
#print(scores)#score의 상위 2개를 top3에 넣고 출력해보기
#top5=[]
#for steps in range(2):
#    top5.append(scores[steps])
#print(top5)

#scores.reverse()
#print(scores)

#------------------------list안의 list에 접근하고 싶을때 
#data = ['a','b','c',['abcd','efg']]
#for steps in data:
#    if isinstance(steps,list):#steps가 list타입이면(steps가 list의 instance이면
#        for step in steps:
#            print(step)
#    else:
#        print(steps)
#---------------------pop(), count(), extend()
#scores=[85,62,63,45,90]
#num = scores.pop()
#print(scores)
#num = scores.pop(2)
#print(scores)

#scores=[85,62,63,45,90,63]
#num = scores.count(63)
#print(num)
#-----------------append와 extend의 차이
#scores=[85,62,63,45,90]
#scores.extend([50,60])
#print(scores)#[85,62,63,45,90,50,60]

#scores=[85,62,63,45,90]
#scores.append([50,60])
#print(scores)#[85,62,63,45,90,[50,60,]]

#--------------tuple이용. tuple은 변경이 안됨. 읽기만 가능한 데이터
#t1=()
#print(t1)
#t2 = (1,)#t2=(1)과 다름
#print(t2)
#t3=(1,2,3)
#print(t3)
#t4=1,2,3
#print(t4)
#t5=('a','b',('ab','cd'))
#print(t5)





