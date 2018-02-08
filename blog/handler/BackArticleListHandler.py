# coding:utf8

# 为了解决markdown编码错误问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
        # 直接读取此文件需要做些修改，不然点击会直接跳回前端显示文章内容页面
        articlelist_content = open(home_dir + "md/articlelist/articlelist.md", 'r').read().replace \
            ("(/article?article_name=", "(" + back_dir + "/article?article_name=")
        articlelist_content = markdown(articlelist_content)
        self.render("../page/back/articlelist.html", articlelist=articlelist_content, back_dir=back_dir)