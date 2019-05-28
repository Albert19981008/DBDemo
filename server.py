from flask import Flask, render_template
from flask import request
from UserDao import UserDao
import sqlite3


app = Flask(__name__)
hasLogin = False


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/signin', methods=['POST'])
def signin():
    # 读取表单内容并从数据库查询：
    if UserDao.search(request.form['username'], request.form['password']):
        hasLogin = True
        return render_template('main.html')
    return render_template('autojump.html', content=' 2;URL=/ ', text="登录失败！2秒之后将自动跳转回登录页")


@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')


@app.route('/registerpost', methods=['POST'])
def register():
    # 读取表单内容并从数据库查询：
    if UserDao.search(request.form['username'], request.form['password']):
        return render_template('autojump.html', content=' 2;URL=/register', text="登录失败！2秒之后将自动跳转回注册页")
    UserDao.insertIntoTable(request.form['username'], request.form['password'])
    hasLogin = True
    return render_template('autojump.html', content=' 1;URL=/main', text="登录成功！1秒之后将自动登录")


@app.route('/main', methods=['get', 'POST'])
def goMain():
    if hasLogin == True:
        return render_template('main.html')
    else:
        return render_template('autojump.html', content=' 2;URL=/ ', text="登录失败！2秒之后将自动跳转回登录页")


if __name__ == '__main__':
    # UserDao.dropTableIfExists()
    UserDao.createTableIfNotExists()
    app.run()
