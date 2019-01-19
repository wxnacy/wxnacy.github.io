---
title: Flask 重镜像地址
date: 2018-07-31 15:22:16
tags: [flask]
---

flask 中 redirect 方法可以重镜像地址。

<!-- more --><!-- toc -->

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/baidu')
def bd():
    '''重镜像'''
    return redirect('http://baidu.com')

@app.route('/')
def index():
    '''获取路由地址，并重镜像'''
    return redirect(url_for('bd'))
```
