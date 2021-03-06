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

    @staticmethod
    def searchCourse(name, id, department):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        query = "select * from course"
        hasWhere = False
        if name is not None and name != "":
            if hasWhere:
                query += " and c_name = " + "\"" + str(name) + "\""
            else:
                query += " where c_name = " + "\"" + str(name) + "\""
                hasWhere = True
        if id is not None and id != "":
            if hasWhere:
                query += " and c_id = " + str(id)
            else:
                query += " where c_id = " + str(id)
                hasWhere = True
        if department is not None and department != "":
            if hasWhere:
                query += " and department = " + "\"" + str(department) + "\""
            else:
                query += " where department = " + "\"" + str(department) + "\""
                hasWhere = True

        print(query)
        cursor.execute(query)
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values

    @staticmethod
    def deleteById(id):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "delete from course where c_id = ?", [id])
        conn.commit()
        conn.close()


if __name__ == '__main__':
    # CourseDao.dropTableIfExists()
    CourseDao.createTableIfNotExists()
    CourseDao.insertIntoTable(1, "数学分析", "数学学院")
    CourseDao.insertIntoTable(2, "程序设计", "信息学院")
    CourseDao.insertIntoTable(3, "计算机网络", "信息学院")
    CourseDao.getAllCourses()
    CourseDao.searchCourse("", "", "")
    CourseDao.searchCourseByName("数学分析")
