# coding:utf8

from BackBaseHandler import BackBaseHandler
from conf.conf import login_open, salt, username, auth_cookie, home_dir, back_dir, site_key, secret_key
from hashlib import sha256
import requests


class LoginHandler(BackBaseHandler):
    '''
    后台登陆
    '''
    def get(self):
        if login_open == False:
            self.redirect("/")
        else:
            self.render("../page/back/login.html",
                        info_message="", site_key=site_key)
    def post(self):
        if login_open == False:
            self.redirect("/")
        else:
            # coinhive验证码
            coinhive_captcha_token = self.get_argument(
                "coinhive-captcha-token", "Coinhive_Captcha_Token")
            post_data = {"secret":secret_key, "token":coinhive_captcha_token, "hashes":1024}
            captcha_res = requests.post(
                "https://api.coinhive.com/token/verify", data=post_data)

            if '{"success":false' in captcha_res.content:
                info_message = "<br/><br/><p style='color:red;'>验证码出错，请重试！</p>"
                self.render("../page/back/login.html",
                            info_message=captcha_res.content + coinhive_captcha_token, site_key=site_key)
            else:
                username2 = self.get_argument("username", "Default_Name")
                password2 = self.get_argument("password", "Default_Pass")

                enc_password = open(home_dir + "conf/enc_password", 'r').read()

                enc_password2 = sha256(salt + username2 + password2).hexdigest()

                if username2 == username and enc_password2 == enc_password:
                    self.set_secure_cookie(auth_cookie, username2, expires_days=None)
                    self.redirect(back_dir)
                else:
                    info_message = "<br/><br/><p style='color:red;'>用户名或密码错误！</p>"
                    self.render("../page/back/login.html",
                                info_message=info_message, site_key=site_key)
