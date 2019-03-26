---
title: Python 计时器 timeit
tags:
  - python
date: 2019-03-26 22:10:02
---


网上很多帖子讨论 Python 中计时用 `time.clock()` 还是用 `time.time()`。

<!-- more --><!-- toc -->

## time.clock() vs time.time()
- `time.clock()` 计算的是 CPU 的时间，在 windows 平台上精度比较高
- `time.time()` 计算的是程序的运行时间，会受到机器负载的影响，除了 windows 以外的平台精度比较高

所以我们可以按照平台来使用不同的方法

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import time
import sys

if sys.platform == "win32":
    # On Windows, the best timer is time.clock()
    default_timer = time.clock
else:
    # On most other platforms the best timer is time.time()
    default_timer = time.time
```

或者呢，直接使用 `timeit` 模块

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import timeit

b = timeit.default_timer()
# to some
e = timeit.default_timer()
print(e - b)
```

`timeit.default_timer()` 可以自动选择当前平台适合的计时器，因为它的源代码就是上面那段判断代码。

下面我们重点来介绍下 `timeit` 模块

`timeit` 模块提供了一种简单的方法来计算一小段Python代码。 它既有命令行界面，也有可调用界面。 它避免了许多用于测量执行时间的常见陷阱。

## timeit

**命令行使用**

```python
$ python -m timeit '"-".join(str(n) for n in range(100))'
10000 loops, best of 3: 40.3 usec per loop
```

默认情况下，命令行对小段代码，重复执行三个循环，每个循环执行 10000 次，其中最好的用了 40.3 秒

**代码块中使用**

```python
>>> import timeit
>>> # attribute is missing
>>> s = """\
... try:
...     str.__nonzero__
... except AttributeError:
...     pass
... """
>>> timeit.timeit(s)
0.5832341330096824
>>> timeit.timeit(s, number=1000)
0.000628526002401486
```

`number` 不指定时，默认为 `default_number = 1000000`

```python
>>> timeit.repeat(s)
[0.5949273270089179, 0.6405833000026178, 0.5868908820120851]
>>> timeit.repeat(s, repeat=4)
[0.5963048749981681, 0.5834796829876723, 0.5749933830084046, 0.5814367970015155]
```

增加重复次数，使用 `repeat()` 方法，不指定 `repeat` 时，默认 `default_repeat = 3`

## 命令行语法

```bash
python -m timeit [-n N] [-r N] [-s S] [-t] [-c] [-h] [statement ...]
```
- `-n N, --number=N` 执行 `statement` 的次数
- `-r N, --repeat=N` 循环的重复次数，默认：3
- `-s S, --setup=S` 最初要执行的语句，默认：pass
- `-t, --time` 使用 `time.time()` 计时，在 windows 以外平台默认使用该模式
- `-c, --clock` 使用 `time.clock()` 计时，在 windows 平台默认使用该模式
- `-v, --verbose` 打印原始计时结果，得到更多数字精度
- `-h, --help` 帮助信息

当 `-n` 不指定时，程序会自动执行 10 的倍数，使执行时间不少于 0.2 秒

`-s` 可以执行一段前置代码，这在很多场景是很有用的

**命令行中使用**

```bash
$ python -m timeit -s 'text = "sample string"; char = "g"'  'char in text'
10000000 loops, best of 3: 0.0877 usec per loop
```

**代码块中使用**

在代码快中，这个参数更有用处，我们不必把代码都写在字符串中

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def test():
    """Stupid test function"""
    L = []
    for i in range(100):
        L.append(i)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
```

- 文档：https://docs.python.org/2/library/timeit.html
- 源代码：https://github.com/python/cpython/blob/2.7/Lib/timeit.py

