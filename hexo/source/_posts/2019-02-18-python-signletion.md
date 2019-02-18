---
title: Python 单例的四种实现方式
date: 2019-02-18 16:21:49
tags: [python]
---

设计模式中，单例模式是很常见的，今天总结下 Python 的几种实现方式。

<!-- more --><!-- toc -->

## 使用 import

`import` 是 Python 中的天然单例模式，我最先推荐这种方式。

创建两个文件 `signletion.py` `signletion_import.py`，文件内容如下

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: import 需要的部分

class User():
    def __new__(cls, *args, **kw):
        print("new instance")
        return super().__new__(cls, *args, **kw)

    def get(self):
        print("get class")


u = User()
u.get()
```

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: import 模式

from singletion import u

u.get()

# 输出结果：
# new instance
# get class
# get class
```

运行结果只输出一次 `new instance`，代表只生成一个实例，创建单例成功，后续我们都用这种验证方式。

## 使用 __new__ 方法

直接修改 `__new__` 方法，类似 Java 的实现方式，实际开发中，我们可以在父类中实现方法，并继承

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用 __new__ 方法

class Singletion():
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            print("new instance")
            cls._instance = super().__new__(cls, *args, **kw)
        return cls._instance

class SingClass(Singletion):
    def get(self):
        print("get class")

c = SingClass()
c.get()

c1 = SingClass()
c1.get()

# 输出结果：
# new instance
# get class
# get class
```

## 使用装饰器

装饰器是比较 Python 的方式，内部实现跟 `__new__` 很像，判断已经有实例则不再生成。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 装饰器模式

def singletion(cls):
    instance = {}
    def get_instance(*args, **kw):
        if cls not in instance:
            print("new instance")
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return get_instance

@singletion
class User():
    def get(self):
        print("get class")

u = User()
u.get()
u1 = User()
u1.get()

# 输出结果：
# new instance
# get class
# get class
```

## 使用元类

元类同样是 Python 特有的，不过并不常用，我们可以利用它的特性来实现单例

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 使用元类

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("new instance")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SingClass(metaclass=Singleton):
    def get(self):
        print("get class")

c = SingClass()
c.get()

c1 = SingClass()
c1.get()

# 输出结果：
# new instance
# get class
# get class
```

完整 demo 地址：https://github.com/wxnacy/study/tree/master/python/singletion
