import sqlite3 as sqlite
from werkzeug import check_password_hash, generate_password_hash
#initdb로 생성하는거
def init_db():
    db = sqlite.connect("test.db")
    with open('schema.sql')as f:
        db.cursor().executescript(f.read())#executescript로 파일에 있는 내용을 수행함
        db.commit()#db에 쓰는거
   #계속실행하면 지워졌다 새로만들어지고 할거임
#디비객체를 계속 만들어야 하니 함수를 만들어 디비객체를 가져오도록
def get_db():
    db = sqlite.connect("test.db")
    db.isolation_level = None
    return db

def register():
    #3개의 값 입력받아 db에 넣기
    #init_db()
    
    
    print("**** 회원 가입 ****\n")
    print("user id:",end="")
    userid = input()
    db = get_db()
    #db.isolation_level = None
    cur = db.cursor()
    cur.execute("select * from user")
   
    if cur.fetchone() != None:
        print("아이디가 존재합니다")
        return
    else:
    #필드명 지정해주면 table원소개수만큼 꽉안차게 해도 됨
   
        print("user name:",end="")
        username = input()
        print("user password:",end="")
        userpasswd = input()
        sql = "insert into user(userid, username,userpw) values(?,?,?)"
        #cur.execute(sql,[userid,username,userpasswd]) 
        cur.execute(sql,[userid,username,userpasswd],generate_password_hash(userpasswd)) 
        cur.execute("select * from user")
        print(cur.fetchall())
        db.commit()  
        #print(cur.fetchall())
        db.close()
    #cur.execute("select * from user where userid=?",[userid])
    #print(cur.fetchall())    
    #registering테이블만듬

    



init_db()
while(1):
    register()



def login():
    #질의문던져서 아이디확인
    print("**** 로그인 ****\n")
    print("user id:",end="")
    userid = input()
    print("user password:",end="")
    userpasswd = input()
    db = get_db()
    #db.isolation_level = None
    cur = db.cursor()
    cur.execute("select * from user where userid=?",[userid])
    temp = cur.fetchone()
    if(temp==None):
        print("아이디가 존재함")
        return
    elif check_password_hash(temp[3],userpasswd):#temp[3]이 패스워드가ㅣ 있는거임
        print("로그인 성공")
        return
    else:
        print("비밀번호 체크요함")
        return
    db.close()

