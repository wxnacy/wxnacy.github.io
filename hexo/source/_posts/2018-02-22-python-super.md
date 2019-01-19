---
title: Python super() 继承方法
tags:
  - python
date: 2018-02-22 10:31:28
---


super() 函数是用于调用父类(超类)的一个方法。

<!-- more --><!-- toc -->
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。

## py2
```python
class TestJson(dict):
    def __init__(self, *args, **kwargs):
        super(TestJson, self).__init__(*args, **kwargs)
```
## py3
```python
class TestJson(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
```

以前只是用 py2 的方法，后来发现了 py3 的写法，果断抛弃之，快拥抱 py3 吧，时代在进步

- [Python super() 函数](http://www.runoob.com/python/python-func-super.html)
