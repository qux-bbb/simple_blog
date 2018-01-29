# coding:utf8

from BackBaseHandler import BackBaseHandler
from conf.conf import login_open, username, password, auth_cookie, back_dir

# 后台登陆
class LoginHandler(BackBaseHandler):
    def get(self):
        if login_open == False:
            self.redirect("/")
        else:
            self.render("../page/back/login.html", info_message = "")
    def post(self):
        if login_open == False:
            self.redirect("/")
        else:
            username2 = self.get_argument('username', 'Default_Name')
            password2 = self.get_argument('password', 'Default_Pass')

            if username2 == username and password2 == password:
                self.set_secure_cookie(auth_cookie, username2, expires_days=None)
                self.redirect(back_dir)
            else:
                info_message = "<br/><br/><p style='color:red;'>用户名或密码错误！</p>"
                self.render("../page/back/login.html", info_message = info_message)