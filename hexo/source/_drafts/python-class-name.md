---
title: Python 获取 class 名字
tags: [python]
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
