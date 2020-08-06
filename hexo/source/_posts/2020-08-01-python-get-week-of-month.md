---
title: Python 获取某天是当月的第几周
tags:
  - python
date: 2020-08-01 21:47:21
---


Python 本身是不提供这样的方法的，我们需要自己做下处理。

<!-- more -->
<!-- toc -->

**思路**

- `strftime("%W")` 方法可以获取日期在当年的第几周
- 借此，我们可以分别获取获取当天和月初是当年的第几周
- 然后，做下减法，在加一就可以了

代码如下

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from datetime import datetime

def get_week_of_month(query_date):
    """
    获取某个日期是当月的第几周
    """
    end = int(query_date.strftime("%W"))
    begin = int(datetime(query_date.year, query_date.month, 1).strftime("%W"))
    return end - begin + 1
```
