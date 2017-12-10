#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:


from app.common import utils
import os
import sys
import time
from datetime import datetime

if __name__ == "__main__":
    print(time.time())
    utc = time.gmtime(time.time())
    print(utc)
    res = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
    print(res)
    t = '2017-12-10 16:37:17'
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    res = int(time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S')))
    print(res)
    print(datetime.now().timestamp())
    res = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    print(res)
