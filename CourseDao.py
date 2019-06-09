import sqlite3


class CourseDao(object):

    @staticmethod
    def createTableIfNotExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists course("
                       + "c_id integer primary key,"
                       + "c_name char(100),"
                       + "department char(100))")
        conn.commit()
        conn.close()

    @staticmethod
    def dropTableIfExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("drop table if exists course")
        conn.commit()
        conn.close()

    @staticmethod
    def insertIntoTable(id, name, department):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "insert or ignore into course(c_id, c_name, department) values (?, ?, ?)", [id, name, department])
        conn.commit()
        conn.close()

    @staticmethod
    def getAllCourses():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from course")
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values

    @staticmethod
    def searchCourseById(id):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from course where c_id = ?", [id])
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values

    @staticmethod
    def searchCourseByDepartment(department):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from course where department = ?", [department])
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values

    @staticmethod
    def searchCourseByName(name):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from course where c_name = ?", [name])
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values


if __name__ == '__main__':
    # CourseDao.dropTableIfExists()
    CourseDao.createTableIfNotExists()
    CourseDao.insertIntoTable(1, "数学分析", "数学学院")
    CourseDao.getAllCourses()
    CourseDao.searchCourseById(1)
    CourseDao.searchCourseByName("数学分析")
