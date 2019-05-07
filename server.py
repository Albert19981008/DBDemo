from flask import Flask, render_template
from flask import request
from UserDao import UserDao
import sqlite3


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容并从数据库查询：
    if UserDao.search(request.form['username'], request.form['password']):
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')


@app.route('/registerpost', methods=['POST'])
def register():
    # 需要从request对象读取表单内容并从数据库查询：
    if UserDao.search(request.form['username'], request.form['password']):
        return '<h3>user has existed! register failed！</h3>'
    UserDao.insertIntoTable(request.form['username'], request.form['password'])
    return '<h3>register successful！</h3>'


if __name__ == '__main__':
    UserDao.createTable()
    app.run()
