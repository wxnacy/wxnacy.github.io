---
title: Python frozenset() 函数
tags:
  - python
date: 2018-10-20 17:28:27
---


`frozenset()` 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

<!-- more -->
<!-- toc -->

参数为一个可迭代的对象，比如列表、字典、元组等等。

```python
>>> a = frozenset()
>>> a
frozenset()
>>> a['s']=1
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a['s']=1
TypeError: 'frozenset' object does not support item assignment
>>> frozenset({1:2, 3:4})
frozenset({1, 3})
>>> frozenset([1, 2, 3])
frozenset({1, 2, 3})
>>> frozenset((1, 2, 3))
frozenset({1, 2, 3})
```
