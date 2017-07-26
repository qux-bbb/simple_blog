# coding:utf8

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# 引入一个当前文件所在目录，方便import和打开其他文件
import os
root_dir = os.path.dirname(__file__) + "/"

# 引入用户名密码
import sys
sys.path.append(root_dir + "../conf")
from conf import *

# 为了解决markdown编码错误问题
reload(sys)  
sys.setdefaultencoding('utf8')

# 对markdown解析
from markdown import markdown

# 用于提取文件列表里的文件名
import re


from tornado.options import define, options
define("port", default=run_port, help="run on the given port", type=int)


# 主页，就是简介
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        introduce_content = open(root_dir + "../md/introduce/introduce.md",'r').read()
        introduce_content = markdown(introduce_content)
        self.render("../page/front/introduce.html",introduce = introduce_content)

# 文章列表
class ArticleListHandler(tornado.web.RequestHandler):
    def get(self):
        articlelist_content = open(root_dir + "../md/articlelist/articlelist.md",'r').read()
        articlelist_content = markdown(articlelist_content)
        self.render("../page/front/articlelist.html",articlelist = articlelist_content)

# 单个文章
class ArticleHandler(tornado.web.RequestHandler):
    def get(self):
        article_name = self.get_argument('article_name')
        article_content = open(root_dir + "../md/article/" + article_name + ".md" ,'r').read()
        article_content = markdown(article_content)
        self.render("../page/front/article.html",article_name = article_name, article_content = article_content)


# 添加cookie，控制访问
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie(auth_cookie)


# 后台登陆
class LoginHandler(BaseHandler):
    def get(self):
        if login_open == False:
            self.redirect("/")
        else:
            self.render("../page/back/login.html")
    def post(self):
        if login_open == False:
            self.redirect("/")
        else:
            username2 = self.get_argument('username', 'Default_Name')
            password2 = self.get_argument('password', 'Default_Pass')

            if username2 == username and password2 == password:
                self.set_secure_cookie(auth_cookie, username2, expires_days=None)
                self.redirect(back_dir)
            else:
                self.write("<p style='color:red;'>用户名或密码错误！</p>")
                self.render("../page/back/login.html")

# 退出
class LogoutHandler(BaseHandler):
    @tornado.web.authenticated       
    def get(self):
        self.clear_cookie(auth_cookie)
        self.redirect("/")

# 负责修改保存 简介，文章
class BackHandler(BaseHandler):
    @tornado.web.authenticated       
    def get(self):
        if (self.get_argument("modify", None)):
            modify = self.get_argument("modify", None)
            # 修改简介
            if modify == "introduce":
                introduce_content = open(root_dir + "../md/introduce/introduce.md",'r').read()
                self.render("../page/back/introduce.html", introduce = introduce_content, back_dir = back_dir)
            # 展示文章列表
            elif modify == "articlelist":
                # 直接读取此文件需要做些修改，不然点击会直接跳回前端显示文章内容页面
                articlelist_content = open(root_dir + "../md/articlelist/articlelist.md",'r').read().replace("./article", "")
                articlelist_content = markdown(articlelist_content)
                self.render("../page/back/articlelist.html", articlelist = articlelist_content, back_dir = back_dir)
        # 修改单个文章
        elif (self.get_argument("article_name", None)):
            article_name = self.get_argument("article_name", None)
            article_content = open(root_dir + "../md/article/" + article_name + ".md" ,'r').read()
            self.render("../page/back/article.html", article_name = article_name, article_content = article_content, back_dir = back_dir)

        else:
            # 默认也转到修改introduce页面
            introduce_content = open(root_dir + "../md/introduce/introduce.md",'r').read()
            self.render("../page/back/introduce.html", introduce = introduce_content, back_dir = back_dir)

    @tornado.web.authenticated
    def post(self):
        # 修改并保存简介
        if (self.get_argument("introduce", None)):
            introduce_content = self.get_argument("introduce", None)
            open(root_dir + "../md/introduce/introduce.md",'w').write(introduce_content)
            self.write("<p style='color:green;'>保存成功</p>")

            introduce_content = open(root_dir + "../md/introduce/introduce.md",'r').read()
            self.render("../page/back/introduce.html", introduce = introduce_content, back_dir = back_dir)
        # 修改并保存单个文章内容
        elif (self.get_argument("article", None)):
            article_name = self.get_argument("article_name", None)
            article_content = self.get_argument("article", None)
            open(root_dir + "../md/article/" + article_name + ".md" ,'w').write(article_content)
            self.write("<p style='color:green;'>保存成功</p>")

            article_content = open(root_dir + "../md/article/" + article_name + ".md" ,'r').read()
            self.render("../page/back/article.html", article_name = article_name, article_content = article_content, back_dir = back_dir)
 

# 上传
class UploadHandler(BaseHandler):
    @tornado.web.authenticated       
    def get(self):
        self.render("../page/back/upload.html", back_dir = back_dir)

    @tornado.web.authenticated       
    def post(self):
        if self.request.files:

            articlelist_content = open(root_dir + "../md/articlelist/articlelist.md",'r').read()
            haven_filenames = re.findall(r"\[(.*)]", articlelist_content)
            
            files = self.request.files["myfile"]
            file_num = 0
            for file in files:
                only_name = file["filename"][:-3]
                if only_name in haven_filenames:
                    self.write("<p style='color:red;'>" + only_name + " 已存在</p>")
                else:
                    # 保存文件
                    open(root_dir + "../md/article/" + file["filename"], "wb").write(file["body"])
                    # 保存文件名
                    only_name = file["filename"][:-3]
                    listline = "[" + only_name + "](./article?article_name=" + only_name + ")  \n"
                    open(root_dir + "../md/articlelist/articlelist.md",'ab+').write(listline)
                    file_num += 1

            self.write("<p style='color:green;'>" + str(file_num) + "个文件上传成功</p>")
        self.render("../page/back/upload.html", back_dir = back_dir)



# 删除
class DeleteHandler(BaseHandler):
    @tornado.web.authenticated       
    def get(self):
        if (self.get_argument('article_name', None)):
            article_name = self.get_argument('article_name')
            
            # 修改文件列表
            listline = "[" + article_name + "](./article?article_name=" + article_name + ")  \n"
            articlelist_content = open(root_dir + "../md/articlelist/articlelist.md",'r').read()
            open(root_dir + "../md/articlelist/articlelist.md",'w').write(articlelist_content.replace(listline,""))

            # 删除文件
            os.remove(root_dir + "../md/article/" + article_name + ".md")

            self.write("<p style='color:green;'>" + article_name + " 已删除</p>")

        articlelist_content = open(root_dir + "../md/articlelist/articlelist.md",'r').read().replace("./article", "./delete")
        articlelist_content = markdown(articlelist_content)
        self.render("../page/back/delete.html", articlelist = articlelist_content, back_dir = back_dir)







if __name__ == "__main__":
    ROOT_DIR = os.path.split(os.path.realpath(sys.argv[0]))[0]
    tornado.options.parse_command_line()
    settings = {
    "cookie_secret": cookie_secret,
    "xsrf_cookies": True,
    "login_url": "/",  # 别定位到登陆，定位到登陆就算是漏洞了,因为我们要隐藏登陆入口
    "static_path": ROOT_DIR + "/../static",
    "debug":debug_open
    }
    app = tornado.web.Application(
        handlers=[("/", IndexHandler),
                  ("/articlelist",ArticleListHandler),
                  ("/article",ArticleHandler),
                  (back_dir, BackHandler),
                  (login_dir, LoginHandler),
                  # 这三个路由都属于后台部分，应该隐藏在back_dir后
                  (back_dir + "/logout", LogoutHandler),  
                  (back_dir + "/upload", UploadHandler),
                  (back_dir + "/delete", DeleteHandler),
                  ("/favicon.ico", tornado.web.StaticFileHandler,dict(url='favicon.ico',permanent=False))

                 ], **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()