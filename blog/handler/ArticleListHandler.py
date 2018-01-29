# coding:utf8

# 为了解决markdown编码错误问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from markdown import markdown
from handler.BaseHandler import BaseHandler

class ArticleListHandler(BaseHandler):
    '''
    文章列表
    '''
    def get(self):
        articlelist_content = open("md/articlelist/articlelist.md",'r').read()
        articlelist_content = markdown(articlelist_content)
        self.render("../page/front/articlelist.html",articlelist = articlelist_content)