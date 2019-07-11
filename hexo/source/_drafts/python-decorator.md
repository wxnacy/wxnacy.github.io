---
title: Python 装饰器
tags: [python]
---

> 要不这样吧，如果编程语言里有个地方你弄不明白，而正好又有个人用了这个功能，那就开枪把他打死。这比学习新特性要容易些，然后过不了多久，那些活下来的程序员就会开始用 0.9.6 版的 Python，而且他们只需要使用这个版本中易于理解的那一小部分就好了（眨眼）。
>   —— Tim Peters （传奇的核心开发者，“Python 之禅”作者）

今天我们来聊一聊 Python 装饰器。

<!-- more -->
<!-- toc -->

## 什么是装饰器

**装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。** 装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象。

先来看一个例子

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def deco(func):                     # 1 创建一个装饰器
    def inner():
        print('running inner()')
    return inner

@deco                               # 2 使用装饰器装饰一个函数
def target():
    print("running target()")

if __name__ == "__main__":
    # 3 执行装饰器返回的函数
    target()                        # running inner()
    # 4 此时 target 是 inner 对象的引用
    print(target)                   # <function deco.<locals>.inner at 0x101609378>
```

装饰器 `deco` 动态的修改了函数 `target()` 的行为，而没有修改它的内容。

严格来说，装饰器只是语法糖。装饰器可以像常规的可调用对象那样调用，其参数是另一个函数，就像下面这样。

```python
>>> t = deco(target)
>>> t()
running inner
```

## 两大特性

装饰器有两大特性：
- 把被装饰的函数替换成其他函数。
- 装饰器在加载模块时立即执行。

第一个特性，通过上面的例子我们已经看到了，这是装饰器的主要作用，但并不是必须的。有时候也会将函数直接返回，只是不太常用。

看一个例子 `registeration.py`

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

registry = []

def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print(f'registry -> {registry}')
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()
```

```python
$ python registeration.py
running register(<function f1 at 0x105485048>)  # 1
running register(<function f2 at 0x1054850d0>)  # 2
running main()
registry -> [<function f1 at 0x105cb3048>, <function f2 at 0x105cb30d0>]
running f1()
running f2()
running f3()
```

在这个例子中，`1, 2` 的输出在 `running main()` 之前，说明了装饰器在模块加载及执行的特性。

## 变量作用域
## 参数化装饰器
