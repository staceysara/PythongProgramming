from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin
#import webbrowser

#html_doc= """
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title"><b>The Dormouse's story</b></p>
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#"""
#soup = BeautifulSoup(html_doc,"html.parser")#뒤에는 파서정보가 들어가야.두번째에 넣어주지 않으면 기본적으로 html파서가 들어감.
#print(soup.prettify())#태그의 형식으로 이쁘게 출력해줘
#print(soup.a.prettify())
#print(soup.p['class'])
#print(soup('a'))
#print(soup('a',{'class':'sister'}))
#print(soup('p',{'class':'title'}))
#print(soup('a')[0].parent)
#print(soup('a')[0].parent.name)#p출력
#print(soup('a')[0].contents)#Elsie
#print(soup.find('p'))
#print(soup.find('a')['href'])#h ttp://example.com/elsie
#print(soup.find_all(id = 'link3'))#id가 link3인걸 찾음
#print(soup.find_all('p'))
#print(soup.find_all(class_='sister'))#class가 sister인걸 찾아줌. _가 들어가는거에 주의
#-----------------------
#url="http://comic.naver.com/webtoon/list.nhn?titleId=20853"
#data= urlopen(url)
#soup = BeautifulSoup(data,'html.parser')
#cartoons = soup.find_all('td',{'class':'title'})
#for i in range(len(cartoons)):
#    title = cartoons[i].find('a').string#a태그에 해당하는내용이랑
#    ref = cartoons[i].find('a')['href']#a태그에 해당하는 값을 찾음
#    tempurl = urljoin(url,ref)
#    print(title," ",tempurl)
#webbrowser.open_new(tempurl)
#----------웹 크롤링: 필요한거 가져오는거.사이트주소를 따라가서 그 주소를 따라가서 또다른 주소를 파싱해야 함.
class crawler:
    def crawl(self,pages,depth=2):
        for i in range(depth):
            newpage = set()
            for page in pages:
                try:
                    c = urlopen(page)
                except:
                    print("Could not open %s" %page)
                    continue
                soup = BeautifulSoup(c.read(),from_encoding="utf-8")
                print('Found%s'%page)
                links = soup('a')
                for link in links:
                    if('href' in dict(link.attrs)):
                        url = urljoin(page,link['href'])
                        if url.find("'")!=-1: continue
                        url = url.split("#")[0]
                        if url[0:4]=='http':
                            newpage.add(url)
                    pages = newpage
              
pagelist=['www.naver.com']
crawler = crawler()
crawler.crawl(pagelist)