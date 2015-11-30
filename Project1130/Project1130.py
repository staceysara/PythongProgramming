import numpy as np
from matplotlib import pyplot as plt
#data = np.array([[1,2,3],[4,5,6],[7,8,9]])

#print(data+2)#[[3 4 5][6 7 8][9 10 11]]
#print(data-2)#[[-1 0 1][2 3 4][5 6 7]]
#print(data*data)#[[1 4 9][16 25 36][49 64 81]]#not a matrix multiplication

#print(data.dot(data))#[[30 36 42][66 81 96][102 126 150]]
#------------------
#a = np.array([1,2,3,4])
#b = np.array([4,2,2,4])
#c = np.array([1,2,3,4])
##이렇게 하면 각 원소에 대한 비교임.
#print(a==b)#False true false true
#print(a>b)#false false true false
##array전체에 대한 비교
#print(np.array_equal(a,b))#false
#print(np.array_equal(a,c))#true
#----------------
#a = np.array([1,1,0,0],dtype=bool)
#b = np.array([1,0,1,0],dtype=bool)
#print(np.logical_or(a,b))#[true true true false]
#print(np.logical_and(a,b))#[true false false false]
#---------
#print(np.all([True,True,False]))#안에있는게 다 true여야 true임
#print(np.any([True,True,False]))#하나라도 true이면 true임.
#---------
#a = np.arange(5)
#print(np.sin(a))
#print(np.log(a))
#print(np.exp(a))
#-------
#전이행렬
#a = np.triu(np.ones((3,3)),1)#triu: 삼각매트릭스를 만들 수 있음. 상삼각행렬
##전체가 1로 채워진 3 by 3 매트릭스를 삼각행렬로 만들겠다. 1:인덱스번호. 대각선에 해당하는게 1임. 인덱스번호를 어디에다주느냐에따라 어디를 채울지 알려줌.
##-1로 주면 아래부터 채워질거임?
#print(a)#[0. 1. 1.][0. 0. 1.][0. 0. 0.]]
#print(a.T)#[0. 0. 0.][1. 0. 0.][1. 1. 0.]]
#------
#a = np.triu(np.ones((3,3)),0)
#print(a)
#------------
#x = np.array([1,2,3,4])
#print(np.sum(x))#10
#print(x.sum())#10
#-----
#x = np.array([[1,1],[2,2]])
#print(x.sum())#6
#print(x.sum(axis=0))#[3 3]축에해당하는값을더함 0: 열을 위주로 합이 구해짐
#print(x.sum(axis=1))#[2 4]행을위주로 합이 구해짐 
#print(x[0,:].sum(),x[1,:].sum())#2 4
#-------------
#x = np.array([1,3,2])
#print(x.min())#1
#print(x.max())#3
#print(x.argmin())#0 #index of minimum
#print(x.argmax())#1 #index of maximum
#-----------
#논리연산이라하더라도 이거 하나만갖고사용되는게아니라 다른연산과 같이 사용됨
#np.all([True, True, False])
#np.any([True, True, False])
#* 배열비교할때주로사용
#a = np.zeros((100,100))
#np.any(a!=0)
#np.all(a==a)

#--------
#x = np.array([1,2,3,1])
#y = np.array([[1,2,3],[5,6,1]])
#print(x.mean())#1.75 평균값구함
#print(np.median(x))#1.5 중간값구함 원소들중에 중간값에 해당하는거
#print(np.median(y,axis=-1))#[2. 5.] #last axis
#print(x.std())#표준편차?
#---------
#pyplot를 import해야. 
data = np.loadtxt('data.txt')
year,hares,lynxes,carrots = data.T#데이터를 전이행렬로 받아옴
#plt.plot(year,hares,year,lynxes,year,carrots)#이거에 해당하는데이터들을 그려줘라. 연도와 산토끼, 연도와 시라소니, 연도와 당근 3개의 항목에대해 차트에보여줌.
#3개의 그래프가 나올거임
#plt.show()
#연도별평균?산토끼, 시라소니, 당근에해당하는연도별평균
#print(year)
#전체에 대한 평균, 표준편차 내가구함
#x = np.array(data.T)
#print(x)
#sum1 = np.array(x.sum(axis=0))
#print("전체다더해서 평균,표준편차")
#print(sum1.mean())
#print(sum1.std())
#각각에 해당하는 평균, 표준편차
#산토끼에 대한 평균, 표준편차
#print("산토끼 평균, 표준편차")
#hareMean = hares.mean()
#hareStd=hares.std()
#print(hareMean)
#print(hareStd)
#print("스라소니 평균, 표준편차")
#lynxesMean = lynxes.mean()
#lynxesStd = lynxes.std()
#print(lynxesMean)
#print(lynxesStd)
#print("당근 평균, 표준편차")
#carrotMean = carrots.mean()
#carrotStd = carrots.std()
#print(carrotMean)
#print(carrotStd)
#최대개체수를 갖는 연도
#print("hare가 최소인연도")
#arHARES = hares.argmin()
#print(year[arHARES])
#print("lynxes가 최소인연도")
#arLYNXES = lynxes.argmin()
#print(year[arLYNXES])
#print("carrot이 최소인연도")
#arCARROT = carrots.argmin()
#print(year[arCARROT])
#---------
row = np.array([[0,10,20,30,40,50]])#[이거 하나만 붙이면 벡터임. 배열이 아니고. 
row = row.T#T연산은 [[ 이렇게 2개가 있어야. 
#row의 shape정보 보기
column = np.array([[0,1,2,3,4,5]])
print(row+column)























































