from flask import Flask
from flask import render_template
from SloganDao import SloganDao


class Presenter(object):

    @staticmethod
    def getMain():
        return render_template('main.html', posters=Presenter.getPosterHtml())

    @staticmethod
    def getPosterHtml():
        res = []
        posters = SloganDao.getAllPosters()
        for poster in posters:
            res.append(poster[0])
        return res
