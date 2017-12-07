---
title: Python 操作目录文件相关命令
date: 2017-08-11
tags: [python]
---

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import os
import sys

cur_file = sys.argv[0]              # ==> 获取当前文件名
print(cur_file)
# python test.py                    ==> test.py
# python test/test.py               ==> test/test.py
# python /Users/wxnacy/test/test.py ==> /Users/wxnacy/test/test.py
# __file__ 可以达到同样效果

cmd_dir = os.getcwd()               # ==> 获取命令运行目录绝对路径
print(cmd_dir)
# python test.py                    ==> /Users/wxnacy/test
# python test/test.py               ==> /Users/wxnacy

print(os.listdir(cmd_dir))          # ==> 获取目录下的所有文件
print(os.path.exists(cmd_dir))      # ==> 判断文件或目录是否存在
print(os.path.isfile(cmd_dir))      # ==> 判断是否为文件
print(os.path.isdir(cmd_dir))       # ==> 判断是否为目录

dirname = os.path.dirname(cur_file) # ==> 获取文件目录名
print(dirname)
# os.path.dirname('test.py')        ==> 空
# os.path.dirname('test/test.py')   ==> test

abspath = os.path.abspath(cur_file) # ==> 获取文件名的绝对路径
print(abspath)
# os.path.abspath('')               ==> 运行命令所在目录
# os.path.abspath('test/test.py')   ==> /Users/wxnacy/test/test.py
# os.path.abspath('/Users/wxnacy')  ==> /Users/wxnacy
```
