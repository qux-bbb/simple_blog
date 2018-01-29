# coding:utf8

# 为了解决markdown编码错误问题
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tornado.web
from markdown import markdown
from BackBaseHandler import BackBaseHandler
from conf.conf import back_dir

class BackIndexHandler(BackBaseHandler):
    '''
    负责修改保存 简介，文章
    '''
    @tornado.web.authenticated
    def get(self):
        if (self.get_argument("modify", None)):
            modify = self.get_argument("modify", None)
            # 修改简介
            if modify == "introduce":
                introduce_content = open("md/introduce/introduce.md" ,'r').read()
                self.render("../page/back/introduce.html", introduce = introduce_content, back_dir = back_dir, info_message = "")
            # 展示文章列表
            elif modify == "articlelist":
                # 直接读取此文件需要做些修改，不然点击会直接跳回前端显示文章内容页面
                articlelist_content = open("md/articlelist/articlelist.md" ,'r').read().replace \
                    ("./article", "")
                articlelist_content = markdown(articlelist_content)
                self.render("../page/back/articlelist.html", articlelist = articlelist_content, back_dir = back_dir)
        # 修改单个文章
        elif (self.get_argument("article_name", None)):
            article_name = self.get_argument("article_name", None)
            article_content = open("md/article/" + article_name + ".md" ,'r').read()
            self.render("../page/back/article.html", article_name=article_name, article_content=article_content,
                        back_dir=back_dir, info_message="")

        else:
            # 默认也转到修改introduce页面
            introduce_content = open("md/introduce/introduce.md", 'r').read()
            self.render("../page/back/introduce.html", introduce=introduce_content, back_dir=back_dir, info_message="")

    @tornado.web.authenticated
    def post(self):
        info_message = "<br/><br/><p style='color:green;'>保存成功</p>"
        # 修改并保存简介
        if (self.get_argument("introduce", None)):
            introduce_content = self.get_argument("introduce", None)
            open("md/introduce/introduce.md", 'w').write(introduce_content)

            introduce_content = open("md/introduce/introduce.md", 'r').read()
            self.render("../page/back/introduce.html", introduce=introduce_content, back_dir=back_dir,
                        info_message=info_message)
        # 修改并保存单个文章内容
        elif (self.get_argument("article", None)):
            article_name = self.get_argument("article_name", None)
            article_content = self.get_argument("article", None)
            open("md/article/" + article_name + ".md", 'w').write(article_content)

            article_content = open("md/article/" + article_name + ".md", 'r').read()
            self.render("../page/back/article.html", article_name=article_name, article_content=article_content,
                        back_dir=back_dir, info_message=info_message)
