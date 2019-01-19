---
title: Python 格式化函数 format
date: 2018-01-03 17:21:24
tags: [python]
---

自 2.6 以后 Python 增加一个新函数 `str.format()` 来增加字符串格式化的功能

<!-- more --><!-- toc -->
本篇不再对比它跟 `%` 的用法，本着用新不用旧原则，我们只看新函数的一些用法。
## 基础
```python
>>> '{} {}'.format('hello', 'world')        # hello world
>>> '{0} {1}'.format('hello', 'world')      # hello world
>>> '{1} {0}'.format('hello', 'world')      # world hello
```
## 参数
```python
>>> '{name} {age}'.format(name='wxnacy', age=0)     # wxnacy 0
# dict
>>> kwargs = dict(name='wxnacy', age=0)
>>> '{name} {age}'.format(**kwargs)                 # wxnacy 0
>>> '{p[name]} {p[age]}'.format(p=kwargs)           # wxnacy 0
# list
>>> args = [1, 2]
>>> '{0} {1}'.format(*args)                         # 1 2
>>> '{0[0]} {0[1]}'.format(args)                    # 1 2
>>> '{p[0]} {p[1]}'.format(p=args)                  # 1 2
```
## 数字
```python
# 保留小数点2位
>>> '{:.2f}'.format(3.1415926)              # 3.14
# 取整
>>> '{:.0f}'.format(3.1415926)              # 3
# 保留数字符号
>>> '{:+.2f}'.format(3.1415926)             # +3.14
>>> '{:+.2f}'.format(-3.1415926)            # -3.14
# 对齐
>>> '{:5d}'.format(3)                       #     3
>>> '{:<5d}'.format(3)                      # 3
>>> '{:^5d}'.format(3)                      #   3
# 对齐并补位
>>> '{:0>5d}'.format(3)                     # 00003
>>> '{:0<5d}'.format(3)                     # 30000
>>> '{:0^5d}'.format(3)                     # 00300
# 以逗号分隔的数字格式
>>> '{:,}'.format(1000000)                  # 1,000,000
# 百分比格式
>>> '{:.2%}'.format(0.25)                   # 25.00%
# 指数
>>> '{:.2e}'.format(1000000000)             # 1.00e+09
# 进制
>>> '{:b}'.format(11)                       # 1011
>>> '{:d}'.format(11)                       # 11
>>> '{:o}'.format(11)                       # 13
>>> '{:x}'.format(11)                       # b
>>> '{:#x}'.format(11)                      # 0xb
>>> '{:#X}'.format(11)                      # 0xB
```
## 字符串
```python
# 截取
>>> '{:.3}'.format('wxnacy')                # wxn
# 截取并对齐
>>> '{:6.3}'.format('wxnacy')               # wxn
>>> '{:>6.3}'.format('wxnacy')              #    wxn
>>> '{:^6.3}'.format('wxnacy')              #  wxn
# 截取并对齐并占位
>>> '{:0<6.3}'.format('wxnacy')             # wxn000
>>> '{:0>6.3}'.format('wxnacy')             # 000wxn
>>> '{:0^6.3}'.format('wxnacy')             # 0wxn00
```
## 时间
```python
>>> from datetime import datetime
>>> dt = datetime.now()
>>> '{:%Y-%m-%d %H:%M:%S.%s}'.format(dt)
>>> '2018-01-03 18:41:52.1514976112'
>>> '{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M:%S.%s')
>>> '2018-01-03 18:41:52.1514976112'
```
## 对象
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class User():
    def __init__(self):
        self.name = 'wxnacy'

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'räpr'

    def __format__(self, fmt):
        if fmt == 'fmt':
            return "I'm format user"
        return 'user'

if __name__ == "__main__":
    u = User()
    print('{:fmt}'.format(u))   # I'm format user
    print('{!s}'.format(u))     # wxnacy
    print('{!r}'.format(u))     # räpr
    print('{!a}'.format(u))     # r\xe4pr
```
## 转义
```python
>>> '{} position is {{0}}'.format('a')      # a position is {0}
# {{ 来显示左大括号
# }} 来显示右大括号
```
## 参考
- [PyFormat](https://pyformat.info/)
- [Python Strings: Replace, Join, Split, Reverse, Uppercase & Lowercase](https://www.guru99.com/learning-python-strings-replace-join-split-reverse.html)

官方文档并没有明确给出要删除老方法 `%`，也没有说过新的方法速度会比较快，但是它已经有很多功能是 `%` 不支持的了，并且在以后官方也会慢慢只维护新函数，而这种格式化方式也比较适合函数式应用，所以建议都采用这种方式。
