# coding:utf8

from handler.BaseHandler import BaseHandler
from conf.conf import site_key
import random


class FspiderHandler(BaseHandler):
    '''
    Fspider egg
    Track in Spider, just two numbers
    '''
    def get(self):
        self.render("../page/front/fspider.html", site_key=site_key,
                    random_num1=random.randint(0, 2147483647), random_num2=random.randint(0, 2147483647))
