#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.config import BaseConfig
from app.models import Article
import mistune
import os

class Article():
    def __init__(self, name):
        self.name = name
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
    Article.query.filter_by(name='wxnacy', content='sssssssssss', is_del=0, name='').first();
    Article.query.filter_by(name='wxnacy', content='sssssssssss', is_del=0).first();
    Article.query.filter_by(name='wxnacy', content='ssssssssssssssss', is_del=0
            ).first();

    a = Article('http://mewe.gochinatv.com/landscapenews/AA3AU9?type=0&version=1.0.0&shop_type=&shop_id=575&mqtt_type=&template_id=0')
    name = a.get_name()

    print(name)
