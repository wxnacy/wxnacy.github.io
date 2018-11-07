---
title: Python 下载模块报错 install_requires must be a string or list of strings containing valid project/version requirement specifiers
date: 2018-07-21 11:45:39
tags: [python]
---

> It seems that older version of distutils do not support this requirement format.  I will change it and make a new release.

<!-- more --><!-- toc -->
将 distutils 升级到最新版即可

```bash
$ pip install setuptools -U
```

- [Installation error: 'install_requires' must be a string or list of strings containing valid project/version requirement specifiers](https://github.com/sdispater/pendulum/issues/187)
