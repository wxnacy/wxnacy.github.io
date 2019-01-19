---
title: Mysql 修改字段加上前缀或后缀
date: 2018-07-19 11:33:19
tags: [mysql]
---

最近需要给数据库表某个字段加上前缀，我想当然的这样操作。

<!-- more --><!-- toc -->
```mysql
> update table set field = '-' + field;
```

很显然不对，应该使用 `CONCAT` 方法

```mysql
> update table set field = CONCAT('-' , field);
```
