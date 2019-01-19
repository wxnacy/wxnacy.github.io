---
title: Python 几种判断 class 是否包含字段的方法
tags:
  - python
date: 2018-03-02 10:20:34
---


Python 有三种判断 class 是否包含字段的方法

<!-- more --><!-- toc -->
## dir
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class User():
    pass

fields = dir(User)
print('foo' in fields)  # False
```

## hasattr
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class User():
    pass

print(hasattr(User, 'foo')) # False
```
该方法在 py2 中不建议使用，详情见[一个危险的Python函数，不推荐使用](http://codingpy.com/article/hasattr-a-dangerous-misnomer/)

## getattr
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class User():
    pass

print(getattr(User, 'foo', None))   # None
```
这种方法是最安全的
