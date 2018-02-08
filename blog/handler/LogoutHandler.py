# coding:utf8

import tornado.web
from BackBaseHandler import BackBaseHandler
from conf.conf import auth_cookie


class LogoutHandler(BackBaseHandler):
    '''
    退出登录
    '''
    @tornado.web.authenticated
    def get(self):
        self.clear_cookie(auth_cookie)
        self.redirect("/")