# 两数相加

## 题目描述

难度：中等

知识点：链表、数学

地址： [https://leetcode-cn.com/problems/add-two-numbers/](https://leetcode-cn.com/problems/add-two-numbers/)

```
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例:

    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
```

## 两次遍历

首先从题目描述我们可以很直观的得到一个很直接的解法，先计算 `l1` 和 `l2` 表示的整数，相加后，再根据数字推导出 `l3`

这时会用到数学的进位和取余。

### 推导过程

```bash
l1: 2 -> 4 -> 3
    |
    2 * ( 10 ** 0 ) + 4 * ( 10 ** 1 ) + 3 * ( 10 ** 2 ) = 342
```

```bash
l2: 5 -> 6 -> 4
    |
    5 * ( 10 ** 0 ) + 6 * ( 10 ** 1 ) + 4 * ( 10 ** 2 ) = 465
```

```bash
    807 -> 807 % 10 = 7
            |
            -> 80 % 10 = 0
                |
                -> 8 % 10 = 8
l3: 8 -> 0 -> 7
```

### 代码

根据上边的推导，很自然可以得到下面的代码，这个过程需要经历两次遍历。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = 0, 0
        n = 0
        while l1 or l2:
            if l1:
                n1 += l1.val * (10 ** n)
                l1 = l1.next
            if l2:
                n2 += l2.val * (10 ** n)
                l2 = l2.next
            n += 1

        n3 = n1 + n2
        if n3 == 0:
            return ListNode(0)

        l3 = ListNode(0)
        l4 = l3
        while n3 > 0:
            rmd = n3 % 10
            l4.next = ListNode(rmd)
            l4 = l4.next
            n3 = (n3 - rmd) // 10

        return l3.next
```

### 复杂度分析

时间复杂度：O(n)，`n = max(len(l1), len(l2)) + 1` 加一是因为可能会遇到进位。

空间复杂度：O(n)，同上

## 一次遍历

再回过头来观察三个链表可以发现，`l3` 的每个位置刚好是 `l1` 和 `l2` 每个位置的和，那我们完全可以在一次循环内完成取值、求和、生成 `l3` 的操作，只是需要在列表的结尾需要考虑 `carry` 进位的问题。

### 推导过程

```bash
l1: 2 ->    4 -> 3
    +       +    +
l2: 5 ->    6 -> 4
    =       =    =
l3: 7+ 1 -> 0 -> 7
```

### 代码

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        l3 = ListNode(0)
        l4 = l3
        while l1 or l2 or carry:
            n3 = carry
            if l1:
                n3 += l1.val
                l1 = l1.next
            if l2:
                n3 += l2.val
                l2 = l2.next
            carry = n3 //  10
            l4.next = ListNode(n3 % 10)
            l4 = l4.next
        return l3.next
```

### 复杂度分析

时间复杂度：O(n)，两种的时间复杂度相同，但是只进行了一次遍历，所以实际时间会快一些

空间复杂度：O(n)，同样的会节省掉 `n1` 和 `n2` 所占用的空间。

## 其他语言

- [python](https://github.com/wxnacy/study/blob/master/python/leetcode/2-add-two-numbers.py)
