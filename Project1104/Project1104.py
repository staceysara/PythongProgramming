import sqlite3
con = sqlite3.connect("test.db")
#memory에 db에 해당하는게 만들어짐빠른속도요하는 거 하고프면 memory에 잠시 만들어두면 됨
cur = con.cursor()
cur.execute('''select * from phonebook;''')
print(cur.fetchall())#db에 계속 insert했는데 commit을 안해서 빈 리스트가 나옴 db에 영구히 저장하라는걸 말 안함. 
##테이블 생성
#con.isolation_level = None
#sql = '''create table if not exists phonebook(name text,phoneNum text);'''
dropsql ='''drop table if exists phonebook;'''
cur.execute(dropsql)
sql = '''create table phonebook(name text,phoneNum text);'''
cur.execute(sql)
insertsql = '''insert into phonebook values('greenjoa1','010-1111-2222');'''
cur.execute(insertsql)
cur.execute('''select * from phonebook;''')
#for row in cur:
#    print(row)#('greenjoa1','010-1111-2222')
#    print(row[0])#greenjoa1
print(cur.fetchall()) 
name = 'greenjoa2'
phoneNumber='010-2222-2222'
insertsql = '''insert into phonebook values(?,?);'''

cur.execute(insertsql,(name,phoneNumber))
#다시 select를 해줘야함
cur.execute('''select * from phonebook;''')
print(cur.fetchall())
#?대신 부여한 이름 사용가능
name ='greenjoa3'
phoneNumber = '010-3333-3333'
insertsql = '''insert into phonebook values(:inputName,:inputNum);'''
cur.execute(insertsql,{"inputNum":phoneNumber,"inputName":name})
cur.execute('''select * from phonebook;''')
print(cur.fetchall())
#리스트데이터를 한꺼번에 db에 넣을 수 있음
insertsql = '''insert into phonebook values(?,?);'''
datalist = (('greenjoa4','010-4444-4444'),('greenjoa5','010-5555-5555'))
cur.executemany(insertsql,datalist)
cur.execute('''select * from phonebook;''')
print(cur.fetchall())
#리턴같이 값반환하지만 함수를 종료하지 않는 yield
def dataGenerator():
    datalist = (('greenjoa6','010-6666-6666'),('greenjoa7','010-7777-7777'))
    for item in datalist:
        yield item
cur.executemany(insertsql,dataGenerator())
cur.execute('''select * from phonebook;''')
print(cur.fetchall())

#con.commit()
con.isolation_level = None

insertsql = '''insert into phonebook values('GREENJOA0','010-1111-2222');'''
cur.execute(insertsql)
cur.execute("select * from phoneBook order by name;")
cur.execute('''select * from phonebook;''')
print(cur.fetchall())

#정렬함수지정
def OrderFunc(str1,str2):
    s1 = str1.upper()
    s2 = str2.upper()
    return (s1>s2)-(s1<s2)
con.create_collation('myordering',OrderFunc)#이 함수를 기준으로 정렬할거임 myordering 은 OrderFunc을 기준으로 정렬할거임
cur.execute("select * from phoneBook order by name collate myordering;")#order by name: 문자열을 빼서 크기비교함(내부적으로 문자열끼리 빼는작업함)
print(cur.fetchall())

#핸폰번호만 넣음
cur.execute("insert into phonebook(phoneNum) values('010-9999-9999');")#이름이 None으로 출력됨
cur.execute('''select * from phonebook;''')
print(cur.fetchall())
#전체 튜플이 몇개인지
cur.execute("select count(*)from phoneBook;")
print(cur.fetchone()[0])#카운트에 해당하는 값 하나밖에 없기에 fetchone [0]
#name의 개수가 몇개인지(null이 아닌 값들만 count함)
cur.execute("select count(name)from phoneBook;")
print(cur.fetchone()[0])#앞에서 핸폰번호만 넣은 경우가 있기에 튜플개수보다 하나 적게 나옴
                        #name이 null이 아닌 값들만 count함
#이름과 나이만 갖고있는 user테이블
dropsql ='''drop table if exists user;'''
cur.execute(dropsql)
sql = '''create table user(name text,age INTEGER);'''
cur.execute(sql)
insertsql = '''insert into user values('user1','27');'''
cur.execute(insertsql)
insertsql = '''insert into user values('user2','23');'''
cur.execute(insertsql)
insertsql = '''insert into user values('user3','28');'''
cur.execute(insertsql)
cur.execute('''select * from user;''')
print(cur.fetchall())
cur.execute("select max(age) from user;")
print(cur.fetchone()[0])
cur.execute("select name,max(age) from user;")
print(cur.fetchone()[0])
#평균나이를 집계하고싶음:별도의 클래스를 만들어서 사용
#agerage클래스, sum, count
#집계함수쓸 떄 반드시 써야하는 함수가 step, finalize
#step: value값이 들어오는 걸 말함. 이 단계마다 뭘 하겠다.
#finalize:최종적으로 반환될 값
class Average:
    def __init__(self):
        self.sum=0
        self.cnt = 0
    def step(self,value):
        self.sum+=value
        self.cnt+=1
    def finalize(self):
        return self.sum/self.cnt

#create_aggregate에 sql구문에서 사용할 키워드(avg로 쓰겠다, step에 들어가는 인자 개수(지금은 value 하나), Average라는 클래스를 가지고)
con.create_aggregate("avg",1,Average)#DB에 등록
cur.execute("select avg(Age)from user;")
print(cur.fetchone()[0])