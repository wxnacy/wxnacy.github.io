---
title: MacOS 中如何使用 md5sum 命令
date: 2018-09-06 10:13:49
tags: [mac]
---

Liunx 中 md5sum 命令非常强大，加密和校对数据的 md5 都非常方便，MacOS 中没有安装该应用，而是默认安装了 md5 命令。

<!-- more --><!-- toc -->
使用起来非常方便

```bash
$ md5 wdl.go
MD5 (wdl.go) = df52858048902988f21479a854bbf617
```

```bash
$ md5 -r wdl.go
df52858048902988f21479a854bbf617 wdl.go
```

或者使用 `openssl` 中的 md5 方法

```bash
$ openssl md5 wdl.go
MD5(wdl.go)= df52858048902988f21479a854bbf617
```

也可以用管道命令

```bash
$ curl http://baidu.com | md5
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    81  100    81    0     0    794      0 --:--:-- --:--:-- --:--:--   801
a6c4b5d58389762e8e7f67c8a3515d3f
```

- [md5sum on Mac OS X | check MD5 hashes](https://www.garron.me/en/bits/how-to-md5sum-mac-os-x.html)
