---
title: Python 使用多属性来进行排序
tags:
  - python
date: 2019-08-31 14:11:29
---


Python 中 `list.sort()` 是列表中非常常用的排序函数，`key` 参数可以对单个属性进行排序。

<!-- more -->
<!-- toc -->

但是想要实现类似 sql 中 `order by id, age` 一样，对多个字段进行排序就不支持了。

py2 中 `sort()` 函数还有个 `cmp` 参数可以传入一个方法，可以自定义对多个属性进行排序，py3 中移除了这个字段。

py3 想要实现这个功能，需要使用 `functools` 模块中的方法，实例如下

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from functools import cmp_to_key

def cmp_func(a, b):

    if a['id'] < b['id']:
        return -1
    elif a['id'] > b['id']:
        return 1

    if a['name'] < b['name']:
        return -1
    elif a['name'] > b['name']:
        return 1

    return 0

arr.sort(key=cmp_to_key(cmp_func))
```

上面的例子我们实现了 `id` 正序排序，如果 `id` 相同，则按照 `age` 正序排序

为了方便可以封装成一个方法，以供列表调用，封装的方法 demo 可以参见地址

https://github.com/wxnacy/study/blob/master/python/office_module/list_demo/sort_by_multi_fields.py
