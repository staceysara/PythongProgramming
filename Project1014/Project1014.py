import re
#pattern= re.compile("d")
#result = pattern.search("dog")
#print(result)
#result = pattern.search("dog",1)
#print(result)
#----------
#str = '''sample1.
# sample2.
# sample3.'''#이걸 하나씩 끊기 문장으로 되어있음
#p = re.compile('^.*',re.S)#multiline에 해당하는거다 받아옴. 처음부터
##p = re.compile('^.$',re.S)
#result = p.search(str)
#print(result.group())
#------------
#pattern = re.compile("o[gh]")
#result = pattern.fullmatch("dog")
#print(result)
#result = pattern.fullmatch("ogre")
#print(result)
#result = pattern.fullmatch("doggie",1,3)#인덱스번호는 0부터 시작. 1,3이면 3은 안들어가는거임. 
#print(result)
#------------split
#pattern = re.compile("\W+")
#result = pattern.split('words, words, words.')
#print(result)
#result = pattern.split('words, words, words.',1)
#print(result)

#pattern = re.compile("x*")
#result = pattern.split('axbc')
#print(result)

#result = re.sub(r'\w',"",'a:b:c,d.')
#print(result)
#------------
#str = '<a href="index.html">HERE</a><font size="10">'
#result = re.search(r'href="(.*?)">',str)
#print(result.group(1))
#포맷이 주민번호포맷에 맞는지 체크하고 맞으면 앞에부분, 뒤에부분 잘라내기
str = "123456-1234567/"
#p = re.fullmatch(s'(\d{6})-(\d{7})')#그룹으로 만듬
pattern = re.compile('(\d{6})-(\d{7})')
result = pattern.fullmatch(str)
print(result)

