#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from datetime import datetime 
from datetime import timezone
import time
import pytz
import re

ex_list = [dict(age=44, n=74), dict(age=43, n=44), dict(age=24, n=43),
        dict(age=74, n=24)]

l = ['BB', 'aa', 'cc']

class User():
    """"""
    def __init__(self):
        pass

    def get_name(self):
        pass

def test_re_match():

    res = re.match('www', 'https://www.wxnacy.com')
    print(res)


if __name__ == "__main__":
    test_re_match()
