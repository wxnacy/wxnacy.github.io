---
title: Python 常用内置方法
tags:
  - python
date: 2018-02-27 08:44:17
---


Python 常用内置方法
<!-- more -->
```bash
__init__(self,...)        # 初始化对象，在创建新对象时调用
__del__(self)             # 释放对象，在对象被删除之前调用
__new__(cls,*args,**kwd)  # 实例的生成操作
__str__(self)             # 在使用print语句时被调用
__getitem__(self,key)     # 获取序列的索引key对应的值，等价于seq[key]
__len__(self)             # 在调用内联函数len()时被调用
__cmp__(stc,dst)          # 比较两个对象src和dst
__getattr__(s,name)       # 获取属性的值
__setattr__(s,name,value) # 设置属性的值
__delattr__(s,name)       # 删除name属性
__getattribute__()        # __getattribute__()功能与__getattr__()类似
__gt__(self,other)        # 判断self对象是否大于other对象 >
__lt__(slef,other)        # 判断self对象是否小于other对象 <
__ge__(slef,other)        # 判断self对象是否大于或者等于other对象 >=
__le__(slef,other)        # 判断self对象是否小于或者等于other对象 <=
__eq__(slef,other)        # 判断self对象是否等于other对象 ==
__call__(self,*args)      # 把实例对象作为函数调用
```

## 用法
巧用内置方法，很多时间会起到意想不到的效果
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name


if __name__ == "__main__":
    a = User(1, 'wxnacy')
    b = User(2, 'ning')
    c = [a, b]
    print(a in c)
```
上边这个例子，最后会打印 `True`，如果去掉重写的 `__eq__` 方法，则返回 `False`，原因在于 `in` 表达式将对象 a 与 数组 c 中每个元素做了 `==` 比较，而 `==` 表达式就是用调用了对象的 `__eq__` 内置方法，重写了这个方法，即可以自定义我们对象的比较方法，其他的内置方法也都可以起到类似的作用。
