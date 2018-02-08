# coding:utf8

import tornado.web
from BackBaseHandler import BackBaseHandler
from conf.conf import auth_cookie, salt, username, home_dir, login_dir, back_dir
from hashlib import sha256


class ChangePassHandler(BackBaseHandler):
    '''
    修改密码
    '''
    @tornado.web.authenticated
    def get(self):
        self.render("../page/back/changepass.html", info_message="", back_dir=back_dir)

    @tornado.web.authenticated
    def post(self):
        info_message = ""
        oldpass = self.get_argument("oldpass", "Default_oldpass")
        newpass = self.get_argument("newpass", "Default_newpass")
        enc_oldpass = sha256(salt + username + oldpass).hexdigest()
        enc_password = open(home_dir + "conf/enc_password", 'r').read()
        if enc_oldpass == enc_password:
            enc_newpass = sha256(salt + username + newpass).hexdigest()
            if enc_newpass == enc_oldpass:
                info_message += "<br/><br/><p style='color:red;'>新密码不能与旧密码相同！</p>"
            else:
                open(home_dir + "conf/enc_password", 'w').write(enc_newpass)
                self.clear_cookie(auth_cookie)
                info_message += "<p style='color:green;'>密码修改成功，需要重新登陆，3秒后跳至登录页面</p>" \
                                "<script>setTimeout('javascript:location.href=\"" + login_dir + "\"', 3000);</script>"
        else:
            info_message += "<br/><br/><p style='color:red;'>旧密码错误！</p>"

        self.render("../page/back/changepass.html", info_message=info_message, back_dir=back_dir)
