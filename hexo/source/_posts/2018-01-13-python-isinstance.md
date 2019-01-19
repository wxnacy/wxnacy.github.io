---
title: Python isinstance 函数判断对象类型
date: 2018-01-13 10:18:11
tags: [python]
---

在 Python 中推荐使用 `isinstance()` 函数来判断两个对象类型是否相同

<!-- more --><!-- toc -->
## 用法
```python
isinstance(object, classinfo)
# object    要比较的对象
# classinfo 直接或间接类名，基本类型或者元组
    # 基本类型为 int，float，bool，complex，str，list，dict，set，tuple
```
如果类型相同则返回 True，否则返回 False
```python
In [29]: b = True

In [30]: isinstance(b, bool)
Out[30]: True

In [31]: isinstance(b, int)
Out[31]: True

In [32]: isinstance(b, str)
Out[32]: False

In [32]: isinstance(b, (bool, int, str))    # b 属于元组中的某个类型
Out[32]: True
```
这里有个比较有意思的事情，`b` 应该是 `bool` 类型，但是使用 `int` 类型对比返回的也是 True，原因在于 Python 中 `bool` 是 `int` 一个子类，`True` 和 `False` 就是代表的 1 和 0 。

## 对比 type()
Python 中另一个判断类型的函数 `type()`
```python
In [29]: b = True

In [36]: type(b)
Out[36]: bool
```
`type()` 函数传入一个对象，返回他的对象类型，它只能返回当前类型，不会考虑到继承关系。

由此可见 Python 中 `isinstance()` 函数比 `type()` 函数更合适判断两个对象类型是否相同。

