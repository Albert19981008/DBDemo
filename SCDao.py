import sqlite3
from StudentDao import StudentDao
from CourseDao import CourseDao


class SCDao(object):

    @staticmethod
    def createTableIfNotExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists select_course("
                       + "c_id integer,"
                       + "s_id integer,"
                       + "primary key(c_id, s_id))")
        conn.commit()
        conn.close()

    @staticmethod
    def dropTableIfExists():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute("drop table if exists select_course")
        conn.commit()
        conn.close()

    @staticmethod
    def insertIntoTable(c_id, s_id):
        print("in! ", c_id, s_id)
        if len(CourseDao.searchCourseById(c_id)) <= 0 or len(StudentDao.searchStudentById(s_id)) <= 0:
            return
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "insert or ignore into select_course(c_id, s_id) values (?, ?)", [c_id, s_id])
        conn.commit()
        conn.close()

    @staticmethod
    def getAllSCs():
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "select * from select_course")
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values

    @staticmethod
    def searchSC(c_id, s_id, c_name, s_name):
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        query = "select c_name, s_name, course.c_id, student.s_id  from select_course, course, student"
        query += " where select_course.c_id = course.c_id "
        query += " and select_course.s_id = student.s_id"
        if c_id is not None and c_id != "":
            query += " and select_course.c_id = " + "\"" + str(c_id) + "\""
        if s_id is not None and s_id != "":
            query += " and select_course.s_id = " + "\"" + str(s_id) + "\""
        if c_name is not None and c_name != "":
            query += " and course.c_name = " + "\"" + str(c_name) + "\""
        if s_name is not None and s_name != "":
            query += " and student.s_name = " + "\"" + str(s_name) + "\""

        print(query)
        cursor.execute(query)
        values = cursor.fetchall()
        conn.commit()
        conn.close()
        print(values)
        return values

    @staticmethod
    def deleteById(c_id, s_id):
        print("delete", s_id, c_id)
        conn = sqlite3.connect('demo.db')
        cursor = conn.cursor()
        cursor.execute(
            "delete from select_course where c_id = ? and s_id = ?", [c_id, s_id])
        conn.commit()
        conn.close()


if __name__ == '__main__':
    # SCDao.dropTableIfExists()
    SCDao.createTableIfNotExists()
    SCDao.insertIntoTable(1, 2017234569)
    SCDao.insertIntoTable(2, 2017234569)
    SCDao.getAllSCs()
    SCDao.searchSC("", "", "", "")
