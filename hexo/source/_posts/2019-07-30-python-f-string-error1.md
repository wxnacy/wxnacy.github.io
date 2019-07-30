---
title: Python 报错 f-string expression part cannot include a backslash
tags:
  - python
date: 2019-07-30 15:02:15
---


Python 3.6 版本新增加的 `f-string` 语句非常简洁，其中可以直接在字符串中使用表达式，可以让代码写起来非常方便。

<!-- more -->
<!-- toc -->

不过也要了解它的一些特性，不然就可能会报一个错误。

```python
>>> n = 2
>>> f'say {"\t" * n}'
  File "<input>", line 1
SyntaxError: f-string expression part cannot include a backslash
```

好像也没有用错，确实应该这样写的，错误翻译过来是 `f-string` 的表达式中不能出现反斜杠。

那记住这一点，以后写起来注意下就好了，有两个方法解决。

**外部计算**

将表达式挪到外部计算好后在传入

```python
>>> n = 2
>>> tables = "\t" * n
>>> f'say {tables}'
'say \t\t'
```

**使用 format **

```python
>>> 'say {}'.format('\t' * n)
'say \t\t'
```
