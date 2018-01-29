# coding:utf8

# 为了解决markdown编码错误问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from markdown import markdown
from handler.BaseHandler import BaseHandler


class IndexHandler(BaseHandler):
    '''
    主页，就是简介
    '''
    def get(self):
        introduce_content = open("md/introduce/introduce.md",'r').read()
        introduce_content = markdown(introduce_content)
        self.render("../page/front/introduce.html",introduce = introduce_content)