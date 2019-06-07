---
title: Python 二分查找模块 bisect
tags:
  - python
date: 2019-06-07 20:50:03
---


Python 中 bisect 模块的作用是将一个数字插入到一个排好序的数组中，而不影响数组原来的排序。

<!-- more -->
<!-- toc -->

换句话说是找到一个数字在一个排序数组中应该出现的位置，而它采用的是二分查找法。

既然是二分查找法首先要准备一个排好序的数组

```python
>>> a = [1, 4, 4, 5, 6]
```

我们希望知道再插入一个 `4`，应该出现在什么位置。

```python
>>> import bisect
>>> bisect.bisect(a, 4)
3
```

`bisect()` 方法只是返回一个索引不会更改数组，另外还有 `bisect_right()` 和 `bisect_left()` 两个方法，`bisect_right()` 等同于 `bisect()` 都是从数组右侧开始查找，而 `bisect()` 是从左侧开始查找。

```python
>>> bisect.bisect_left(a, 4)
1
```

如果想要直接插入这个数字呢？可以用 `insort()` 方法

```python
>>> bisect.insort(a, 4)
>>> a
[1, 4, 4, 4, 5, 6]
```

这个方法没有返回值，是在原数组上做的修改，另外也还有 `insort_left()` 和 `insort_right()`，他们的作用相信你已经明白了。

说到这的话，其实标题说 `bisect` 是二分查找模块有点不准确，因为当数组中没有该数字时，`bisect.bisect()` 方法也会返回一个有效索引。所以如果我们想把它当做二分查找法的话，还需要做一些判断

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import bisect

def binary_search(nums, n):
    i = bisect.bisect_left(nums, n)
    if i >= len(nums):
        return -1
    else:
        if nums[i] == n:
            return i
        else:
            return -1
```

最后要说的是，数组只能是正序，如果是倒序该模块不生效

```python
>>> a.reverse()
>>> a
[6, 5, 4, 4, 2, 1]
>>> bisect.insort_left(a, 2)
>>> a
[2, 6, 5, 4, 4, 2, 1]
```
