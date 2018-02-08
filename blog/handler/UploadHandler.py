# coding:utf8

import os
import re
import tornado.web
from BackBaseHandler import BackBaseHandler
from BaseHandler import home_dir
from conf.conf import back_dir


class UploadHandler(BackBaseHandler):
    '''
    上传文章处理
    '''
    @tornado.web.authenticated
    def get(self):
        info_message = "<p style='color:green;'>可多选上传文件</p>"
        self.render("../page/back/upload.html", back_dir=back_dir, info_message=info_message)

    @tornado.web.authenticated
    def post(self):
        info_message = "<br/><br/>"
        if self.request.files:
            haven_files = os.listdir(unicode(home_dir + 'md/article', 'utf-8'))

            files = self.request.files["myfile"]
            file_num = 0
            for file in files:
                if file["filename"][-3:] != ".md":
                    info_message += "<p style='color:red;'>" + file["filename"] + " 需要以.md结尾</p>"
                elif file in haven_files:
                    info_message += "<p style='color:red;'>" + file["filename"] + " 已存在</p>"
                else:
                    # 保存文件
                    open(home_dir + "md/article/" + file["filename"], "wb").write(file["body"])
                    file_num += 1

            info_message += "<p style='color:green;'>" + str(file_num) + "个文件上传成功</p>"
        self.render("../page/back/upload.html", back_dir = back_dir, info_message = info_message)
