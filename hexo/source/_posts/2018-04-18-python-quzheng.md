---
title: Python 取整
date: 2018-04-18 17:29:04
tags: [python]
---

Python 有三种方式取整：向下取整、向上取整、四舍五入。
<!-- more -->
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import math

# 向上取整
print(math.ceil(2.4))   ==> 3

# 向下取整
print(math.floor(2.8))   ==> 2

# 四舍五入
print(round(2.8))   ==> 3
print(round(2.2))   ==> 2

```

