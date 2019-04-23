---
title: Redis get 报错 a key holding the wrong kind of value
date: 2019-04-23 15:45:17
tags: [redis]
---

最近发现使用 `redis-cli` 命令来获取数据报错，如下

<!-- more -->
<!-- toc -->

```bash
(error) WRONGTYPE Operation against a key holding the wrong kind of value
```

比较费解，因为线上程序并没有报错，时间紧迫也没有多关注，今天有时间感觉搜索了下。

这个错误是因为对 `key` 的 `value` 使用了错误的操作，比如 `lpush` 的数据只能使用 `lrange` 获取数据，使用 `get` 就会报错。

```bash
127.0.0.1:6379> lpush test_key 1
(integer) 1
127.0.0.1:6379> get test_key
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> lrange test_key 0 1
1) "1"
```

同样的使用 `set` 报错的数据，在使用 `lpush` 就会报错。

因为是很久之前写的代码，已经忘记了是用 `lpush` 保存的数据，所以在命令行中使用 `get` 自然报错。
