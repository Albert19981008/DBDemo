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
        desc = Presenter.getDetailPosterDesc(name)
        return render_template('sloganDetail.html', name=name, desc=desc)

    @staticmethod
    def getDetailPosterDesc(name):
        posters = SloganDao.searchPosterByName(name)
        for poster in posters:
            return poster[1]
        return None
