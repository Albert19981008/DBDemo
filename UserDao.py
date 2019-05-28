
import sqlite3
import hashlib


class UserDao(object):

    @staticmethod
    def createTableIfNotExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists user("
                       + "username char(100),"
                       + "passwordMd5 char(100))")
        conn.commit()
        conn.close()

    @staticmethod
    def dropTableIfExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("drop table if exists user")
        conn.commit()
        conn.close()

    @staticmethod
    def insertIntoTable(usr, pw):
        pwMd5 = hashlib.md5(pw.encode(encoding='UTF-8')).hexdigest()
        print(pwMd5)
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "insert or ignore into user(username, passwordMd5) values (?, ?)", (usr, pwMd5))
        conn.commit()
        conn.close()

    @staticmethod
    def searchAndReturnIfExist(usr, pw):
        pwMd5 = hashlib.md5(pw.encode(encoding='UTF-8')).hexdigest()
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from user where username = ? and passwordMd5 = ?", [usr, pwMd5])
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        if len(values) > 0:
            return True
        return False


if __name__ == '__main__':
    # UserDao.dropTableIfExists()
    UserDao.createTableIfNotExists()
