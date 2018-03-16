---
title: Python 使用字符串名字导入模块
tags:
  - python
date: 2018-03-16 15:46:22
---


在优化代码时出现一个需求，我希望通过 module 的字符串名字来导入模块，这样可以避免没写一个 module 就手动导入。
<!-- more -->

`importlib.import_module()` 可以完成该操作
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

mod = importlib.import_module('os')
print(mod.getcwd())     # /Users/wxnacy/wxnacy.github.io
```

- [importlib](https://docs.python.org/3/library/importlib.html)
