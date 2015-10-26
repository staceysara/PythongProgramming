import re
import os
import glob
import urllib.request
#--------------
#str ='''Window
#Unix
#Linux
#Solaris'''
##p = re.compile('^.+',re.M)#.:줄바꿈을 제외한 모든 문자, +:하나이상.결과: ['Window','Unix','Linux','Solaris']
#p = re.compile('^.+')#결과:['Window']
#print(p.findall(str))
#---------------
#str ='''Window
#Unix
#Linux
#Solaris'''
#p = re.compile('^.+',re.M)
#result = p.search(str)
#print(result)
#---------
#str ='''Window
#Unix
#Linux
#Solaris'''
#p = re.compile('^.+',re.S)
#result = p.search(str)
#print(result)
#-----------Group에 이름지정하기
#m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)","Malcolm Reynolds")
#print(m.group('first_name','last_name'))
#print(m.groups())#<'Malcol','Reynolds'>  <'Malcolm','Reynolds'>
#print(m.group('last_name'))#Reynolds
#------------Group에 디폴트값 주기(이거 실행안되었음)
#m=re.match(r"(\d+)W.?(Wd+)?", "24")
#print(m.groups())
#print(m.groups(0))
#----------
#m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)","Malcolm Reynolds")
#print(m.groupdict())#<'first_name':'Malcolm','last_name':'Reynolds'>
#-----------------
#p = re.compile(".+:")#콜론 앞에 하나이상의 아무거나 올 수 있음
#m = p.search("http://google.com")
#print(m.group())#http:
#-------콜론전에(콜론은 포함하지 않겠다)
#p = re.compile(".+(?=:)")
#m = p.search("http://google.com")
#print(m.group())#http
#-------현재디렉토리를 C디렉토리로 옮기기
#os.chdir("C:/")
#print(os.curdir)
##현재디렉토리에 있는 파일 찾아오기
#print(glob.glob('*'))
##bat나 exe로 끝나는건 안나옴
#p = re.compile('.*[.](?!bat$|exe$).*$')
#----------
p = re.compile("(?<=abc)def")
m = p.search("abcdef")
print(m.group())#def만 반환됨
#----------
m = re.search('(?<=-)\w+','spam-egg')
print(m.group())#egg만 반환됨
#---------
#email = "tony@tiremove_thisger.net"
#m = re.search("remove_this",email)
#result = email[:m.start()]+email[m.end():]#end:내가 찾고자하는문자열의 바로 뒤에거의 인덱스번호를 뜻함
#print(result)#tony@tiger.net
#----------
#def displaymatch(match):
#    if match is None:
#        return None
#    return '<Match: %r,groups=%r>'%(match.group(),match.groups())

#valid = re.compile(r"^[a2-9tjqk]{5}$")#a2-9tjqk에서 5개가 이렇게 끝나야함
#print(displaymatch(valid.match("akt5q")))
#---------
#text="""Ross: McFluff: 834.345.1254: 155 Elm Street
#Ronald: Heathmore: 892.345.3428 436: Finley Avenue
#Frank: Burger: 925.541.7625 662: South Dogwood Way
#Heather: Albrecht: 548.326.4584 919 Park Place"""
##entry에 있는거중에서 콜론을 기준으로 4개에 해당하는걸로 구분을 함.
##first이름, last이름, 전화번호, 주소 로 ...
#entries = re.split("\n",text)
#result = [re.split(":?",entry,4)for entry in entries]
#print(result)
#-----------
#with urllib.request.urlopen('http://www.naver.com')as f:
#    #print(f.read())
#    m=re.search("<title>",f)
#    value =urllib.request.urlopen(url).read()
#    par='<title>(.+?)</title>'
#    result = re.findall(par,str(value))
#    print(result)
#    #print(f.read(300))#300byte
#   # print(f.read(300).decode("utf-8"))#encoding mode utf-8
url ="http://www.naver.com"
value = urllib.request.urlopen(url).read()
par='<title>(.+?)</title>'
result = re.findall(par,str(value))
print(result)















