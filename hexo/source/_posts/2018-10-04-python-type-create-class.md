---
title: Python 使用 type() 动态创建 class
date: 2018-10-04 14:26:52
tags: [python]
---

动态语言比静态语言有一个很方便的地方，就是可以动态创建类和函数，这在很多逻辑实现上会很方便，有些批量代码也可以通过这个特性实现，省去了程序员的手上功夫。

<!-- more --><!-- toc -->

我们先来看一下静态创建的类的类型

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class User():
    def get(self):
        print("user")

u = User()
print(type(User))
print(type(u))
# <class 'type'>
# <class '__main__.User'>
```

从这里可以看到，静态创建的 class 也是 type 类型。

下面我们来动态创建

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def get(self):
    print('user')

Class = type('User', (object,), {
    'get': get
})

u = Class()
print(type(Class))
print(type(u))
# <class 'type'>
# <class '__main__.User'>
```

从结果看动态创建的 class 跟静态创建的完全一样

```bash
type(classname [, super [, func]])
```

type 函数的三个参数分别为
- class 名称，字符串形式
- 需要继承的父类，元组形式，如果只有一个需要注意在最后加上逗号
- 需要绑定的函数，字典形式
