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

- [autoreload](https://ipython.org/ipython-doc/3/config/extensions/autoreload.html)
