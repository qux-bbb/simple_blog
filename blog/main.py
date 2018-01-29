# coding:utf8

import tornado.options
import tornado.web
import tornado.ioloop
import tornado.httpserver

from handler.BaseHandler import BaseHandler
from handler.IndexHandler import IndexHandler
from handler.ArticleListHandler import ArticleListHandler
from handler.ArticleHandler import ArticleHandler

from handler.BackIndexHandler import BackIndexHandler
from handler.LoginHandler import LoginHandler
from handler.LogoutHandler import LogoutHandler
from handler.UploadHandler import UploadHandler
from handler.DeleteHandler import DeleteHandler

from handler.CodeRainHandler import CodeRainHandler
from handler.Fspider import FspiderHandler

from conf.conf import run_port, cookie_secret, debug_open, back_dir, login_dir


from tornado.options import define, options
define("port", default=run_port, help="run on the given port", type=int)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
    "cookie_secret": cookie_secret,
    "xsrf_cookies": True,
    "login_url": "/",  # 别定位到登陆，定位到登陆就算是漏洞了,因为我们要隐藏登陆入口
    "static_path": "./static",
    "debug":debug_open
    }
    app = tornado.web.Application(
        handlers=[("/", IndexHandler),
                  ("/articlelist",ArticleListHandler),
                  ("/article",ArticleHandler),
                  (back_dir, BackIndexHandler),
                  (login_dir, LoginHandler),
                  # 这三个路由都属于后台部分，应该隐藏在back_dir后
                  (back_dir + "/logout", LogoutHandler),  
                  (back_dir + "/upload", UploadHandler),
                  (back_dir + "/delete", DeleteHandler),
                  ("/favicon.ico", tornado.web.StaticFileHandler,dict(url='favicon.ico',permanent=False)),
                  # 代码雨
                  ("/comein", CodeRainHandler),
                  # Fspider
                  (r"/comeon.*", FspiderHandler),
                  (r".*", BaseHandler)

                 ], **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()