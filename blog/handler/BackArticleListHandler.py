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


class BackArticleListHandler(BackBaseHandler):
    '''
    处理文章管理链接，只要显示文章列表即可
    '''
    @tornado.web.authenticated
    def get(self):
        filelist = os.listdir(unicode(home_dir + 'md/article', 'utf-8'))
        articlelist = ''
        for file in filelist:
            articlelist += '<a href="{1}/article?article_name={0}">{0}</a><br>'.format(file[:-3], back_dir)
        self.render("../page/back/articlelist.html", articlelist=articlelist, back_dir=back_dir)