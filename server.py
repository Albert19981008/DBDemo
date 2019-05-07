from flask import Flask
from flask import request
import sqlite3


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容并从数据库查询：
    if search(request.form['username'], request.form['password']):
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/register', methods=['GET'])
def register_form():
    return '''<form action="/register" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">register</button></p>
              </form>'''


@app.route('/register', methods=['POST'])
def register():
    # 需要从request对象读取表单内容并从数据库查询：
    if search(request.form['username'], request.form['password']):
        return '<h3>user has existed! register failed！</h3>'
    insertIntoTable(request.form['username'], request.form['password'])
    return '<h3>register successful！</h3>'


def createTable():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("create table user("
                   + "username char(20),"
                   + "password char(20))")
    conn.commit()
    conn.close()


def dropTable():
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("drop table user")
    conn.commit()
    conn.close()


def insertIntoTable(usr, pw):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute(
        "insert or ignore into user(username, password) values (?, ?)", (usr, pw))
    conn.commit()
    conn.close()


def search(usr, pw):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute(
        "select * from user where username = ? and password = ?", [usr, pw])
    values = cursor.fetchall()
    conn.commit()
    conn.close()
    if len(values) > 0:
        return True
    return False


if __name__ == '__main__':
    # dropTable()
    createTable()
    #insertIntoTable("admin", "password")
    #search("admin", "password")
    app.run()
