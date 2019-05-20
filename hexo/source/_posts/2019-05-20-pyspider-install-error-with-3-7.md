---
title: PySpider 安装的坑：不支持 3.7 版本
tags:
  - python
date: 2019-05-20 18:13:05
---


PySpider 安装还真是各种坑啊，所以感觉不能单独记录，收成一个系列吧。

<!-- more -->
<!-- toc -->

这次的问题是不兼容 3.7 版本，安装虽然成功，但是运行及报错。

```bash
Traceback (most recent call last):
  File "/Users/wxnacy/.pyenv/versions/3.7.2/bin/pyspider", line 11, in <module>
    load_entry_point('pyspider==0.3.10', 'console_scripts', 'pyspider')()
  File "/Users/wxnacy/.pyenv/versions/3.7.2/Python.framework/Versions/3.7/lib/python3.7/site-packages/pkg_resources/__init__.py", line 487, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
  File "/Users/wxnacy/.pyenv/versions/3.7.2/Python.framework/Versions/3.7/lib/python3.7/site-packages/pkg_resources/__init__.py", line 2728, in load_entry_point
    return ep.load()
  File "/Users/wxnacy/.pyenv/versions/3.7.2/Python.framework/Versions/3.7/lib/python3.7/site-packages/pkg_resources/__init__.py", line 2346, in load
    return self.resolve()
  File "/Users/wxnacy/.pyenv/versions/3.7.2/Python.framework/Versions/3.7/lib/python3.7/site-packages/pkg_resources/__init__.py", line 2352, in resolve
    module = __import__(self.module_name, fromlist=['__name__'], level=0)
  File "/Users/wxnacy/.pyenv/versions/3.7.2/Python.framework/Versions/3.7/lib/python3.7/site-packages/pyspider/run.py", line 231
    async=True, get_object=False, no_input=False):
        ^
SyntaxError: invalid syntax
```

一看到这个错误心里就有一种不祥的预感，妥妥的代码出错了啊，咋它就这么多事呢？

这个错误的原因在于 `3.7` 版本以上已经把 `async` 和 `await` 列为关键字，所以在用 `async` 当参数名自然会报错，看了下源码，已经将 `async` 改为了 `async_mode`，但是最新发行版本 `0.3.10` 版本已经一年多了，还没有发新版是怎么个意思，作者也觉得 `3.7` 版本兼容还很大呗，好吧，人家也没说过支持 `3.7`，你想用就自己折腾呗。

这时候有两种方式，第一下载最近版本的代码，然后改个版本号自己编译

```bash
$ git clone https://github.com/binux/pyspider
$ cd pyspider
$ vim pyspider/__init__.py
__version__ = '0.3.11'
$ pip install .
```

或者将当前版本的代码修改一下，替换掉 `async`

```bash
$ vim /Users/wxnacy/.pyenv/versions/3.7.2/Python.framework/Versions/3.7/lib/python3.7/site-packages/pyspider/run.py
$ vim /Users/wxnacy/.pyenv/versions/3.7.2/Python.framework/Versions/3.7/lib/python3.7/site-packages/pyspider/fetcher/tornado_fetcher.py
$ vim /Users/wxnacy/.pyenv/versions/3.7.2/Python.framework/Versions/3.7/lib/python3.7/site-packages/pyspider/webui/app.py
```

前面那一大坨是本地仓库的位置，打开文件后复制下面的文字然后回车即可。

```bash
:%s/async/async_mode/g
```

然后再次运行即可。
