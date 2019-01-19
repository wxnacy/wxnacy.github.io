---
title: python 配置PYTHONPATH(了解python导入模块搜索路径运作原理)
date: 2017-08-15
tags: [python]
---

> python项目导入模块是必不可少的，大多数情况下，可以以来模块导入搜索路径的
自动特性，完全不需要配置路径。不过，如果你想在用户间定义目录边界来导入文件，
就需要知道搜索路径是如何运作的。

<!-- more -->

<!-- toc -->

```bash
$ python tests/test_utils.py

Traceback (most recent call last):
  File "tests/test_utils.py", line 7, in <module>
    from run_api import app
ImportError: No module named 'run_api'

```
在我刚学习python时，做模块导入最长碰到的就是这个错误，我明明定义了 `run_api`
模块，但是却总是报找不到的错误， No module No module No你妹啊，如果你也碰到这
样的问题，你应该好好看看这篇文章

## 不太好的解决办法
```python
import sys
import os
sys.path.append( os.path.join( os.path.dirname(__file__), os.path.pardir ) )
```
在 google 模块导入问题的时候，大部分博客给出了这样的解决方案，在每个文件配置
这样的代码，他做到了将当前文件的路径加入到 Python 模块搜索路径 sys.path 中，
确实可以起到解决 bug 的作用，但是每个文件都写上这样一段代码，实在让人不舒服，
下面我们还是来学习下 Python 模块搜索路径是如何运作的

## Python 从哪些路径导入模块
```
1、程序的主目录
2、PYTHONPATH 目录（如果已经进行了设置）
3、标准链接库目录
4、任何 .pth 文件的内容（如果存在的话）
```

### 主目录
Python 首先会在主目录内搜索导入的文件。如果程序完全位于单一目录，所有导入的会
自动工作，而并不需要配置路径。由于这个目录总是先搜索，其文件也将覆盖路径上的
其他目录中具有同样名称的模块。如果你需要在自己程序中使用库模块的话，小心不要
以这种方式以外地隐藏库模块。

### PYTHONPATH 目录
之后，Python 会从左到右搜索 PYTHONPATH 环境变量设置中罗列出的所有目录，可以是
用户定义或平台特定的目录名。因为 Python 优先搜索主目录，当导入的文件跨目录时，
这个设置才显得格外重要。

### 标准库目录
接着，Python 会自动搜索标准库模块安装在机器上的那些目录，这块通常不需要在单独
配置

### .pth 文件目录
最后，Python 有个相当新的功能，允许用户把有效的目录添加到模块搜索路径中去，
也就是在后缀名为 .pth （路径的意思）的文本文件中一行一行的列出目录。他是 
PYTHONPATH 的一种替代方案，我们也可以把它放在标注库所在位置的 sitepackages 的
子目录中扩展模块搜索路径

## 应用到当前项目
在开发大型项目之前，我们可以将项目根目录作为 PYTHONPATH 存到环境变量中，也可以
每次运行前之前该命令
```bash
$ touch env.sh
$ vim env.sh

export PYTHONPATH=./ # 将项目根目录作为PYTHONPATH

$ source env.sh # 在项目运行之前执行该命令
```
最后我们可以通过下面两行代码来查看当前项目python模块搜索路径和导入的模块
```python

import sys

print(sys.path) # 输出python模块搜索目录

print(list(sys.modules.keys())) # 输出python已经导入的模块列表
```
