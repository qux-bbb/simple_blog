# coding:utf8

from handler.BaseHandler import BaseHandler
import random

class FspiderHandler(BaseHandler):
    '''
    Track in Spider, just two numbers
    '''
    def get(self):
        self.render("../page/front/fspider.html",
                    random_num1=random.randint(0, 2147483647), random_num2=random.randint(0, 2147483647))
