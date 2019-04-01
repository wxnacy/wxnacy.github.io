---
title: Python 中循环语句速度对比
tags:
  - python
date: 2019-04-01 13:31:39
---


今天来比较下 Python 中循环语句的性能，参赛选手为 `while` `for` `生成器` `内置函数` `列表解析`

<!-- more --><!-- toc -->

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: for while generator list_comprehension map 对比速度

def loop_for(n):
    res = []
    for i in range(n):
        res.append(abs(i))
    return res

def loop_while(n):
    i = 0
    res = []
    while i < n:
        res.append(abs(i))
        i += 1
    return res

def loop_generator(n):
    '''使用生成器'''
    res = (abs(i) for i in range(n))
    res =  list(res)
    return res

def loop_list_compre(n):
    '''使用列表解析'''
    res = [abs(i) for i in range(n)]
    return res

def loop_map(n):
    '''使用内置函数 map'''
    return list(map(abs, range(n)))

import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        '''before each test function'''
        pass

    def tearDown(self):
        '''after each test function'''
        pass

    def test_func(self):
        n = 10
        # 我们要求他们生成的结果是一样的
        flag = (loop_for(n) == loop_while(n) == loop_generator(n) ==
                loop_list_compre(n) == loop_map(n))
        self.assertTrue(flag)

import timeit

def print_func_run_time(count, func, **kw):
    b = timeit.default_timer()
    for i in range(count):
        func(**kw)
    print('{} run {} times used {}s'.format(
        func.__name__.ljust(20),
        count,
        timeit.default_timer() -b ))

if __name__ == "__main__":
    count = 1000
    n = 1000
    print_func_run_time(count, loop_for, n = n)
    print_func_run_time(count, loop_while, n = n)
    print_func_run_time(count, loop_generator, n = n)
    print_func_run_time(count, loop_list_compre, n = n)
    print_func_run_time(count, loop_map, n = n)
    unittest.main()

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
# loop_for             run 1000 times used 0.14018906400087872s
# loop_while           run 1000 times used 0.21399457900042762s
# loop_generator       run 1000 times used 0.12857274799898732s
# loop_list_compre     run 1000 times used 0.08585307099929196s
# loop_map             run 1000 times used 0.043123570998432115s
```

我们以性能好坏来区分，得到的结论

```bash
map > 列表解析 > 生成器 > for > while
```

`map` 是内置函数，底层由 C 来编写，最快是毫无疑问的。而 `while` 是纯 Python 实现的，所以性能最差。

列表解析比生成器要快一些，这里多少有些存疑，因为我们想要返回列表，所以其实 `map` 和生成器都是在负重前行，我们修改下测试方式。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def loop_generator(n):
    res = (abs(i) for i in range(n))
    return res

def loop_list_compre(n):
    res = [abs(i) for i in range(n)]
    return res

def loop_map(n):
    return map(abs, range(n))

import timeit

def print_func_run_time(count, func, **kw):
    b = timeit.default_timer()
    for i in range(count):
        func(**kw)
    print('{} run {} times used {}s'.format(
        func.__name__.ljust(20),
        count,
        timeit.default_timer() -b ))

if __name__ == "__main__":
    count = 1000
    n = 1000
    print_func_run_time(count, loop_list_compre, n = n)
    print_func_run_time(count, loop_map, n = n)
    print_func_run_time(count, loop_generator, n = n)

# loop_list_compre     run 1000 times used 0.08865494900237536s
# loop_map             run 1000 times used 0.0007684140000492334s
# loop_generator       run 1000 times used 0.0009459810025873594s
```

好了，这次我们不再强制转换 list，而仅仅只是返回一个可迭代的对象，发现 `map` 依然最快，生成器稍慢，而列表解析竟然慢了近百倍。

这次我们可以下个结论，处理循环时，我们已经尽可能的使用内置方法，然后根据业务需求来选择使用列表解析和生成器，实在不行了使用 `for` 循环，而 `while` 则是尽量不去使用的。
