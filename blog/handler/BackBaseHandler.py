# coding:utf8

from handler.BaseHandler import BaseHandler
from conf.conf import auth_cookie

class BackBaseHandler(BaseHandler):
    '''
    添加cookie，控制访问
    '''
    def get_current_user(self):
        return self.get_secure_cookie(auth_cookie)