# coding:utf8

from handler.BaseHandler import BaseHandler

class CodeRainHandler(BaseHandler):
    '''
    CodeRain egg
    '''
    def get(self):
        self.render("../page/front/code_rain.html")