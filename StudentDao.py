import sqlite3


class StudentDao(object):

    @staticmethod
    def createTableIfNotExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists student("
                       + "s_id integer primary key,"
                       + "s_name char(100),"
                       + "s_sex char(7))")
        conn.commit()
        conn.close()

    @staticmethod
    def dropTableIfExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("drop table if exists student")
        conn.commit()
        conn.close()

    @staticmethod
    def insertIntoTable(id, name, sex):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "insert or ignore into student(s_id, s_name, s_sex) values (?, ?, ?)", [id, name, sex])
        conn.commit()
        conn.close()

    @staticmethod
    def getAllStudents():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from student")
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values

    @staticmethod
    def searchStudentById(id):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from student where s_id = ?", [id])
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values

    @staticmethod
    def searchStudentByName(name):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from student where s_name = ?", [name])
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values


if __name__ == '__main__':
    # StudentDao.dropTableIfExists()
    StudentDao.createTableIfNotExists()
    StudentDao.insertIntoTable("2017234567", "小明", "male")
    StudentDao.getAllStudents()
    StudentDao.searchStudentById(2017234567)
    StudentDao.searchStudentByName("小明")
