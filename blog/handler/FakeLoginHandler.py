# coding:utf8

from handler.BaseHandler import BaseHandler
from conf.conf import site_key


class FakeLoginHandler(BaseHandler):
    '''
    fake login, a trap
    '''
    def get(self):
        self.render("../page/back/login.html",
                    info_message="", site_key=site_key)
    def post(self):
        username2 = self.get_argument("username", "Default_Name")
        if username2 == "admin":
            info_message = "<br/><br/><p style='color:red;'>密码错误！</p>"
        else:
            info_message = "<br/><br/><p style='color:red;'>用户名或密码错误！</p>"
        self.render("../page/back/login.html",
                    info_message=info_message, site_key=site_key)
