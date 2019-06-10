from flask import render_template, request
from SloganDao import SloganDao


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
    def getManagement(type, opt):
        if type == 'slogan':
            print(opt)
            return Presenter.getSloganManagement(opt)


    @staticmethod
    def getSloganManagement(opt):
        if opt is None:
            return render_template('sloganManagement.html', posters=Presenter.getMainPosters())
        if opt == 'add':
            name = request.form['name']
            desc = request.form['desc']
            SloganDao.insertIntoTable(name, desc)
            return Presenter.getMain()

        if opt == 'delete':
            name = request.form['name']
            SloganDao.deletePosterByName(name)
            return Presenter.getMain()


