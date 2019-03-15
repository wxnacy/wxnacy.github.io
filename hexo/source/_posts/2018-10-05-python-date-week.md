---
title: Python 日期输出星期信息
date: 2018-10-05 14:26:24
tags: [python]
---

Python `datetime.date` 模块是可以输出星期天数的，不过是从 0 开始的数字

<!-- more --><!-- toc -->

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

>>> from datetime import date
>>> today = date.today()
>>> today.weekday()
4
```

4 即为今天是周五，我们可以使用一个 JSON 常量来格式化输出。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from datetime import date

WEEK = {
    0: '周一',
    1: '周二',
    2: '周三',
    3: '周四',
    4: '周五',
    5: '周六',
    6: '周日',
}

today = date.today()

print(WEEK[today.weekday()])
# 周五
```
