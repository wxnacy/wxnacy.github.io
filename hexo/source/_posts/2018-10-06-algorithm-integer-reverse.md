---
title: 算法题：整数翻转（难度：简单）
date: 2018-10-06 10:18:24
tags: [算法]
---


> 《算法题》是个系列文章，题主要来自 [LeetCode](https://leetcode-cn.com/problemset/all/)，每道题我尽量使用两种以上的方法来解决，一种是好理解，但是可能性能差，一种需要花点功夫理解，但是性能好，所以题均由 Python 实现

<!-- more -->

先看下题目要求

> 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
>
> 示例 1: `输入: 123 输出: 321`
> 示例 2: `输入: -123 输出: -321`
> 示例 3: `输入: 120 输出: 21`
>
> 注意: 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

### 使用字符串

提到翻转，我们第一反应是使用字符串，因为是探讨算法，我们不使用语言的特性，比如 `a[::-1]` 就直接可以实现字符串翻转。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

MAX = 2 ** 31 - 1
MIN = -2 ** 31

def reverse1(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    y = ""
    r = 0
    a = str(x)
    length = len(a)
    for i in range(length):
        index = length - 1 - i
        if not y and a[index] == "0":
            continue
        y += a[index]
    if y[-1] == "-":
        r = -int(y[0:-1])
        if r < MIN:
            return 0
        return r
    r = int(y)
    if r > MAX:
        return 0
    return r
```

这个算法看上去并不简洁，因为题目的限制，逻辑上显得比较复杂，我们再看一下使用数学的方式翻转。

### 数学运算

这个算法的思路还是像字符串一样，将 `x` 的最后一位推出，并推到 `r` 的前边。

**推出**最后一位，我们使用取余的方式。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

MAX_R = (MAX - 7) // 10
MIN_R = (MIN - -8) // 10

def reverse2(x):
    """
    使用取余的方式，弹出 x 的最后一位，并推到 r 的后面，并如此往复，直到 x = 0
    :type x: int
    :rtype: int
    """
    r = 0
    while x != 0:
        chu = 10
        if x < 0:           # 根据整数的正负，使用相应的取余除数
            chu = -10
        pre = x % chu       # 弹出 x 的最后一位
        x = (x - pre) // 10 # 取余完毕后，整数减去一位
        if r > MAX_R or (r == MAX_R and pre == 7):
            # MAX_R = 2147483640
            # 此处防止后续推入 pre 时，整数溢出
            return 0
        if r < MIN_R or (r == MIN_R and pre == -8):
            # MIN_R = -2147483648
            # 此处防止后续推入 pre 时，整数溢出
            return 0
        r = r * 10 + pre    # 将弹出的最后一位，推到 r 的后面
    return r
```

再看这次代码，现在逻辑简洁了很多，我们使用测试用例测试结果

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
import unittest

class TestMain(unittest.TestCase):

    def test_reverse1(self):
        self.assertEqual(reverse1(123), 321)
        self.assertEqual(reverse1(-123), -321)
        self.assertEqual(reverse1(-12300), -321)
        self.assertEqual(reverse1(1534236469), 0)
        self.assertEqual(reverse1(-1563847412), 0)
        self.assertEqual(reverse1(0), 0)

    def test_reverse2(self):
        self.assertEqual(reverse2(123), 321)
        self.assertEqual(reverse2(-123), -321)
        self.assertEqual(reverse2(-12300), -321)
        self.assertEqual(reverse2(1534236469), 0)
        self.assertEqual(reverse2(-1563847412), 0)
        self.assertEqual(reverse2(0), 0)

if __name__ == "__main__":
    unittest.main()
```

```bash
$ python 7_reverse_integer.py

..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

我们再来测试下他们的运行速度

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import time

def print_func_run_time(count, func, **kw):
    b = time.clock()
    for i in range(count):
        func(**kw)
    print(func.__name__, 'run {} times used {}s'.format(count, time.clock() -b ))

print_func_run_time(count, reverse1, x=1534236469)
print_func_run_time(count, reverse2, x=1534236469)
```

```bash
$ python 7_reverse_integer.py

reverse1 run 10000 times used 0.02178899999999999s
reverse2 run 10000 times used 0.025115s
```

运行了，发现有点奇怪，理论上 `reverse2` 时间复杂度要更小，但结果并不是这样，可能是我测试的方式不对。

即使时间有差距，但也不大，还是更推荐第二种算法，因为逻辑更简单，也不容易出错。

完整代码地址：https://github.com/wxnacy/study/blob/master/python/leetcode/7_reverse_integer.py


该题来自 [LeetCode](https://leetcode-cn.com/problems/reverse-integer/)
