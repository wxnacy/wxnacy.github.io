---
title: Redis 命令行登陆
date: 2018-09-24 11:24:40
tags: [redis]
---

因为 Redis 本身的安全限制，很多服务器提供的 Redis 都不会提供外网访问，那使用命令行访问数据库内容就不可避免。

<!-- more --><!-- toc -->

`redis-cli` 为 Redis 登录基本命令

```bash
$ redis-cli
redis 127.0.0.1:6379>
```

访问远程服务

```bash
$ redis-cli -h host -p port -a password
```

加上 `--raw` 可以避免中文乱码

```bash
$ redis-cli --raw
```

- [Redis 命令](https://www.runoob.com/redis/redis-commands.html)
