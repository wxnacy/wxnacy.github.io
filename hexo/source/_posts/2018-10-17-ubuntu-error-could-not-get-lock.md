---
title: Ubuntu 报错：Could not get lock /var/lib/dpkg/lock
date: 2018-10-17 15:10:54
tags: [linux]
---

在 Ubuntu 中使用 `apt` 下载软件时报了错误

<!-- more --><!-- toc -->
```bash
E: Could not get lock /var/lib/dpkg/lock - open (11 Resource temporarily unavailable)
E: Unable to lock the administration directory (/var/lib/dpkg/) is another process using it?
```

最后几个单词提示 `dpkg` 当前有其他进程在使用，可以通过两种方式解决

```bash
$ sudo rm /var/lib/dpkg/lock
```

或杀掉进程

```bash
$ ps aux | grep apt
$ kill -9 processNum
```

- [Unable to lock the administration directory (/var/lib/dpkg/) is another process using it?](https://askubuntu.com/questions/15433/unable-to-lock-the-administration-directory-var-lib-dpkg-is-another-process)
