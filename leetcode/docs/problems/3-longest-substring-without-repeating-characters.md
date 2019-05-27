# 无重复字符的最长子串

## 题目描述

难度：中等

知识点：哈希表、双指针、字符串、Sliding Window

地址：[https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

```
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
        请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

## 暴力解法

暴力解法依然是最容易想到，也最容易理解的，我们使用两个指针 `i = 0` 和 `j = i + 1`，`i` 不变，`j` 不断的右移，同时将遇到的字符储存到哈希结构中，如果碰见重复数据，则 `i` 右移一位，重新开始右移 `j`，并将遇到的最大长度储存起来。

### 代码

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ans = 1
        temp = 1
        i = 0
        j = 1
        letters = {s[0]}
        while i < len(s) and j < len(s):
            if s[j] not in letters:
                letters.add(s[j])
                temp += 1
                ans = max(ans, temp)
                j += 1
            else:
                i += 1
                j = i + 1
                letters = {s[i]}
                temp = 1

        return ans
```

### 复杂度分析

时间复杂度：O(n^2)，显然最坏的情况需要经过两次循环

空间复杂度：O(n)，所需外部储存空间最大为字符串的长度

### 优化

即使是使用暴力解法，上面的代码我们还可以进行一次优化，在 Python 中使用循环语句要尽量避免使用 `while`，因为这是效率最低的，具体的比较情况可以看我的这篇文章 [Python 中循环语句速度对比](/2019/04/01/python-loop-speed-comparison/)

在这里我们可以将 `while` 改为 `for` 用法。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 1
        temp = 1
        letters = {s[0]}
        for i in range(len(s)):
            for j in range(1, len(s)):
                k = i + j
                if k >= len(s):
                    break
                if s[k] not in letters:
                    letters.add(s[k])
                    temp += 1
                    ans = max(ans, temp)
                else:
                    letters = {s[i + 1]}
                    temp = 1
                    break
        return ans
```

这样优化大概可以节省四分之一的时间，不过并没有从根本上解决什么，我们需要的是量级的优化。

## 滑动窗口

暴力解法的缺点在哪里呢？凡是涉及到计算数组和字符串的子元素问题，暴力解法都会很多的重复运算，尽量多的去掉这些重复计算即可。

滑动窗口算法可以用以解决数组/字符串的子元素问题，它可以将嵌套的循环问题，转换为单循环问题，降低时间复杂度。

在数组/字符串中有开始和结束索引定义的一些列元素的集合，我们称之为窗口。当他们的索引值朝着一个方向增加/减少时，便是窗口的滑动，比如 `[i, j) -> [i + 1, j + 1)`

### 推导过程

暴力解法的推导过程是这样的

```
abcabcbb    i   j   ans
ab          0   1   2
abc         0   2   3
abca        0   3   3
 bc         1   2   3
 bca        1   3   3
...
```

在这个过程中

```
 bc         1   2   3
 bca        1   3   3
```

就是重复的计算。

当 `j` 第一次走过这些位置时，是否有重复我们是知道的，使用哈希表存起来，然后右移 `i` 至不重复的位置，继续遍历下去即可。

```
abcabcbb    i   j   ans
a           0   0   1
ab          0   1   2
abc         0   2   3
abca        0   3   3
 bcab       1   4   3
  cabc      2   5   3
   abcb     3   6   3
     cbb    5   6   3
       b    7   7   3
```

这个过程只经历了一次循环，在这个问题上这将是最优解。

### 代码

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0         # 最大长度
        letters = {}
        temp = 0        # 临时长度
        i = 0
        for j in range(len(s)):
            a = s[j]
            if a not in letters:
                letters[a] = j
                temp += 1
                ans = ans if ans > temp else temp
            else:
                if letters[a] >= i:
                    # 如果重复坐标的位置大于 i，移动 i 到它的前方
                    # 并重新计算临时长度，此时肯定小于最大长度
                    temp = j - letters[a]
                    i = letters[a] + 1
                else:
                    # 否则继续计算临时长度
                    temp += 1
                    ans = ans if ans > temp else temp
                letters[a] = j
        return ans
```

### 复杂度分析

时间复杂度：O(n)，我们只需要遍历一次 s 即可

空间复杂度：O(n)，当整个字符串无重复字符时，需要储存 len(s) 的空间

### 优化？

如果你想的话，还是可以再次优化的，不过这次不是时间复杂度，而是代码复杂度

上面的代码，嵌套了两个 `ifelse`，并且有些重复代码，如果我们想的话，是可以去掉的。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        letters = {}
        i = 0
        for j in range(len(s)):
            a = s[j]
            if a in letters:
                # 只要发现重复字符，就重新计算 i 的位置
                i = max(letters[a] + 1, i)
            # 每次都重新计算最大值
            ans = max(ans, j - i +1)
            letters[a] = j
        return ans
```

这是一种时间换逻辑的改法，它的时间复杂度依然是 O(n)，但是有一些重复计算，速度会稍慢一些，但是逻辑无脑，代码美观，如果你不需要极致的速度，那这是一种不错的写法。

## 其他语言

- [python](https://github.com/wxnacy/study/blob/master/python/leetcode/3-longest-substring-without-repeating-characters.py)
