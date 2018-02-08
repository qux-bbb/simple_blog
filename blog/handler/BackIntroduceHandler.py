# coding:utf8

# 为了解决markdown编码错误问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web
from BackBaseHandler import BackBaseHandler
from conf.conf import home_dir, back_dir


class BackIntroduceHandler(BackBaseHandler):
    '''
    负责修改保存简介
    '''
    @tornado.web.authenticated
    def get(self):
        introduce_content = open(home_dir + "md/introduce/introduce.md", 'r').read()
        self.render("../page/back/introduce.html", introduce=introduce_content, back_dir=back_dir, info_message="")


    @tornado.web.authenticated
    def post(self):
        info_message = "<br/><br/><p style='color:green;'>保存成功</p>"
        # 修改并保存简介
        introduce_content = self.get_argument("introduce", None)
        open(home_dir + "md/introduce/introduce.md", 'w').write(introduce_content)

        introduce_content = open(home_dir + "md/introduce/introduce.md", 'r').read()
        self.render("../page/back/introduce.html", introduce=introduce_content, back_dir=back_dir,
                    info_message=info_message)

