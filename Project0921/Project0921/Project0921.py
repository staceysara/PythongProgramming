#class Movie:
#    secret = "영구는 배꼽이 두 개다"
#    def _init_(self, name, value=0):
#        self.name = name
#        self.value = value
#        self.secret = name
#    def sum(self,a,b):
#       result = a+b
#       print("%s님 %s + %s = %s입니다"%(self.name,a,b,result))
    #---------
#class Movie:
#   title=""
#   director=""
#   def __init__(self, title, director):
#       self.title = title;
#       self.director = director;
#   def showInfo(self):
#       print(self.title+" " +self.director)

#movie1 = Movie("암살","최동훈","character1")
#Movie__init__(movie1,"암살","최동훈");
#movie2 = Movie("hi1","what1")
#Movie.character=0
#movie1.character="character1"
#print(movie1.showInfo)
#print(movie2.showInfo)
#--------------생성자, 소멸자 이용
#class Movie:
#    '''영화 클래스입니다'''
#    title="mission impossible"
#    director="steve sphilberg"
#    def __init__(self, title, director):
#        self.title = title
#        self.director = director
#        print(self.title+ "생성자 호출")
#    def __del__(self):
#        print(self.title+ "소멸자 호출")
#    def showInfo(self):
#        print(self.title+" " +self.director)
#m1 = Movie("베테랑1","류승완1");
#m2 = Movie("베테랑2","류승완2");
#m3 = Movie("베테랑3","류승완3");
#m4 = Movie("베테랑4","류승완4");
#print(type(m4))#m4에 해당하는 타입정보가 출력 Movie가 출력될 것
#m4  = m3 #대입연산수행. 파이썬은 참조형이니까 얕은복사가 됨. 같은 주소를 가리키는 형태가 됨.
#         #베테랑 4소멸자가 호출된다음 m4는 m3와 같은 걸 가리킴
#print(id(m4))#id: 구분하는 주소값
#print(id(m3))
#m4.showInfo()
#print(m1.title);
#print(m1.__doc__)
#---------------static메소드 이용
class Movie:
    '''영화 클래스입니다'''
    count = 0 
    title="mission impossible"
    director="steve sphilberg"
    def __init__(self, title, director):
        self.title = title
        self.director = director
       # self.count+=1;
        Movie.count+=1;
        print(self.title+ "생성자 호출")
    def __del__(self):
        print(self.title+ "소멸자 호출")
    def showInfo(self):
        print(self.title+" " +self.director)
    @staticmethod#굳이 함수 정의하고 staticmethod호출하지 않아도됨
    def showCount1(): #class정보가 들어오지 않음
        print(Movie.count)

    @classmethod#class에 해당하는 정보가 들어옴
    def showCount2(cls):#무슨정보인지 몰라도 됨.
        print(cls.count)


m1 = Movie("a","b");
m2 = Movie("c","d");
m3 = Movie("e","f");
m4 = Movie("g","h");
m5 = Movie("i","j");

Movie.showCount1()
Movie.showCount2()