---
title: Python 如何给屏幕打印信息加上颜色
tags:
  - python
date: 2019-04-24 13:31:54
---


以前写过 [Go 如何给屏幕打印信息加上颜色](/2018/09/07/go-fmt-color/)，想当然的以为 Python 也一样，结果被打脸，他们的配置还是有一些区别的。

<!-- more -->
<!-- toc -->

## 语法

```python
print('\033[显示方式;字体色;背景色m文本\033[0m')
# 三种设置都可以忽略不写，都不写则为默认输出
```

配置如下

```bash
# 字体 背景 颜色
# ---------------------------------------
# 30  40  黑色
# 31  41  红色
# 32  42  绿色
# 33  43  黄色
# 34  44  蓝色
# 35  45  紫红色
# 36  46  青蓝色
# 37  47  白色
#
# 显示方式
# -------------------------
#  0  终端默认设置
#  1  高亮显示
#  4  使用下划线
#  5  闪烁
#  7  反白显示
#  8  不可见
```

举几个例子

```python
# 高亮显示，字体紫红色，背景白色
text = 'Hello World'
print(f'\033[1;35;47m{text}\033[0m')
```

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/pycolor1.png)

```python
# 默认显示，字体紫红色，背景白色
text = 'Hello World'
print(f'\033[35;47m{text}\033[0m')
```

![2](https://raw.githubusercontent.com/wxnacy/image/master/blog/pycolor2.png)

```python
# 默认显示，字体紫红色，背景默认
text = 'Hello World'
print(f'\033[35m{text}\033[0m')
```

![3](https://raw.githubusercontent.com/wxnacy/image/master/blog/pycolor3.png)

往往我们更关注字体颜色，几个字体颜色效果如下，我用的 iTerm2 的深色背景，效果会有点偏差

![4](https://raw.githubusercontent.com/wxnacy/image/master/blog/output-color.png)

如果你想看所有组合的颜色，可以查看这篇文章 [Go语言在Linux环境下输出彩色字符](https://www.cnblogs.com/journeyonmyway/p/4317108.html)

## 工具化

这个语法看起来还是很别扭的，平常使用我们可以封装起来。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from enum import Enum

class Color(Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37

def print_color(text: str, fg: Color = Color.BLACK.value):
    print(f'\033[{fg}m{text}\033[0m')

# 打印红色文字
print_color('Hello World', fg = Color.RED.value)
```
