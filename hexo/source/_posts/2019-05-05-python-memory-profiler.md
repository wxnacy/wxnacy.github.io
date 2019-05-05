---
title: Python 使用 memory_profiler 分析程序内存占用情况
date: 2019-05-05 17:18:09
tags: [python]
---

Python 中可以使用 memory_profiler 包来分析程序的内存占用情况

<!-- more -->
<!-- toc -->

memory_profiler 可以分析每行代码的内存使用情况，使用起来非常简单。

## 安装

```bash
$ pip install memory_profiler
```

## 使用

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from memory_profiler import profile

@profile
def test1():
    c = []
    a = [1, 2, 3] * (2 ** 20)
    b = [1] * (2 ** 20)
    c.extend(a)
    c.extend(b)
    del b
    del c

if __name__ == "__main__":
    test1()
```

```bash
$ python -m memory_profiler memory_profiler
```

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/pmf1.png)

结果如图，每一步的内存变化情况都很清楚

- `Mem usage` 为当前总内存
- `Increment` 为增加的内存

总结起来使用非常时间

- 方法前加上 `@profile` 主键
- 使用 `python -m memory_profiler` 来运行，不过直接用 `python` 运行也可以

通过上面这段代码我们可以发现，`del` 语句只是将变量删除，并不能减少内存的消耗。

## 参数使用

- `precision` 显示小数点后的位数

默认显示的内存单位为 `MiB`，小数点后显示一位，如果某行代码占用内存比较小，就可能显示不出来，此时可以通过调整小数点后的位数实现。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from memory_profiler import profile


@profile(precision=4)
def test3():
    a = [1, 2] * (2 ** 10)

if __name__ == "__main__":
    test3()
```

![3](https://raw.githubusercontent.com/wxnacy/image/master/blog/pmf3.png)

- `stream` 将结果输出到流中

每次运行都要打印内存情况，势必会影响程序输出效果，我们可以将结果通过流输出到文件中

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from memory_profiler import profile

@profile(precision=4, @profile(precision=4, stream=open('/tmp/memory_profiler.log','w+')))
def test3():
    a = [1, 2] * (2 ** 10)

if __name__ == "__main__":
    test3()
```

![4](https://raw.githubusercontent.com/wxnacy/image/master/blog/pmf4.png)

## mprof 命令

memory_profiler 本身也提供了命令行 `mprof`

```bash
Usage: mprof <command> <options> <arguments>

Available commands:

    run      运行给定的命令或 python 文件
    rm       删除 mprof 生成的给定文件
    clean    清除当前目录中 mprof 创建的文件
    list     显示带索引的现有配置文件
    plot     可以将 mprof run 的结果生成图片

Type mprof <command> --help for usage help on a specific command.
For example, mprof plot --help will list all plotting options.
```

重点说一下 `plot` 命令，`run` 命令可以生成 `.dat` 文件，`plot` 可以将该文件生成图片，不过需要 `matplotlib` 包的加持。

```bash
$ pip install matplotlib
$ mprof run memory_profiler_demo.py
$ mprof list
0 mprofile_20190505182200.dat 18:22:00 05/05/2019
$ mprof plot mprofile_20190505182200.dat
```

结果如下

![5](https://raw.githubusercontent.com/wxnacy/image/master/blog/pmf5_1260.png)
