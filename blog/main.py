# coding:utf8

import tornado.options
import tornado.web
import tornado.ioloop
import tornado.httpserver

from handler.BaseHandler import BaseHandler
from handler.IntroduceHandler import IntroduceHandler
from handler.ArticleListHandler import ArticleListHandler
from handler.ArticleHandler import ArticleHandler

from handler.BackIntroduceHandler import BackIntroduceHandler
from handler.LoginHandler import LoginHandler
from handler.LogoutHandler import LogoutHandler
from handler.BackArticleListHandler import BackArticleListHandler
from handler.BackArticleHandler import BackArticleHandler
from handler.UploadHandler import UploadHandler
from handler.DeleteHandler import DeleteHandler
from handler.ChangePassHandler import ChangePassHandler

from handler.CodeRainHandler import CodeRainHandler
from handler.Fspider import FspiderHandler

from conf.conf import run_port, cookie_secret, debug_open, home_dir, back_dir, login_dir, log_position
import tornado.log


if __name__ == "__main__":
    tornado.options.define("port", default=run_port, help="run on the given port", type=int)
    # 默认log保存位置
    tornado.options.options.log_file_prefix = log_position
    tornado.options.parse_command_line()
    settings = {
    "cookie_secret": cookie_secret,
    "xsrf_cookies": True,
    "login_url": "/",  # 别定位到登陆，定位到登陆就算是漏洞了,因为我们要隐藏登陆入口
    "static_path": home_dir + "static",
    "debug":debug_open
    }
    app = tornado.web.Application(
        handlers=[("/", IntroduceHandler),
                  ("/articlelist",ArticleListHandler),
                  ("/article",ArticleHandler),
                  (login_dir, LoginHandler),
                  (back_dir, BackIntroduceHandler),
                  # 后台部分的路由，应该隐藏在back_dir后
                  (back_dir + "/articlelist", BackArticleListHandler),
                  (back_dir + "/article", BackArticleHandler),
                  (back_dir + "/upload", UploadHandler),
                  (back_dir + "/delete", DeleteHandler),
                  (back_dir + "/changepass",ChangePassHandler),
                  (back_dir + "/logout", LogoutHandler),
                  ("/favicon.ico", tornado.web.StaticFileHandler,dict(url='favicon.ico',permanent=False)),
                  # 代码雨
                  ("/comein", CodeRainHandler),
                  # Fspider
                  (r"/comeon.*", FspiderHandler),
                  (r".*", BaseHandler)

                 ], **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()