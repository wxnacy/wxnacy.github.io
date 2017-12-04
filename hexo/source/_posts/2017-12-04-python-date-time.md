---
title: Python 时间
date: 2017-12-04 21:06:39
tags: [python]
---

## 时间戳的坑

`datetime` 的 `timestamp()` 方法可以获取时间戳

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from datetime import datetime
print(datetime.now().timestamp()        # ==> 1512393482.510263
print(datetime.utcnow().timestamp())    # ==> 1512364682.510288
```
在使用 `datetime` 的 `timestamp()` 方法获取时间戳时遇到一点问题，既然这个方法
