# coding:utf8

import tornado.web
from BackBaseHandler import BackBaseHandler
from conf.conf import home_dir, back_dir

class BackArticleHandler(BackBaseHandler):
    '''
    负责修改保存文章
    '''
    @tornado.web.authenticated
    def get(self):
        article_name = self.get_argument("article_name", None)
        article_content = open(home_dir + "md/article/" + article_name + ".md", 'r').read()
        self.render("../page/back/article.html", article_name=article_name, article_content=article_content,
                    back_dir=back_dir, info_message="")

    @tornado.web.authenticated
    def post(self):
        info_message = "<br/><br/><p style='color:green;'>保存成功</p>"
        article_name = self.get_argument("article_name", None)
        article_content = self.get_argument("article", None)
        open(home_dir + "md/article/" + article_name + ".md", 'w').write(article_content)

        article_content = open(home_dir + "md/article/" + article_name + ".md", 'r').read()
        self.render("../page/back/article.html", article_name=article_name, article_content=article_content,
                    back_dir=back_dir, info_message=info_message)
