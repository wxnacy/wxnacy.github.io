---
title: Python 列表 List
date: 2017-11-24 16:43:56
tags: [python]
---

> 序列是 Python 中最基本的数据结构。序列中每个元素都有自己的索引（数字），从 0
开始。Python 有 6 个序列的内置类型，最常见的是列表和元组。

<!-- more -->
<!-- toc -->

## 基础
### 生成
列表的生成很简单，使用赋值的方式即可，列表可以包含数字，字符串等基本类型或数组
字典这样的结构，甚至是这些的混合数据
```python
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c']
l3 = [l1, l1]
l4 = [{"k": "v"}, {"k": "v"}]
l5 = [1, 'a', l1, l4]
```

### 取值
取值包括单个值和一个连续的范围，我们可以使用索引来完成
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

l = [1, 2, 3, 4]

print("l[0] = ", l[0])          # ==> l[0] = 1
print("l[0:2] = ",  l[0:2])     # ==> l[0:2] = [1, 2]
print("l[1:-1] = ", l[1:-1])    # ==> l[1:-1] = [2, 3]
```
前两个我们都好理解，最后一个 -1 可能会有点费解，其实可以这样来想，1 是从左边数
第二个元素，-1 就是从右边数第二个元素，了解了这点，我们就可以很方便的截取前后的
数据

### 更新
想要修改列表某一个索引的数据，只需要直接对该索引位置赋值即可
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

l = [1, 2, 3]
l[2] = 6

print(l)        # ==> [1, 2, 6]
```

列表通过 `append()` 方法添加单个列表项
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

l = [1, 2, 3]
l.append(4)

print(l)        # ==> [1, 2, 3, 4]
```
### 删除
有很多种方式删除列表元素
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

l = [1, 2, 3]
del l[2]
print(l)        # ==> [1, 2]

l = [1, 2, 3]
l.pop(2)        # ==> 3
print(l)        # ==> [1, 2]

l = [1, 2, 3]
l.remove(2)
print(l)        # ==> [1, 3]
```
`del` 和 `pop` 通过索引删除元素，`pop` 方法默认删除最后一个对象，会返回被删除的
数据，`remove` 方法查找匹配到的第一个对象并删除

## 二维数组
Python 中二维数组的本质相当于嵌套数组，就像这样
```python
l = [[1, 2, 3], [4, 5]]
```
而想要改变二维数组的值，只需要嵌套索引赋值即可
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

l = [[1, 2, 3], [4, 5]]
l[0][1] = 10            # 修改
print(l)                # [[1, 10, 3], [4, 5]]
del l[0][1]             # 删除
print(l)                # [[1, 3], [4, 5]]
```

## 拼接/合并
列表的拼接有两种操作符与函数
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

l = [1, 2, 3]
a = [3, 4]

n = l + a
print(n)        # ==> [1, 2, 3, 3, 4]

m = l.extend(a)
print(m)        # ==> [1, 2, 3, 3, 4]
```

### 去重合并
通过上边的例子，我们可以做一点延伸，如何合并去重
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

l = [1, 2, 3]
a = [3, 4]

[l.append(x) for x in a if x not in l]

print(l)        # ==> [1, 2, 3, 4]
```
通过使用列表解析，可以完成去重合并的目的，这也是比较高效的做法

## 函数
```bash
len(list)      # 返回列表的长度
max(list)      # 返回列表的最大值
min(list)      # 返回列表的最小值
list(list)     # 将元组、字典等数据结构转变为列表
```

## 方法
```bash
list.append(obj)           # 在列表末尾添加新对象
list.count(obj)            # 计算列表中某个对象出现的次数
list.extend(seq)           # 在列表末尾追加另一个列表数据
list.index(obj)            # 找出列表中某个对象的索引位置
list.insert(index, obj)    # 在列表指定索引位置插入对象
list.pop(index=-1)         # 删除列表指定索引位置对象，默认删除最后一个
list.remove(obj)           # 删除列表中指定对象的第一个匹配项
list.sort([func])          # 对列表进行排序
list.reverse()             # 对列表进行反向排序
```

## 错误集锦
### sequence item 0: expected str instance, int found
```python
print(','.join([1, 2, 3]))
```
在使用字符串的 `join` 方法将列表对象拼接为一个字符串时，我们期望出现的结果是
`'1,2,3'` 会出现这个错误，出错的原因是因为传入的参数列表中不能含有 int 类型对象，
这时我们需要对列表做些转换，将列表中的对象都转为字符串，使用列表解析可以很高效
的完成这项任务
```python
print(','.join([str(o) for o in [1, 2, 3]]))    # ==> '1,2,3'
```
