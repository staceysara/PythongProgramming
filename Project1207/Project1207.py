from matplotlib import pyplot as plt
import numpy as np
#plt.plot([1,2,3,4])#x축이 아니라 y축임. 값이 하나만잇는게 아니라 y축에 해당하는거. x축은 0부터 자동으로 벡터로...
#plt.show()
#-------
#plt.plot([1,2,3,4],[1,4,9,16],'o-')#앞에건 x축, 뒤에건 y축#선과 circle을 같이 줌
#plt.show()
#-----------
#plt.plot([1,2,3,4],[1,4,9,16],'ro')#o: circle marker r: color정보
#plt.show()
#---------------
#t일때t를 그릴거고, t일때 t의 제곱을, t일때 t의 세제곱을...
#figure에 각각 속성정보를 주고플 때
#t = np.arange(0.,5.,0.2)#x축이 0~5까지 0.2씩...
#plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
#plt.show()
#---------그래프에범례넣기
#plot에 해당하는 라벨정보를 주면 legend라는걸 주면 범례를 줄 수 있음.
#location 정보는 upper left하면 왼쪽 위에 위치함.
#보통 범례는 일반적인 위치는 upper right쪽에 많이있음
#np에 cos, sin이 있음.
#X = np.arange(0,1,0.1)
#C = np.cos(X)
#S = np.sin(X)
#plt.plot(X,C,color="blue",linewidth=2.5,linestyle="-",label="cosine")
#plt.plot(X,S,color="red",linewidth=2.5,linestyle="-",label="sine")
#plt.legend(loc='upper left')#범례가 왼쪽위에 있음.
#plt.show()
#-------------창을 윈도우에서 영역을 나눠서 그래프를 여러개 할 수 있음. 
#plt.figure(figsize=(8,6),dpi=80)#create a figure of size8ㅌ6 inches, 80 dots per inch
#plt.show()
#--------
#plt.subplot(1,1,1)#1bㅛ1에 한개만들기
#plt.show()
#-----

#def f(t): 
#    return np.exp(-t) * np.cos(2*np.pi*t) 
#t1 = np.arange(0.0, 5.0, 0.1) 
#t2 = np.arange(0.0, 5.0, 0.02)
#plt.figure(1) #Figure1에다 그려라
#plt.subplot(211) 
#plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#plt.subplot(212) 
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#plt.show()
#------------0,0에 해당하는건 좌측하단에 있음. 이 축을 중앙으로 옮기고 싶을때 spine을 씀
#ax = plt.gca()#gca: get current axis
#ax.spines['right'].set_color('none')#spine축의 오른쪽에 해당하는 컬러정보를 없애겠다.
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')#set tick position 을 bottom으로tick을 기준으로 옮겨짐
#ax.spines['bottom'].set_position(('data',0))#x축에 해당하는걸 bottom을 기준으로 spine에 해당하는걸 bottom의 0번째에
#                                            #bottom을 data의 0,0dp akwcna
#ax.yaxis.set_ticks_position('left')#y축에 해당하는 tick의 left에 해당하는게 tick의 0번째 데이타에...
#ax.spines['left'].set_position(('data',0))#x축에 해당하는걸 left을 기준으로
#                                           #left에 해당하는 걸 tick정보를 이용해 맞춤.
#                #bottom에 해당하는걸 data의 0부분에 넣고 
#                #x를 0만큼 옮긴거고 y도 0으로 옮김. 
#---------- Scatter
#n = 1024
#X = np.random.normal(0,1,n)
#Y = np.random.normal(0,1,n)
#T = np.arctan2(Y,X)

#plt.axes([0.025,0.025,0.95,0.95])
#plt.scatter(X,Y,s = 75,c = T,alpha = .5)

#plt.xlim(-1.5,1.5)
#plt.xticks(())
#plt.ylim(-1.5,1.5)
#plt.yticks(())
#plt.show()
#----------ㅡmeshgrid로 그리드정보 만들어냄. contourf로 그래프 그려줌
#등고선그릴때 함수 2개사용. 채워진 면 그릴때, 구분 선 그릴 때
#함수 2개를 갖는것으로 사용. contourf로 채워진 면, contour로 라인그리기  레이블정보는 clabel을 이용해
#def f(x,y):
#    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
#n=256
#x = np.linspace(-3,3,n)
#y = np.linspace(-3,3,n)
#X,Y = np.meshgrid(x,y)
#plt.axes([0.025,0.025,0.95,0.95])
#plt.contourf(X,Y,f(X,Y),8,alpha=.75,cmap = plt.cm.hot)#8개의 영역으로 나누어짐
#C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)
#plt.clabel(C,inline=1,fontsize=10)
#plt.show()
#----------보간법을 지정해서 만들어줄 수 있음. 여기서는 nearest를 이용한거임. 사용할 수 있는 보간법 종류가 많음
        #옆하고 색상을 smooth하게 나타냄
            #colormap: map종류에 칼라를 나타내는 패턴으로..cmap='bone' 인데 cmap='winter'로 해보기
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3 ) * np.exp(-x ** 2 - y ** 2)
n = 10
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3.0 * n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(Z, interpolation='nearest', cmap='winter', origin='upper')# cmap='bone'을 'winter'로 바꿔봄
plt.colorbar(shrink=.92)
plt.xticks(())
plt.yticks(())
plt.show()











