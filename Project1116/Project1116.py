from flask import Flask, redirect, url_for
app =Flask(__name__)#플라스크 객체를 구성. 괄호안에 패키지이름이나 모듈이름이 들어감.
@app.route('/')#앱이 하나 만들어짐.그 앱에 해당하는거 갖고 web프로그래밍 하려고 하면 브라우저를 통해서 접근함. 그때 주소 다음 루트를 방문했을 때 호출할 함수
                #웹에 root에 접속했을 때 hello world함수를 호출하라는거
                #파이썬에 flask에 가장 큰 특징은 몇줄 안되는코드로 돌릴 수 있다는거.. '/': 루트로 접속했을 때는 hello_world함수를 호출할거임. 
                #앱을 실행시키는거는 __main__(메인모드일때) 일때 앱을 런하겠다는거
                #기본포트: 5000
                #http://127.0.0.1:5000/ 을 누르면 hello world가 출력될 것
#def get_profile(username):
#    return 'profile:'+username
def hello_world():#root에서는 hello_world함수를 호출할 것.
    #return 'Hello World!'
    #url_for: 특정한 함수를 호출했을 때 경로를 만들어주는 함수?
    return redirect(url_for('login'))#/login경로를 만들어주고/login으로 경로가 바뀌고 login()이 호출됨

@app.route('/login')#경로 하나 만듬.
def login():#뷰펑션 하나 만듬. login을 반환. 경로가 /login임. hello_world()를 호출했을 때 login을 호출하도록 redirect하기
    return 'login'

if __name__=='__main__':
    #app.run()#run할때 옵션지정할 수 있음. 디버그속성을 지정해줄 수 있음. 디폴트:false. true로 했을때는 에러 난 원인에 해당하는 리스트를 보여줌.
            #실제 서비스할 때 true로 설정하면 안될것.
            #배포하고나서도 true로 하고 하면 안됨
            #app의 host지정가능, port지정가능. 해당 ip의 해당 port로 지정가능
    #app.debug=True#소스 변경과 디버거 제공
    app.run(host='203.252.166.47')#이 컴터의 ip정보
