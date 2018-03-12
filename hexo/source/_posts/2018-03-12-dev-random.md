---
title: Unix /dev/random 与 /dev/urandom
tags:
  - linux
date: 2018-03-12 11:37:41
---

> 在UNIX操作系统（包括类UNIX系统）中，[/dev/random](https://zh.wikipedia.org/wiki//dev/random) 是一个特殊的设备文件，可以用作随机数发生器或伪随机数发生器。

<!-- more -->
`/dev/urandom` 是 `/dev/random` 一个副本，非阻塞的随机数发生器，它会重复使用熵池中的数据以产生伪随机数据。这表示对 `/dev/urandom` 的读取操作不会产生阻塞，但其输出的熵可能小于 `/dev/random` 的。它可以作为生成较低强度密码的伪随机数生成器，不建议用于生成高强度长期密码。

常用的生成随机数的方法
```bash
tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)-+= < /dev/urandom | head -c 32 | xargs
```
该命令生成 32 位的带有 `A-Za-z0-9_!@#$%^&*()-+=` 的随机数，在 MacOS 中需要指定语言环境为 C 语言才行
```bash
LC_CTYPE=C tr -dc A-Za-z0-9_\!\@\#\$\%\^\&\*\(\)-+= < /dev/urandom | head -c 32 | xargs
```

- [/dev/random](https://zh.wikipedia.org/wiki//dev/random)
- [/dev/random和/dev/urandom的一点备忘](http://blog.csdn.net/ohmygirl/article/details/40385083)
