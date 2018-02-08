# coding:utf8

import os

from handler.BaseHandler import BaseHandler
from conf.conf import home_dir


class ArticleListHandler(BaseHandler):
    '''
    文章列表
    '''
    def get(self):
        filelist = os.listdir(unicode(home_dir + 'md/article', 'utf-8'))
        articlelist = ''
        for file in filelist:
            articlelist += '<a href="/article?article_name={0}">{0}</a><br>'.format(file[:-3])
        self.render("../page/front/articlelist.html",articlelist = articlelist)