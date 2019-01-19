---
title: Python 获取时区的偏移量
date: 2018-09-29 14:57:34
tags: [python]
---

Python 中想要获取计算时区相关的问题，可以借助 `pytz` 模块。

<!-- more --><!-- toc -->

**下载**

```bash
$ pip install pytz
```

比如想要通过时区名获取对应的小时偏移量可以这样。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from pytz import timezone
from datetime import datetime
tz = timezone("America/New_York")
res = datetime.now(tz).utcoffset().total_seconds()/60/60
print(res)
# -5.0
```
