#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.config import BaseConfig
from app.models import Article
import mistune
import os
import unittest

class Test(unittest.TestCase):

    def test_query_items(self):
        #  items = Article.query_items(order_by='pv,desc')
        #  self.assertEqual(items[0].url, 'https://wxnacy.com/vim/')
        #  items = Article.query_items(order_by='publish_date,asc')
        #  self.assertEqual(items[0].url, 'https://wxnacy.com/vim/')
        res = Article.query_by()
        print(res[0])
        pass

    #  def test_sa(cls):
        #  Article.statistics_article()

if __name__ == "__main__":
    unittest.main()
