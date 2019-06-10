import sqlite3


class SloganDao(object):

    @staticmethod
    def createTableIfNotExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists poster("
                       + "p_name char(100) primary key,"
                       + "p_desc char(200))")
        conn.commit()
        conn.close()

    @staticmethod
    def dropTableIfExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("drop table if exists poster")
        conn.commit()
        conn.close()

    @staticmethod
    def insertIntoTable(name, desc):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "insert or ignore into poster(p_name, p_desc) values (?, ?)", [name, desc])
        conn.commit()
        conn.close()

    @staticmethod
    def getAllPosters():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from poster")
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values

    @staticmethod
    def searchPosterByName(name):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from poster where p_name = ?", [name])
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values


if __name__ == '__main__':
    SloganDao.dropTableIfExists()
    SloganDao.createTableIfNotExists()
    SloganDao.insertIntoTable("国民表率", "本国公民的好榜样")
    SloganDao.insertIntoTable("社会栋梁", "担负社会重任的人")
    SloganDao.insertIntoTable("追求极致", "完美主义 在更大的范围内寻找最优解")
    SloganDao.insertIntoTable("不设边界", "敢于创新 不怕麻烦 拥抱变化")
    SloganDao.getAllPosters()
