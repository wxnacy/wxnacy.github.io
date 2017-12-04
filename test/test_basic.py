#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from datetime import datetime

ex_list = [dict(age=44, n=74), dict(age=43, n=44), dict(age=24, n=43), 
        dict(age=74, n=24)]

l = ['BB', 'aa', 'cc']


if __name__ == "__main__":
     #  print(ex_list)
     #  #  ex_list.sort(key=lambda x: x['age'])
     #  #  ex_list.sort(key=age)
     #  print(ex_list)
     #  print(l)
     #  l.sort(key=str.lower)
     #  print(l)
     print(datetime.now().timestamp())
     print(datetime.utcnow().timestamp())
