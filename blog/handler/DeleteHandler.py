# coding:utf8

# 为了解决markdown编码错误问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import tornado.web
from markdown import markdown
from BackBaseHandler import BackBaseHandler
from BaseHandler import home_dir
from conf.conf import back_dir

class DeleteHandler(BackBaseHandler):
    '''
    删除文章
    '''
    @tornado.web.authenticated
    def get(self):
        info_message = ""
        if (self.get_argument('article_name', None)):
            article_name = self.get_argument('article_name')

            # 删除文件
            os.remove("md/article/" + article_name + ".md")
            info_message += "<br/><br/><p style='color:green;'>" + article_name + " 已删除</p>"

        filelist = os.listdir(unicode(home_dir + 'md/article', 'utf-8'))
        articlelist = ''
        for file in filelist:
            articlelist += '<a href="{1}/delete?article_name={0}">{0}</a><br>'.format(file[:-3], back_dir)
        self.render("../page/back/delete.html", articlelist = articlelist, back_dir = back_dir, info_message = info_message)
