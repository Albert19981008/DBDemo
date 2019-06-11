from flask import render_template, request
from SloganDao import SloganDao
from StudentDao import StudentDao
from CourseDao import CourseDao
from SCDao import SCDao


class Presenter(object):

    @staticmethod
    def getMain():
        return render_template('main.html', posters=Presenter.getMainPosters())

    @staticmethod
    def getMainPosters():
        res = []
        posters = SloganDao.getAllPosters()
        for poster in posters:
            res.append(poster[0])
        return res

    @staticmethod
    def getDetailPoster(name):
        desc = Presenter.getDetailPosterDesc(name)
        if desc is not None:
            return render_template('sloganDetail.html', name=name, desc=desc)
        return Presenter.getMain()

    @staticmethod
    def getDetailPosterDesc(name):
        posters = SloganDao.searchPosterByName(name)
        for poster in posters:
            return poster[1]
        return None

    @staticmethod
    def getSearch(type, opt):
        if type == 'slogan':
            return Presenter.getSloganSearch(opt)
        if type == 'student':
            return Presenter.getStudentSearch(opt)
        if type == 'course':
            return Presenter.getCourseSearch(opt)
        if type == 'sc':
            return Presenter.getScSearch(opt)

        return Presenter.getMain()

    @staticmethod
    def getScSearch(opt):
        if opt is None:
            return render_template('scSearch.html', posters=Presenter.getMainPosters())

        if opt == 'search':
            s_name = request.form['s_name']
            s_id = request.form['s_id']
            c_name = request.form['c_name']
            c_id = request.form['c_id']
            scs = SCDao.searchSC(c_id, s_id, c_name, s_name)
            lis = []
            i = 1
            for sc in scs:
                lis.append({"c_name": sc[0], 's_name': sc[1], 'c_id': sc[2], 's_id': sc[3]})
                i += 1
            return render_template('scSearch.html', posters=Presenter.getMainPosters(), scs=lis)

    @staticmethod
    def getStudentSearch(opt):
        if opt is None:
            return render_template('studentSearch.html', posters=Presenter.getMainPosters())

        if opt == 'search':
            name = request.form['name']
            id = request.form['id']
            sex = request.form['sex']
            students = StudentDao.searchStudent(name, id, sex)
            lis = []
            i = 1
            for student in students:
                lis.append({"id": student[0], 'name': student[1], 'sex': student[2]})
                i += 1
            return render_template('studentSearch.html', posters=Presenter.getMainPosters(), students=lis)

    @staticmethod
    def getCourseSearch(opt):
        if opt is None:
            return render_template('courseSearch.html', posters=Presenter.getMainPosters())

        if opt == 'search':
            name = request.form['name']
            id = request.form['id']
            department = request.form['department']
            courses = CourseDao.searchCourse(name, id, department)
            lis = []
            i = 1
            for course in courses:
                lis.append({"id": course[0], 'name': course[1], 'department': course[2]})
                i += 1
            return render_template('courseSearch.html', posters=Presenter.getMainPosters(), courses=lis)

    @staticmethod
    def getSloganSearch(opt):
        if opt is None:
            return render_template('sloganSearch.html', posters=Presenter.getMainPosters())

        if opt == 'search':
            name = request.form['name']
            slogans = None
            if name is None or name == "":
                slogans = SloganDao.getAllPosters()
            else:
                slogans = SloganDao.searchPosterByName(name)
            lis = []
            i = 1
            for slogan in slogans:
                lis.append({"id": i, 'name': slogan[0], 'desc': slogan[1]})
                i += 1
            return render_template('sloganSearch.html', posters=Presenter.getMainPosters(), slogans=lis)

    @staticmethod
    def getManagement(type, opt):
        if type == 'slogan':
            return Presenter.getSloganManagement(opt)
        if type == 'student':
            return Presenter.getStudentManagement(opt)
        if type == 'course':
            return Presenter.getCourseManagement(opt)
        if type == 'sc':
            return Presenter.getScManagement(opt)

        return Presenter.getMain()

    @staticmethod
    def getScManagement(opt):
        if opt is None:
            if request.args.get("prev") == "delete":
                return render_template('scManagement.html', posters=Presenter.getMainPosters(), delete=True)
            else:
                return render_template('scManagement.html', posters=Presenter.getMainPosters(), add=True)

        if opt == 'add':
            c_id = request.form['c_id']
            s_id = request.form['s_id']
            SCDao.insertIntoTable(c_id, s_id)
            return Presenter.getMain()

        if opt == 'delete':
            c_id = request.form['c_id']
            s_id = request.form['s_id']
            SCDao.deleteById(c_id, s_id)
            return Presenter.getMain()

    @staticmethod
    def getStudentManagement(opt):
        if opt is None:
            if request.args.get("prev") == "delete":
                return render_template('studentManagement.html', posters=Presenter.getMainPosters(), delete=True)
            else:
                return render_template('studentManagement.html', posters=Presenter.getMainPosters(), add=True)

        if opt == 'add':
            name = request.form['name']
            id = request.form['id']
            sex = request.form['sex']
            StudentDao.insertIntoTable(id, name, sex)
            return Presenter.getMain()

        if opt == 'delete':
            id = request.form['id']
            StudentDao.deleteStudentById(id)
            return Presenter.getMain()

    @staticmethod
    def getCourseManagement(opt):
        if opt is None:
            if request.args.get("prev") == "delete":
                return render_template('courseManagement.html', posters=Presenter.getMainPosters(), delete=True)
            else:
                return render_template('courseManagement.html', posters=Presenter.getMainPosters(), add=True)

        if opt == 'add':
            name = request.form['name']
            id = request.form['id']
            department = request.form['department']
            CourseDao.insertIntoTable(id, name, department)
            return Presenter.getMain()

        if opt == 'delete':
            id = request.form['id']
            CourseDao.deleteById(id)
            return Presenter.getMain()

    @staticmethod
    def getSloganManagement(opt):
        if opt is None:
            if request.args.get("prev") == "delete":
                return render_template('sloganManagement.html', posters=Presenter.getMainPosters(), delete=True)
            else:
                return render_template('sloganManagement.html', posters=Presenter.getMainPosters(), add=True)

        if opt == 'add':
            name = request.form['name']
            desc = request.form['desc']
            SloganDao.insertIntoTable(name, desc)
            return Presenter.getMain()

        if opt == 'delete':
            name = request.form['name']
            SloganDao.deletePosterByName(name)
            return Presenter.getMain()
