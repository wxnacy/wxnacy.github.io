---
title: Ubuntu 报错 Unable to locate package
date: 2017-11-23 11:13:57
tags: [linux]
---

在给 Ubuntu 安装 Git 时，报了 `Unable to locate package git` 的错误，经 Google
后发现 apt-get 本地的包列表长时间没有更新已经过时了，只需要更新后在安装即可
<!-- more -->

```bash
$ apt-get update
$ apt-get install git
```
