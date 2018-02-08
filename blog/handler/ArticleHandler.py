# coding:utf8


# 为了解决markdown编码错误问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from markdown import markdown
from handler.BaseHandler import BaseHandler
from conf.conf import home_dir


class ArticleHandler(BaseHandler):
    '''
    单个文章
    '''
    def get(self):
        article_name = self.get_argument('article_name')
        article_content = open(home_dir + "md/article/" + article_name + ".md" ,'r').read()
        article_content = markdown(article_content)
        self.render("../page/front/article.html",article_name = article_name, article_content = article_content)