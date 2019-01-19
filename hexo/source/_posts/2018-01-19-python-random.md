---
title: Python random 随机数模块
tags:
  - python
date: 2018-01-19 14:27:48
---


random 模块负责生成各种随机数，下面是几种常用的函数。

<!-- more --><!-- toc -->
## uniform
uniform() 方法将随机生成下一个实数，它在 [x, y) 范围内。
```python
import random   # uniform 是 random 模块中的函数

# random.uniform(x, y)
# x 随机数的最小值，包含该值。
# y 随机数的最大值，不包含该值。

res = random.uniform(0, 5)
print(res)      # 2.5156399226615003
```

## random
random() 方法返回随机生成的一个实数，它在[0,1)范围内。
```python
>>> import random
>>> random.random()
0.1740686850927936
>>> random.random()
0.21103578046838467
```

## randint
randint() 方法返回随机整数，它在 [x, y] 范围内。
```python
>>> random.randint(0, 9)
4
>>> random.randint(0, 9)
0
```
## randrange
randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
```python
import random

random.randrange ([start,] stop [,step])
# start -- 指定范围内的开始值，包含在范围内。
# stop  -- 指定范围内的结束值，不包含在范围内。
# step  -- 指定递增基数。
```
```python
>>> random.randrange(1, 100, 2)     # 从 1-100 中选取一个奇数
81
>>> random.randrange(100)           # 从 0-99 选取一个随机数
84
```
## choice
choice() 方法返回一个数组、元组或字符串的随机项。
```python
>>> random.choice([1, 2, 3, 5, 9])
9
>>> random.choice('wxnacy')
'a'
>>> random.choice((1, 2, 3))
1
```
## shuffle
shuffle() 方法将序列的所有元素随机排序。
```python
>>> a = [1, 2, 3, 4, 5]
>>> random.shuffle(a)
>>> a
[4, 2, 1, 3, 5]
```
## simple
simple() 从指定序列中随机获取指定长度的片断，并返回（不改变元序列）
```python
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> random.sample(a, 5)
[5, 4, 3, 7, 10]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
