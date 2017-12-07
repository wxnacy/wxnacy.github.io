#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:


from app.common import utils
import os
import sys

if __name__ == "__main__":
    cur_dir = os.getcwd()
    print(cur_dir)                        # ==> 获取当前文件目录
    #  print(os.listdir(cur_dir))              # ==> 获取目录下的所有文件
    #  print(os.path.exists(cur_dir))
    print(sys.argv)
    print(__file__)
    print(os.path.dirname('test/test_basic.py'))
    print(os.path.abspath(''))
    print(os.path.abspath(sys.argv[0]))
