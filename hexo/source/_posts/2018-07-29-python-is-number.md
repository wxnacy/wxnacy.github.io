---
title: 转载 · Python 判断字符串是否由数字组成的几种方法
date: 2018-07-29 14:59:19
tags: [python]
---

Python 判断字符串是否由数字组成的几种方法

<!-- more --><!-- toc -->
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# 测试字符串和数字
print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False
```

简单的情况下还可以使用另外两个方法
- `"".isdigit()`
- `"".isnumeric()`


- [Python 判断字符串是否为数字](http://www.runoob.com/python3/python3-check-is-number.html)
- [Python3 isnumeric()方法](http://www.runoob.com/python3/python3-string-isnumeric.html)
