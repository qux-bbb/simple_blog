# coding:utf8

import tornado.web
import random
import re

# 主目录，在读取文件，资源文件时用
import os
home_dir = os.path.dirname(__file__) + "/../"

class BaseHandler(tornado.web.RequestHandler):
    '''
    最基本的handler，规定了错误导向页面
    '''
    # 所有的错误都接管到404页面，使用腾讯404公益页面
    def write_error(self, status_code, **kwargs):
        self.render("../page/front/404.html")