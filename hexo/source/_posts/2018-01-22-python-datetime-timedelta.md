---
title: Python timedelta 时间差
tags:
  - python
date: 2018-01-22 14:15:17
---


timedelta 本身代表一个时间差，可以在 date 或 datetime 类型间做时间差运算。

<!-- more --><!-- toc -->
## 时间差运算
```python
In [21]: from datetime import datetime

In [22]: from datetime import timedelta

In [23]: a = datetime.now()

In [24]: b = datetime.utcnow()

In [25]: a - b
Out[25]: datetime.timedelta(0, 28788, 822751)
```
timedelta 不能单独使用，需要引入 datetime 模块，在上面这个例子上 a 是当前北京时间（东八区），b 是 UTC 时间，两者做减法，返回一个 `timedelta(0, 28788, 822751)` 对象，三个值分别代表的是 `days`、`seconds`、`microseconds`。三个值换算后加起来会约等于 8 小时

timedelta 只会保存 `days`、`seconds`、`microseconds` 三个值，其他类型换算如下：
- 1 millisecond（毫秒） 转换成 1000 microseconds（微秒）
- 1 minute 转换成 60 seconds
- 1 hour 转换成 3600 seconds
- 1 week 转换成 7 days

三个参数的取值范围分别为：
- 0 <= microseconds < 1000000
- 0 <= seconds < 3600 * 24 (the number of seconds in one day)
- -999999999 <= days <= 999999999

在 2.7 版本以后 timedelta 增加了 `total_seconds()` 方法
```python
In [35]: timedelta(days=1, hours=2, seconds=3.5)
Out[35]: datetime.timedelta(1, 7203, 500000)

In [36]: timedelta(days=1, hours=2, seconds=3.5).total_seconds()
Out[36]: 93603.5
```
```python
total_seconds() = seconds + days * 24 * 60 * 60 + microseconds / 1000 / 100
```

## 自定义时间差
用法
```python
timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
```
所有参数可选，且默认都是0，参数的值可以是整数，浮点数，正数或负数。
示例
```python
In [27]: from datetime import datetime

In [28]: from datetime import timedelta

In [29]: a = datetime.now()

In [32]: a
Out[32]: datetime.datetime(2018, 1, 22, 13, 58, 46, 45448)

In [30]: a + timedelta(2)
Out[30]: datetime.datetime(2018, 1, 24, 13, 58, 46, 45448)

In [31]: a + timedelta(days=2, hours=3)
Out[31]: datetime.datetime(2018, 1, 24, 16, 58, 46, 45448)
```

## 参考
- [timedelta](https://docs.python.org/2/library/datetime.html#datetime.timedelta)
