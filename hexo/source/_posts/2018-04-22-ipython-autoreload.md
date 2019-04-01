---
title: IPython autoreload 自动重加载
date: 2018-04-22 12:01:50
tags: [python]
---

IPython 在项目开发中快速测试函数是很常用的，但是默认情况下他不会自动重新加载模块，这样在高频繁的改动情况下会很不方便，而 `autoreload` 可以解决这个问题。

<!-- more -->

**运行方法前重新加载所以模块**

```python
$ ipython
In [1]: %load_ext autoreload

In [2]: %autoreload 2

In [3]: from foo import some_function

In [4]: some_function()
Out[4]: 42

In [5]: # open foo.py in an editor and change some_function to return 43

In [6]: some_function()
Out[6]: 43
```

**启动时默认加载**

每次手动执行命令也不是个好主意，最好是默认加载

找到配置文件 `~/.ipython/profile_default/ipython_config.py`

如果你之前没用过这个文件，很可能还不存在，需要手动创建

```bash
$ ipython profile create
```

随后修改该文件，选择下面一种方式即可

```python
c.InteractiveShellApp.exec_lines = [ '%load_ext autoreload', '%autoreload 2' ]
```

或者

```python
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = [ '%autoreload 2' ]
```

随后再次执行 ipython，现在已经自动实现热加载。

- [autoreload](https://ipython.org/ipython-doc/3/config/extensions/autoreload.html)
