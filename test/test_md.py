#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''工具类'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

from app.common import utils
import mistune
import os
from datetime import datetime as dt

class User():
    def __init__(self):
        # TODO
        pass


if __name__ == '__main__':
    renderer = mistune.Renderer(escape=True, hard_wrap=True)
    m = mistune.Markdown(renderer=renderer)
    res = m('# hello world')
    #  print(res)
    #  print(os.getcwd())

    path = '{}/doc/{}'.format(os.getcwd(),'index.md')

    #  with open(path) as f:jjjdd

        #  res = m(f.read())
        #  print(res)
    print(utils.get_random_str(3))
    print(os.getenv('helloddd'))
    print(os.getenv('FLASK_CONFIGklllll'))
