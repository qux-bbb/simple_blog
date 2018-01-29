# coding:utf8

import re
import tornado.web
from BackBaseHandler import BackBaseHandler
from conf.conf import back_dir

class UploadHandler(BackBaseHandler):
    '''
    上传文章处理
    '''
    @tornado.web.authenticated
    def get(self):
        info_message = "<p style='color:green;'>可多选上传文件</p>"
        self.render("../page/back/upload.html", back_dir = back_dir, info_message = "")

    @tornado.web.authenticated
    def post(self):
        if self.request.files:

            articlelist_content = open("md/articlelist/articlelist.md" ,'r').read()
            haven_filenames = re.findall(r"\[(.*)]", articlelist_content)

            files = self.request.files["myfile"]
            file_num = 0
            info_message = "<br/><br/>"
            for file in files:

                only_name = file["filename"][:-3]
                if file["filename"][-3:] != ".md":
                    info_message += "<p style='color:red;'>" + file["filename"] + " 需要以.md结尾</p>"
                elif only_name in haven_filenames:
                    info_message += "<p style='color:red;'>" + file["filename"] + " 已存在</p>"
                else:
                    # 保存文件
                    open("md/article/" + file["filename"], "wb").write(file["body"])
                    # 保存文件名
                    only_name = file["filename"][:-3]
                    listline = "[" + only_name + "](./article?article_name=" + only_name + ")  \n"
                    open("md/articlelist/articlelist.md" ,'ab+').write(listline)
                    file_num += 1

            info_message += "<p style='color:green;'>" + str(file_num) + "个文件上传成功</p>"
        self.render("../page/back/upload.html", back_dir = back_dir, info_message = info_message)
