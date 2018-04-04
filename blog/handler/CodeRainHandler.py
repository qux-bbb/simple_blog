# coding:utf8

from handler.BaseHandler import BaseHandler
from conf.conf import site_key


class CodeRainHandler(BaseHandler):
    '''
    CodeRain egg
    '''
    def get(self):
        self.render("../page/front/code_rain.html", site_key=site_key)