#list = [1,2,3,4]

#print(dir(list))
#data =list
#----------
#data = list(enumerate("greenjoa"))
#print(data)
#-------
#def positive(l):
#    result=[]
#    for i in l:
#        if i>0:
#            result.append(i)
#        return result
#print(positive[1,-3,2,0,-5,6])
#------------filter사용

#def positive(l):
#    return l%2==0
#print(list(filter(positive,[1,2,3,4,5])))
#-----------id이용. 반환
#a = 3
#print(id(3))
#print(id(a))
#-------
#print(int('3'))
#int(3.5)
#int('11',2)
#int('1A',16)
#----------lambda:필터와 같이 쓰일 때 딱임
#print(list(filter(lambda x:x%2==0,[1,2,3,4,5])))
#----------len이용:길이반환
#len([1,2,3,4])
#len("greenjoa")
#----------a: 123b:리스트 a한거, c: b를 대입  id값 출력. id값이 어케다른지보기
#a=[1,2,3]
#b = list(a)
#c=[]
#for i in b:
#    c.append(i)
#print(id(a))
#print(id(b))
#print(id(c))
#--------map이용mapping되는걸 출력
#def two_times(x):return x*2
#print(list(map(two_times,[1,2,3,4])))
#print(list(map(lambda a:a*2,[1,2,3,4])))
#----------repr은 eval과 주로 사용
#print(eval(repr("hi".upper())))
#----------sorted(): sorting해줌
#list=[10,2,5,4,3,6,7,8,9,1]
#print(sorted(list))
#print(list)
#--------예전에는 sort를 이렇게 함.
#list=[10,2,5,4,3,6,7,8,9,1]
#list.sort()
#print(list)
#----------zip이용 1과'A'를 묶고... 그런식으로 함.
#A=[1,2,3]
#B=['A','B','C']
#for i in zip(A,B):
#    print(i)
#-------각 리스트에 해당하는걸 정렬하기. data의 홍길동하면 정렬되어서
#data={'홍길동':[80,70,60,92],'김길동':[24,35,18,10],'고길동':[10,20,8,5]}

#data.keys()
#for i in data.values():   
#       i=i.sort()

#print(data['홍길동'])#이랬을때 60 70 80 92
#print(data)
#-------
data={'홍길동':[80,70,60,92],'김길동':[24,35,18,10],'고길동':[10,20,8,5]}
#홍길동, 김길동, 고길동 각각의 values값 정렬
for name in data.keys():
    data[name].sort()
print(data['홍길동'])
print(data)

#이름순으로 values값 정렬
l = list(data.keys())
l.sort()
myList=[]
for name in l:
    myList.append(name)
    myList.append(data[name])
print(myList)

