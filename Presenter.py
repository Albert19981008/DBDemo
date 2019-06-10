from flask import render_template
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
        return render_template('main.html', posters=Presenter.getDetailPosters(name))

    @staticmethod
    def getDetailPosters(name):
        res = []
        posters = SloganDao.searchPosterByName(name)
        for poster in posters:
            res.append(poster[0])
        return res
