---
title: Python 处理 Linux 命令
date: 2017-12-09 10:36:35
tags: [python, linux]
---

在 Python 开发中经常会需要处理一些 Linux 命令，下面介绍几种常见的处理此类命令模块，以下命令均在 `ipython` 中进行

<!-- more --><!-- toc -->
## os 模块
```python
In [5]: import os
In [5]: os.system('echo "Hello World"')
Hello World
Out[5]: 0
```
使用 `system()` 方法可以执行命令，但是方法返回的结果是 0，在大多数情况下，这不是我们想要的
```python
In [6]: os.popen('echo "Hello World"')
Out[6]: <open file 'echo "Hello World"', mode 'r' at 0x10faa5c00>
```
`popen()` 方法可以返回结果，但是返回的是一个 file 类型，通过对返回值在使用 `read()` 或 `readlines()` 返回即可拿到结果
```python
In [7]: os.popen('echo "Hello World"').read()
Out[7]: 'Hello World\n'
```

## commands
os 模块可以勉强达到我们想要的效果，但是用起来会很别扭，我们还可以使用 commands 模块提供的 `getstatusoutput(), getoutput()` 两个方法来完成任务
```python
In [1]: import commands

In [2]: commands.getstatusoutput('ls')
Out[2]:
(0,
 'README.md\nTest.java\nUser-Admin\nUser-Api\nUser-Base\npom.xml\nsrc\ntarget\nuser-center.iml')
```
`getstatusoutput()` 方法会返回一个元组 `(status, output)` 分别为执行状态和结果，这个结果是用字符串的形式将结果呈现出来，而 `getoutput()` 方法只返回结果

```python
In [3]: commands.getoutput('ls')
Out[3]: 'README.md\nTest.java\nUser-Admin\nUser-Api\nUser-Base\npom.xml\nsrc\ntarget\nuser-center.iml'
```

## subprocess
在官方文档中 subprocess 模块是被用来替换上边提到的方法的，它可以开启子线程工作，比他们更加灵活。它有非常丰富的使用方法，这里简单介绍输出方法 `check_output()`
```python
In [13]: import subprocess

In [14]: subprocess.check_output('ls')
Out[14]: 'README.md\nTest.java\nUser-Admin\nUser-Api\nUser-Base\npom.xml\nsrc\ntarget\nuser-center.iml\n'
```
简单的命令没有太大区别，但是执行一些复杂的方法会有所不同
```python
In [15]: subprocess.check_output('echo "hello world"')
OSError: [Errno 2] No such file or directory
```
在进行复杂命令时，该方法需要接收一个数组
```python
In [16]: subprocess.check_output(['echo', 'hello world'])
Out[16]: 'hello world\n'
```
更多使用方法见[文档](https://docs.python.org/2/library/subprocess.html)
