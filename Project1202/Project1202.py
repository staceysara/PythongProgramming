import numpy as np
from matplotlib import pyplot as plt
########********강의자료에있는거다다시하기이때상태안좋았음
#newaxis: 새로축으로 나타내짐
#강의자료에있는 두 도시사이의 거리구하기
#mileposts = np.array([0,198,303,736,871,1175,1475,1544,1913,2448])
#distance_array = np.abs(mileposts - mileposts[:,np.newaxis])
#print(distance_array)#LA랑 oklahoma: 1577
#----------그리드 또는 네트워크 기반 거리 계산
#x,y = np.arange(5),np.arange(5)[:,np.newaxis]#arange를 써서 x에 해당하는범위, y에 해당하는 범위나타냄
#0,1,2,3,4가 나옴. 0~4까지 영향을 미치는 정도. 노드의 거리값구하는 메트릭스
#distance = np.sqrt(x**2+y**2)#(0,0) 과 (0,3)의 거리: x차이의 제곱+y차이의제곱에 루트씌운거
#print(distance)
#plt.pcolor(distance)
#plt.colorbar()
#plt.show()
#----------
#ogrid,mgrid로 matrix만들 수 있음.
#x,y = np.ogrid[0:5,0:5]
#print(x)
#print(y)
#distance = np.sqrt(x**2+y**2)
#print(distance)
#plt.pcolor(distance)
#plt.colorbar()
#plt.show()
#x,y = np.mgrid[0:5,0:5]
#print(x)
#print(y)
#----------
#a = np.array([[1,2,3],[4,5,6]])
#print(a.ravel())#[1 2 3 4 5 6]
#print(a.T)#[[1 4][2 5][3 6]]
#print(a.T.ravel())#[1 2 3 4 5 6]
#shape정보 바꿀 때는 개수가 고정되어야
#a.shape
#print(a)
#b = a.ravel()
#b = b.reshape((2,3))
#b.reshape((2,-1))
#---------Adding a dimension
z = np.array([1,2,3])
print(z[:,np.newaxis])#[[1]
#                       [2]
#                       [3]]
print(z[np.newaxis,:])#[[1 2 3]]

#-----
#a = np.arange(4)
#a.resize((8,))#파이썬에서는 대입을하면 복사가아니라 참조형태임.
#                #다른거에의해 참조되지 않으면resize가 가능
#                #그 뒤에는 다 0으로 채워짐.
#print(a)#[0 1 2 3 0 0 0 0]
#-----
#a = np.array([[4,3,5],[1,2,1]])
#b = np.sort(a,axis = 1)
#a.sort(axis=1)
#print(a)#[[3 4 5][1 1 2]]
#print(b)#[[3 4 5][1 1 2]]
#--------sorting된 index를 반환 argumentsort:원본내용은 내버려두고 정렬된 데이터만 원하면 argsort를 사용함. 
          #정렬된 index번호 사용가능
#a = np.array([4,3,1,2])
#j = np.argsort(a)
#print(a)#[4 3 1 2]
#print(j)#[2 3 1 0]#sorting with index
#j_max = np.argmax(a)#finding maxima
#j_min = np.argmin(a)#finding minima
#print(j_max)#0
#print(j_min)#2
#-------
#p = np.poly1d([3,2,-1])#근이 -1,1/3임.
#print(p(0))#-1
#print(p.roots)#[-1.    0.3333333]
#print(p.order)#2
#p = np.polynomial.Polynomial([-1,2,3])
#print(p)#poly([-1. 2. 3.])
#----------polyfit:x,y에 가장 fitting되는 3차식을 만들어줌.
#x = np.linspace(0,1,20)#0부터 1까지 20개의 점을 찍어줌.
#y = np.cos(x)+0.3*np.random.rand(20)
#p = np.poly1d(np.polyfit(x,y,3))
#t = np.linspace(0,1,200)
#plt.plot(x,y,'o',t,p(t),'-')
#plt.show()
#------------chebyshev방정식이용?
#x = np.linspace(-1,1,2000)
#y = np.cos(x)+0.3*np.random.rand(2000)
#p = np.polynomial.Chebyshev.fit(x,y,90)
#t = np.linspace(-1,1,200)
#plt.plot(x,y,'r.')
#plt.plot(t,p(t),'k-',lw=3)
#plt.show()
#-----------파일에 해당하는걸 불러와서 메트릭스를 할 수 잇음
#메트릭스를 파일에 넣어놓고 불러다 사용할 수 있음
#data= np.loadtxt('populations.txt')
#np.savetxt('pop2.txt',data)
#data2= np.loadtxt('pop2.txt')
#-----
img = plt.imread('bora.png')
print(img.shape,img.dtype)
print(img.shape)#<x사이즈,y사이즈,알파값(3이면 r,g,b라고 된거고 4이면 r,g,b,투명도가 들어간거)>
plt.imshow(img)
plt.show()
img1 = plt.imread
#그림에서 특정부분만 잘라낼거임




