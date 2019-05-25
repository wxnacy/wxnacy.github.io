# 两数之和

## 题目描述

难度：简单

知识点：数组、哈希表

地址：[https://leetcode-cn.com/problems/two-sum/](https://leetcode-cn.com/problems/two-sum/)

```
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
```

## 暴力解法

暴力解法，将列表中所以的元素两两相加，直到找到和 `target` 相等的值。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                k = j + i
                if k < len(nums):
                    if nums[i] + nums[k] == target:
                        return [i, k]
        return None
```

### 复杂度分析

时间复杂度：O(n^2)，只要是涉及到两层长度为 n 的 `for` 循环的嵌套，我们都可以直接将时间复杂度判断为 `O(n^2)`。

空间复杂度：O(1)。

## 两遍哈希表

暴力解法的内层循环意在查找一个数字 `nums[k]` 等于 `target - nums[i]`，这个过程的时间复杂度为 O(n^2)，而我们需要优化的就是将它的时间复杂度变为 O(1)，哈希表可以实现这一步。

我们先将列表中的数字和索引的对应关系存入到哈希表中，然后循环一遍列表，找到 `target - nums[i]` 所在的位置即可，这里需要注意的地方在于需要排除 `nums[i]` 本身的位置

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution(object):
    def twoSum(self, nums, target):
        m = {}
        for i in range(len(nums)):
            m[nums[i]] = i
        for i in range(len(nums)):
            b = target - nums[i]
            if b in m and m[b] != i:
                return [i, m[b]]
```

### 复杂度分析

时间复杂度：O(n)，虽然将列表变量了两遍，去掉常数仍然为 O(n)。

空间复杂度：O(n)，所需的额外空间取决于哈希表中存储的元素数量，该表中存储了 n 个元素。

## 一遍哈希表

我们还可以将上面的算法再次优化，两次遍历分别做了不同的事，缓存索引和查找索引，这两件事情可以放在一次循环里进行。

最开始时 `m` 为空，假设 `nums[i]` 和 `b` 是我们想要找的两个数字，当遍历到 `nums[i]` 时，发现 `b` 并没有在 `m` 中，可以先将 `nums[i]` 存入 `m` 中，等到循环到 `b` 时，就可以在 `m` 中找到 `nums[i]`。

需要注意的时，此时我们找到的两个索引位置是反的，调换位置在输出即可。


```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution(object):
    def twoSum(self, nums, target):
        m = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in m:
                return [m[b], i]
            m[a] = i
```


### 复杂度分析

时间复杂度：O(n)，最坏的情况，只有当两个数字为列表的头尾时才会如此。

空间复杂度：O(n)，最坏的情况下需要储存 n 个元素

## 其他语言

- [python](https://github.com/wxnacy/study/blob/master/python/leetcode/1-two-sum.py)
