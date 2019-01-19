---
title: Python pip 安装模块报错（Expected, end-of-list）
date: 2018-08-29 18:19:46
tags: [python]
---

Python 新环境中安装项目所需包时，可能会报一个类型的错误

<!-- more --><!-- toc -->

```bash
    "Expected ',' or end-of-list in",line,"at",line[p:]
ValueError: ("Expected ',' or end-of-list in", "tornado>=4.2.1,<6.0; python_version < '3.5'", 'at', "; python_version < '3.5'")
```

这种情况通常是 `setuptools` 版本太老导致的，更新一下版本即可

```bash
$ pip install --upgrade setuptools
```
