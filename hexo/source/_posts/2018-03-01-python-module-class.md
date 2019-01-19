---
title: Python 如何获取模块中所以 class 的列表
tags:
  - python
date: 2018-03-01 14:09:30
---


Python 如何获取模块中所以 class 的列表

<!-- more --><!-- toc -->
查询模块 `foo` 的 class 列表
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import inspect
import foo  # 需要查询的模块

for name, obj in inspect.getmembers(foo):
    if inspect.isclass(obj):
        print obj
```
查询当前模块的 class 列表
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import inspect
import sys

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        print obj
```


