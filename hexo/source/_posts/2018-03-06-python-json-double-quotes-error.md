---
title: Python 解析单引号 JSON 格式数据报错
tags:
  - python
date: 2018-03-06 10:28:12
---


> JSONDecodeError Expecting property name enclosed in double quotes line 1 column 2 (char 1)

Python 在使用 `json.loads()` 方法时会报一个标题提到的错误，这是因为 JSON 格式的问题。
<!-- more -->
首先 JSON 格式数据本身规定字符串必须使用双引号来包裹，而 `loads()` 方法又没有做这方面的处理，想要解决 BUG 笨点办法就是用双引号替换单引号

当然更好的办法就是使用 [ast](https://docs.python.org/3/library/ast.html#ast-helpers) 模块

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import ast

text = "{'name': 'wxnacy'}"
res = ast.literal_eval(text)
print(res)  # => {'name': 'wxnacy'}
```
