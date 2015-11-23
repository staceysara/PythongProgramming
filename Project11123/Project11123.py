import sqlite3 
from flask import Flask, request, session,g,redirect,url_for, abort,render_template,flash
from contextlib import closing


# configuration
DATABASE = 'flask.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

#with open('schema.sql')as f:
#    db.cursor().executescript(f.read())
#    db.commit()
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
         with app.open_resource('schema.sql', mode='r') as f:
             db.cursor().executescript(f.read())
         db.commit()

@app.before_request#request실행전에 호출
def before_request():
    g.db = connect_db()

@app.teardown_request#request의 마지막에 호출
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    print(entries)
    return render_template('show_entries.html', entries=entries)#db에 가지고온걸 변수에 다 담음다음 html에 뿌려줘야 할 것 그 html은 가지고온data로 랜더링된 html문서가 보여져야 브라우저에 뿌려지는거
                                #render_template모듈을 사용해서 show_entries.html을 사용할것. entries값에는 entries갑승ㄹ 넣어줄 것
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)  
 

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
        [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__=='__main__':#name이 main모듈로 실행될 때
    init_db()
    app.run()