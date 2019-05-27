---
title: Python list 对象一些方法的时间复杂度
date: 2019-05-27 17:07:51
tags: [python]
---

列举下 Python list 对象常用方法的时间复杂度

<!-- more -->
<!-- toc -->

方法                 | 时间复杂度
----                 | ---------
list[i]              | O(1)
list[i] = 1          | O(1)
list[i:j]            | O(k)  k = j - i
list[i:k] = list()   | O(n + k)
list.index(item)     | O(n)
list.append(item)    | O(1)
list.insert(i, item) | O(n)
list.pop()           | O(1)
list.pop(i)          | O(n) 假如推出的是第一个元素，那么数组所有的元素都要重新计算坐标
del list[i]          | O(n)
item in list         | O(n)
list.reverse()       | O(n)
list.sort()          | O(n logn)
