---
title: Python 常用内置方法
tags: [python]
---

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
__gt__(self,other)        # 判断self对象是否大于other对象
__lt__(slef,other)        # 判断self对象是否小于other对象
__ge__(slef,other)        # 判断self对象是否大于或者等于other对象
__le__(slef,other)        # 判断self对象是否小于或者等于other对象
__eq__(slef,other)        # 判断self对象是否等于other对象
__call__(self,*args)      # 把实例对象作为函数调用
```
