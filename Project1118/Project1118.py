from flask import Flask, render_template,url_for

app = Flask(__name__)
@app.route('/')
def hello():
    data=[dict(href="http://www.naver.com",caption="네이버"),dict(href="http://www.google.com",caption="구글")]
    return render_template('hello.html',items=data)
@app.route('/hello/')
def hello_world():
    return 'Hello World!'

#상속 등등 실습한거 더 있는데 안되었음
#이거 실습해보기(상속, 이름 보내기? 등)
#@app.route('hello/<name>')
#def hello(name=None):
#    return render_template('hello.html',name=name)
#----------
#@app.route('/data1/')
#def hello_world():
#    data={
#        'title':'Hello',
#        'name':'greenjoa'
#        }
#    return render_template('hello.html',**data)
if __name__ == '__main__':
    app.debug=True
    app.run()
    