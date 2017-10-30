#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.config import BaseConfig
import mistune
import os

class Article():
    def __init__(self):
        self.name = 'test'
        pass

    def get_name(self):
        if self.name:
            return self.name
        else:
            return 'name'

if __name__ == '__main__':
    # python test/test_article.py
    #  CATEGORYS = ['python', 'mysql', 'git']
    #  file_list = os.listdir(BaseConfig.ARTICLE_DIR)
    #  categorys = set([o.split('-', 1)[0] for o in file_list])
    #  categorys = list(filter(lambda x: x in CATEGORYS, categorys))
    #  print(categorys)
    a = Article()
    name = a.get_name()

    print(name)
