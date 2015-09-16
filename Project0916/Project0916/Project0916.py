#파일 w+: 파일 일고 쓰기
#fileName = "greenjoa.txt"
#with open("fileName","w+")as myfile:
#    myfile.write("201311203 김지연\n")
#    myfile.write("201311203 이지연\n")
#    myfile.write("201311203 삼지연\n")
#    myfile.write("201311203 사지연\n")

#-------------------
#파일읽기: r
#fileName = "greenjoa.txt"
#with open("fileName","r")as myfile:
#    content = myfile.read()
#    print(content)
#------------------
#fileName = "greenjoa.txt"
#READ = "r"
#myFile = open(fileName,mode=READ)
#while True:
#    content = myFile.readline()
#    if not content:break
#    print(content)
#myFile.close()
#---------
#fileName = "friends.txt"
#with open(fileName,"r")as myfile:
#   for content in myfile:
#    print(content)
#------- Monica에 해당하는 대사만 추려서 파일로 별도로 만들기

#fileName = "friends.txt"
#fileName2 = "Monica.txt"
#with open(fileName,"r")as myfile, open(fileName2,"w") as monica:
#    for content in myfile:
#        (role, etc) = content.strip().split(":")#콜론을 기반으로 분할시켜줄거임.앞에 해당하는건 role에 저장, 뒤에 해당하는건 etc에 저장
#       #파일에 모니카의 대사만 Monica.txt로 저장하기
#        if(role =="Monica"):
#           print(etc)
#           monica.write(etc)
#           monica.writelines("\n")
  #------------
  
#fileName = "friends2.txt"
#fileName2 = "Monica.txt"
#with open(fileName,"r")as myfile, open(fileName2,"w") as monica:
#    for content in myfile:
#        (role, etc) = content.strip().split(":")#콜론을 기반으로 분할시켜줄거임.앞에 해당하는건 role에 저장, 뒤에 해당하는건 etc에 저장
#       #파일에 모니카의 대사만 Monica.txt로 저장하기
#        if(role =="Monica"):
#           print(etc)
#           monica.write(etc)
#           monica.writelines("\n")      
#-------
#print(help(str.split))
 
#----------
#fileName = "friends2.txt"
#fileName2 = "Monica.txt"
#with open(fileName,"r")as myfile, open(fileName2,"w") as monica:
#    for content in myfile:
#        (role, etc) = content.strip().split(":",1)#콜론을 기반으로 분할시켜줄거임.앞에 해당하는건 role에 저장, 뒤에 해당하는건 etc에 저장
#       #파일에 모니카의 대사만 Monica.txt로 저장하기
#        if(role =="Monica"):
#           print(etc)
#           monica.write(etc)
#           monica.writelines("\n")  
#-----------
##role에 해당하는걸 list에 저장하기
#fileName = "friends2.txt"
#fileName2 = "Monica.txt"
#roles = []
#with open(fileName,"r")as myfile, open(fileName2,"w") as monica:
#    for content in myfile:
#       (role, etc) = content.strip().split(":",1)#콜론을 기반으로 분할시켜줄거임.앞에 해당하는건 role에 저장, 뒤에 해당하는건 etc에 저장
#       roles.append(role)
#print(roles)

#------------
#우리가 사용하고 있었던 list를 파일에 그대로 저장했다가 파일에서 읽으면 list로 읽어내는거
#이거 하려면 pickle을 이용해야
import pickle
fileName = "friends2.txt"
fileName2 = "Monica.txt"
roles = []
with open(fileName,"r")as myfile, open(fileName2,"wb+") as monica:#피클에 해당하는게 binary에 해당함
    for content in myfile:
       (role, etc) = content.strip().split(":",1)#콜론을 기반으로 분할시켜줄거임.앞에 해당하는건 role에 저장, 뒤에 해당하는건 etc에 저장
       roles.append(role)
    pickle.dump(roles,monica)#monica에 저장 이제 이걸 읽을 예정이니 w+  을 해줌
with open(fileName2,"rb") as monica:#rb로 함   
    result= pickle.load(monica)
print(result)