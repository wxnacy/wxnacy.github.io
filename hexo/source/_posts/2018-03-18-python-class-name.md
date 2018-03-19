---
title: Python 获取 class 名字
tags:
  - python
date: 2018-03-18 09:54:17
---


```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class User():
    pass

u = User()
print(u.__class__.__name__)     # User
```
