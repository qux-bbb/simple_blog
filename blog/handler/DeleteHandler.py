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

            # 修改文件列表
            listline = "[" + article_name + "](/article?article_name=" + article_name + ")  \n"
            articlelist_content = open(home_dir + "md/articlelist/articlelist.md" ,'r').read()
            open(home_dir + "md/articlelist/articlelist.md" ,'w').write(articlelist_content.replace(listline ,""))

            # 删除文件
            os.remove("md/article/" + article_name + ".md")

            info_message += "<br/><br/><p style='color:green;'>" + article_name + " 已删除</p>"

        articlelist_content = open(home_dir + "md/articlelist/articlelist.md" ,'r').read().replace\
            ("(/article?article_name=", "(" + back_dir + "/delete?article_name=")
        articlelist_content = markdown(articlelist_content)
        self.render("../page/back/delete.html", articlelist = articlelist_content, back_dir = back_dir, info_message = info_message)
