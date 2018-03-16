#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import hashlib
import sys
import inspect
import importlib
import os

def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

class User():
    pass

u = User()
print(u.__class__.__name__)

if __name__ == "__main__":
    str = "www.wxnacy.com"
    print(str.upper())          # 把所有字符中的小写字母转换成大写字母
    print(str.lower())          # 把所有字符中的大写字母转换成小写字母
    print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
    print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 

    mod = importlib.import_module('os')
    print(mod.getcwd())
