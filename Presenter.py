from flask import render_template, request
from SloganDao import SloganDao
from StudentDao import StudentDao


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

        return Presenter.getMain()

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
