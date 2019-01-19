---
title: CentOS 怎样安装 ifconfig
date: 2018-07-03 13:58:43
tags: [linux]
---

在 centos 的原始版本是不带 `ifconfig` 工具的，而它是 `net-tools` 工具包的一部分。

<!-- more --><!-- toc -->

安装 `net-tools` 就很简单了，使用 `yum` 即可

```bash
$ sudo yum install -y net-tools
```

