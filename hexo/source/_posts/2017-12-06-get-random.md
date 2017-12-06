---
title: 如何获取指定位数随机数
date: 2017-12-06 18:00:59
tags: [算法]
---

在实际开发中经常会用到随机数，这里介绍各种语言的实现方法
<!-- more --><!-- toc -->
## Python
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

STR = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
def get_random_str(str_len):
    """
    获取随机字符串
    :param str_len: 需要获取的长度
    :return:
    """
    def _create():
        return str(STR[int(random.uniform(0, len(STR)))])
    res = [_create() for x in range(0, str_len)]
    return ''.join(res)
```
