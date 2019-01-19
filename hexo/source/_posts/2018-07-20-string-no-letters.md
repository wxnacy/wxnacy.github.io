---
title: Python3 与 Python2 的不同之：module 'string' has no attribute 'letters'
date: 2018-07-20 11:32:35
tags: [python]
---

很多人说 Python3 与 Python2 没什么不同，无非就是 `print` 写法不同而已，很显然他没怎么处理过兼容问题。

<!-- more --><!-- toc -->

```python
AttributeError: module 'string' has no attribute 'letters'
```

报这个错误是因为 python3 去掉了该方法，使用 `ascii_letters` 替换即可

```python
str.ascii_letters
```
