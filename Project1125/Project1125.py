import numpy as np
from matplotlib import pyplot as plt
#data = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(data.ndim)
#print(data.shape)
#print(len(data))
#np.array는 모두 같은 데이터형을 가짐.
#data = np.array([[1,2,3],[4,5,6],[7,8,9.]])
#data1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
#data1.astype(np.float)
#data1 = np.array(['1','2','3'])
#data1.astype(np.int)
#data1 = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)
#data1 = np.array([1,2,3],dtype=complex)
#np.ones((3,2))
#print(data)
#np.zeros(3,2)

#------
#data = np.array([[1,2,3,4]])
#print(data.T)#transpose시킨거. 전치행렬로 구해짐.
#data1 = np.arange(10)
#print(data1)#[0 1 2 3 4 5 6 7 8 9]
#data1 = np.arange(10,1,-1)#start, end, step
#print(data1)#[10 9 8 7 6 5 4 3 2]
#data1 = np.arange(35).reshape(5,7)
#print(data1)#[[0 1 2 3 4 5 6] [7~13] [28~34]]로 됨
#data1 = np.linspace(1.,4.,6)
#print(data1)#[1. 1.6 2.2  2.8 3.4 4.]
#data1 = np.linspace(1.,4.,6,endpoint=False)
#print(data1)#[1. 1.5 2. 2.5 3. 3.5]
##난수발생으로 임의로 배열 채워주기
#data = np.random.rand(4)
#print(data)#0.5205 0.2374 0.011 0.022
#data = np.random.randn(4)#가우시안분포로해줌
#print(data)
#data = np.random.randn(4,4)#가우시안분포로 4by 4
#print(data)
#===========
#data.txt로부터 데이터읽어서 그래프그리기
#data = np.loadtxt('data.txt')
#year,hares,lynxes,carrots = data.T
#plt.plot(year,hares,year,lynxes,year, carrots)
#plt.show()

##인덱스&슬라이싱
#data= np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
#print(data[0])#[1,2,3,4]
#print(data[-1])#마지막에 해당하는건 -1[7 8 9 10]
#print(data[0:2])#[[1 2 3 4][4 5 6 7]]맨 마지막(2)는 포함되지 않음
#print(data[0:1])#[[1 2 3 4]]
#print(data[1:4:2])#[[4 5 6 7]]이거 왜이렇게 되는지몰겠음
#print(data[::-1])#처음부터끝까지[[7 8 9 10][4 5 6 7][1 2 3 4]]
#print(data[2,0])#7 //이렇게 각 원소에 해당하는거 access할 수 있음
##특정부분만 slice해서 가져올수도
##인덱스에해당하는번호를 줄수있음
#x = np.arange(10,1,-1)
#print(x[np.array([3,3,2,8])])#인덱스값을줌[7 7 8 2] 특정부분을인덱스배열로 만들수있음
#print(x[np.array([[1,1],[2,3]])])#[[9 9][8 7]]
#y = np.arange(35).reshape(5,7)#5by7이었음
#print(y[np.array([0,2,4])])#0행, 2행,4행이 출력됨
#b = y>20
#print(y[b])#[21 22 23 24 25 26 27 28 29 30 31 32 33 34]

data = np.arange(36).reshape(6,6)
print(data)
mask = np.array(np.array([1,0,1,0,0,1],dtype=bool))
print(mask)#[True False True False False True]
print(data[mask,2])#[2 14 32] 각 행마다 3번째 원소를 봐서  true인것만 가져옴

mask1 = np.array([0,1,2,3,4])
mask2 = np.array([1,2,3,4,5])
print(data[mask1,mask2])#[1 8 15 22 29] 0행에서 1번째꺼...~4행에서 5번째꺼

#boolean masks강의자료에 있는하늘색깔을 할 수 있음.
mask3 = np.array([0,2,5])
print(data[3:,mask3])


















