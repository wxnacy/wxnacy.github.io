# 只出现一次的数字

## 题目描述

难度：简单

知识点：哈希表、位运算

地址：[https://leetcode-cn.com/problems/single-number/](https://leetcode-cn.com/problems/single-number/)

```
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明:

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

    输入: [2,2,1]
    输出: 1
示例 2:

    输入: [4,1,2,1,2]
    输出: 4
```

## 哈希表

这道题这么多的限制条件，显然是为了考察某个知识点，我们先抛开这些，想想如何使用普通方式来解题，并且尽量时间和空间都最优。

凡是涉及某个元素出现次数的问题，都可以优先考虑哈希表，遍历一遍数组统计每个元素出现的次数，在遍历一遍哈希表，找出只出现一次的即可。这样时间复杂度为 O(2n)，空间复杂度为 O(n)

再进一步优化下，因为其他元素都是出现两次，也就是我们可以将重复出现的抵消掉，这样遍历一遍数组后，哈希表只会有一个元素存在，在遍历哈希表时，时间复杂度就是 O(1)。总体时间复杂度为 O(n)，在最优的情况下空间复杂度只有 O(1)。

### 代码

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if n not in m:
                m[n] = 1
            else:
                del m[n]
        for k, v in m.items():
            return k
```

### 复杂度分析

时间复杂度：O(n)

空间复杂度：O(n)

## 异或运算

回归原题的要求，普通方式是不可能达到不使用额外空间的。再看原题，***其余每个元素均出现两次***，这个地方很关键，它提示我们可以使用位运算***异或***来进行计算。

### 推导过程

数组 `[4, 1, 2, 1, 2]` 元素的二进制值分别为 `[100, 1, 10, 1, 10]`

```
4 ^ 1   ->  100 ^ 1
|           |
5 ^ 2   ->  101 ^ 10
|           |
7 ^ 1   ->  111 ^ 1
|           |
6 ^ 2   ->  110 ^ 10
|           |
4       ->  100
```

### 代码

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] = nums[0] ^ nums[i]
        return nums[0]
```

### 复杂度分析

时间复杂度：O(n)

空间复杂度：O(0)，这里确实没有用到额外空间，但是改变数组元素，如果实际开发中可能需要使用变量来储存最后的结果。

## 其他语言

- [Python](https://github.com/wxnacy/study/blob/master/python/leetcode/136-single-number.py)
- [Go](https://github.com/wxnacy/study/blob/master/goland/src/leetcode/136-single-number_test.go)
