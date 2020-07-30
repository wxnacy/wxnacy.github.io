---
title: Python 使用双引号打印字典数据
tags:
  - python
date: 2020-05-01 15:55:34
---


默认 Python 打印字典数据是用的单引号

<!-- more -->
<!-- toc -->

但标准的 JSON 数据都是用双引号的，我希望可以用双引号打印并直接复制


使用 `json.dumps` 方法即可

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
import json
m = dict(name = '温', others=['wen'])
print(json.dumps(m, ensure_ascii=False))
```
```bash
{"name": "温", "others": ["wen"]}
```
