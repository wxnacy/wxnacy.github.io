---
title: Python collections.namedtuple() 命名元组的工厂函数
date: 2019-06-12 16:25:52
tags: [python]
---

`collections` 包中的 `namedtuple()` 函数可以创建命名元组，并提供可读性和自文档性。它可以用于普通元组并使用名称或索引获取值。

<!-- more -->
<!-- toc -->

先看一个例子

```python
>>> from collections import namedtuple
>>> User = namedtuple('User', ['name', 'age'])
>>> u = User('wxnacy', 12)
>>> u
User(name='wxnacy', age=12)
>>> u.name
'wxnacy'
>>> u[1]
12
>>> type(u)
<class '__main__.User'>
```

`namedtuple()` 可以很快捷的创建一个元组子类，再来看一下它的语法

```python
collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
```

- `typename` 是创建得到的元组子类名
- `field_names` 域名序列，可以是一个字符串序列 `[x, y]`，或者用空格、逗号隔开的字符串 `x y` 或 `x, y`
    任何有效的字符串都可以当做域名，除了以下划线和数字开头的字符串和[关键字](https://docs.python.org/zh-cn/3/library/keyword.html#module-keyword)，比如 `_name`, 'class' 等
- `rename` 无效域名会自动转换成位置名。比如 `['abc', 'def', 'ghi', 'abc']` 转换成 `['abc', '_1', 'ghi', '_3']` ， 消除关键词 def 和重复域名 abc。
- `defaults` 可以为 None 或者是一个默认值的 iterable 。如果一个默认值域必须跟其他没有默认值的域在一起出现，defaults 就应用到最右边的参数。比如如果域名 ['x', 'y', 'z'] 和默认值 (1, 2) ，那么 x 就必须指定一个参数值 ，y 默认值 1 ， z 默认值 2 。
- `module` 值如果有定义，命名元组的 `__module__` 属性值就被设置。

**命名元组实例没有字典，所以它们要更轻量，并且占用更小内存。**

除了继承元组的方法，命名元组还支持三个额外的方法和两个属性。为了防止域名冲突，方法和属性以下划线开始。

- `classmethod somenamedtuple._make(iterable)` 类方法从存在的序列或迭代实例创建一个新实例。

```python
>>> User._make(['wxnacy', 18])
User(name='wxnacy', age=18)
```

- `somenamedtuple._asdict()` 返回一个新的 OrderedDict ，它将字段名称映射到它们对应的值

```python
>>> u = User._make(['wxnacy', 18])
>>> u._asdict()
OrderedDict([('name', 'wxnacy'), ('age', 18)])
```

- `somenamedtuple._replace(**kwargs)` 返回一个新的命名元组实例，并将指定域替换为新的值

```python
>>> u._replace(name = 'winn')
User(name='winn', age=18)
```

- `somenamedtuple._fields` 字符串元组列出了域名。用于提醒和从现有元组创建一个新的命名元组类型。

```python
>>> u._fields
('name', 'age')
```

- `somenamedtuple._field_defaults` 默认值的字典。

```python
>>> User = namedtuple('User', ['name', 'age'], defaults=['wxnacy', 18])
>>> u = User()
>>> u._fields_defaults
{'name': 'wxnacy', 'age': 18}
```

`3.5` 版本以后，文档字段变为可写

```python
>>> User = namedtuple('User', ['name', 'age'], defaults=['wxnacy', 18])
>>> User.__doc__
'User(name, age)'
>>> User.__doc__ += ": user in collection"
>>> User.__doc__
'User(name, age): user in collection'
>>> User.name.__doc__ = "User name"
>>> User.name.__doc__
'User name'
```


- [namedtuple()](https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple)
