# 整数翻转

## 题目描述

难度：简单

知识点：数学

地址：[https://leetcode-cn.com/problems/reverse-integer/](https://leetcode-cn.com/problems/reverse-integer/)

```
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

    输入: 123
    输出: 321
示例 2:

    输入: -123
    输出: -321
示例 3:

    输入: 120
    输出: 21
注意:

    假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
```

## 字符串翻转

说来惭愧，看到这道题的第一反应是先转成字符串，翻转完字符串后，再次转为整数，这个没什么值得推导了，直接上代码了。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:

    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        y = ""
        rev = 0
        a = str(x)
        length = len(a)
        for i in range(length):
            index = length - 1 - i
            if not y and a[index] == "0":
                continue
            y += a[index]
        if y[-1] == "-":
            rev = -int(y[0:-1])
            if rev < self.MIN:
                return 0
            return rev
        rev = int(y)
        if rev > self.MAX:
            return 0
        return rev
```

### 复杂度分析

- 时间复杂度：O(log(x))，x 中大约有 log10(x) 位数字

- 空间复杂度：O(1)

## 弹出和推入数字

字符串的方式虽然时间复杂度并不高，但是分析起来太复杂了，要考虑各种情况，很容易出 BUG，说到数字翻转，取余、弹出、推入是首选办法。

### 推导过程

`x` 取出个位数字，推入到 `rev` 中，然后 `x` 除以 10 减少一位，再次取出个位数字，同时将 `rev` 乘以 10 增加一位，然后加上取出的个位数，如此往复，然后在这个过程中判断数字是否溢出即可。

```
x       rev
123     0
12      3       pop = 123 % 10 = 3  x = 120 / 10 = 12   rev = 0 ** 10 + 3 = 3
1       32      pop = 12 % 10 = 2   x = 10 / 10 = 1     rev = 3 ** 10 + 2 = 32
0       321     pop = 1 % 10 = 1    x = 0 / 10 = 0      rev = 32 ** 10 + 1 = 321
```

### 代码

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:

    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    def reverse(self, x: int) -> int:
    def reverse1(self, x: int) -> int:
        rev = 0
        div = 10 if x > 0 else -10  # 如果数字为负，div 也要为负
        max_r = (self.MAX - 7) // 10
        min_r = (self.MIN + 8) // 10
        while x != 0:
            pop = x % div           # x 取余，pop 就是要推出的数字
            rev = rev * 10 + pop    # 将 pop 推到 r 的后面
            x = ( x - pop ) // 10   # 推出 pop 后 x 应该等于的数字
            # 防止整数溢出
            if rev > max_r or (rev == max_r and pop > 7):
                return 0
            if rev < min_r or (rev == min_r and pop < -8):
                return 0
        return rev
```

### 复杂度分析

- 时间复杂度：O(log(x))，x 中大约有 log10(x) 位数字

- 空间复杂度：O(1)

## 其他语言

- [python](https://github.com/wxnacy/study/blob/master/python/leetcode/7-reverse-integer.py)
