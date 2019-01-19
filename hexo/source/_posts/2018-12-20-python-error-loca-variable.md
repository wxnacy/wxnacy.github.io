---
title: Python 报错：local variable 'count' referenced before assignment
date: 2018-12-20 16:06:16
tags: [python]
---

使用 Python 很久了，仍然会碰到一些莫名其妙的错误。

<!-- more --><!-- toc -->

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

count = 0

a = [1, 2, 3]

def fmt(i):
    count += i

[fmt(o) for o in a]
print(count)
```

我的本意是想在 `fmt` 方法中对 `count` 进行累加，但是会报错

```bash
local variable 'count' referenced before assignment
```

google 后发现

```python
count = 0
```

定义为全局变量

```python
def fmt(i):
    count += i
```

方法中只能对局部变量进行修改，***如果想要修改全局变量，需要在方法内使用 global 对变量进行修改***

```python
def fmt(i):
    global count
    count += i
```

完整代码如下

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

count = 0

a = [1, 2, 3]

def fmt(i):
    global count
    count += i

[fmt(o) for o in a]
print(count)
```
