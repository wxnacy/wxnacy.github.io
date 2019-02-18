#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import os
import time

#  from googletrans import Translator
#  translate = Translator()
#  result = translate.translate('America Argentina Jujuy', dest='zh-CN')
#  print(result.text)


#  from pytz import timezone
#  from datetime import datetime
#  tz = timezone("America/New_York")
#  res = datetime.now(tz).utcoffset().total_seconds()/60/60
#  print(res)

class User():
    def get(self):
        print("user")

u = User()
print(type(User))
print(type(u))

def get(self):
    print('user')
Class = type('User', (object,), {
    'get': get
})

u = Class()
print(type(Class))
print(type(u))

print(time.time())
