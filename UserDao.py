
import sqlite3
import hashlib

'''
m2 = hashlib.md5()
m2.update(src)
print m2.hexdigest()
'''


class UserDao(object):

    @staticmethod
    def createTable():
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists user("
                       + "username char(20),"
                       + "password char(20))")
        conn.commit()
        conn.close()

    @staticmethod
    def dropTable():
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute("drop table user")
        conn.commit()
        conn.close()

    @staticmethod
    def insertIntoTable(usr, pw):
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute(
            "insert or ignore into user(username, password) values (?, ?)", (usr, pw))
        conn.commit()
        conn.close()

    @staticmethod
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
    UserDao.createTable()
