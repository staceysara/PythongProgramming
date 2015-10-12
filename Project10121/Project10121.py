import glob
import os
import os.path
import tempfile
import time
import calendar
import random
import webbrowser
#os.chdir('C:/python34')
#print(glob.glob('*.exe'))
#print(glob.glob('?????.*'))
#print(glob.glob('./[0-9].*'))
#------------------
#디렉토리 안에는 또 다른 파일들이 있을 거임. 파일에 해당하는 리스트들을 트리형태로 출력해주는 함수
#ndir = nfile = 0
#def traverse(dir,depth):#depth만큼 반복해서 안으로 들어가는 형태. 디렉토리이면 다시호출하는거.
#                        #obj이 파일이면 basename만 출력해주는 거.
#    global ndir, nfile
#    for obj in glob.glob(dir+'/*'):
#        if depth == 0:
#            prefix='|--'
#        else:
#            prefix='|'+' '*depth+'|--'
#        if os.path.isdir(obj):
#            ndir+=1
#            print(prefix+os.path.basename(obj))
#            traverse(obj,depth+1)
#        elif os.path.isfile(obj):
#            nfile+=1
#            print(prefix+os.path.basename(obj))
#        else:
#            print(prefix+'unknown object:',obj)

#if __name__ =='__main__':
#    traverse('..',0)
#    print('\n',ndir,'directories','nfile','files')
#----------------tempfile
#with tempfile.TemporaryFile('w+',delete=False) as fp:
#    fp.write('Hello world!')
#    fp.seek(0)
#    data = fp.read()
#    print(os.path.exists(fp.name))#tempfile이 존재함. 
#    print(fp.name)
#    print(data)


#print(os.path.exists(fp.name))
#-----------------이거셤에나올듯
#t1 = time.time()#time객체를 만듬.
##time.sleep(10)
#print(time.time())
#print(t1)
#time1 = time.ctime(1234567)
#print("time.ctime(12345567)한 결과:(ctime은 입력된 초를 스트링 객체로 반환))",time1)
#t = time.strptime(time1)
#print(t)

#print(time.strftime("%B %dth %A %I:%M",time.localtime()))
#------------------
#print(calendar.weekday(1993,4,3))#0~6까지 반환. 월:0~일:6까지 
#print(calendar.calendar(2000))
#-----------------
#print(random.randrange(0,101,2))#0~100까지,2의 배수
#list = [32,43,545,12,235,345,36,456]
#print(random.choice(list))#입력 받은 리스트에서 무작위로 하나를 선택해 반환
#random.shuffle(list)#무작위로 섞어주는 함수
#print(list)
#print(random.sample(range(100),5))
##0~100까지에 해당하는 난수에서 10깨를 뽑아 한 번 섞고 그 중에서 하나 초이스하기
#--------------------
#red:3 blue:1 green:4 yellow:2 각 칼라마다 가중치가있음특정번호는 발생할 확률이 높도록
#이거에 해당하는 리스트에서 하나를 choice하고픔
#data = [('Red',3),('Blue',1),('Green',4),('Yellow',2)]
#datalist = []
#for val, cnt in data:
#    for i in range(cnt):
#        datalist.append(val)

#print(datalist)
#random.shuffle(datalist)
#print(random.choice(datalist))
##----------------가장 바깥에 그 안에.. 그 안에... 하는 순으로 for문을 작성하면 여러 개의for문이더라도 한줄로 해결할 수 있음
#weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)] 
#population = [val for val, cnt in weighted_choices for i in range(cnt)]
#print(population)
#------------
url = 'http://www.naver.com'
webbrowser.open_new_tab(url)
webbrowser.open_new(url)









