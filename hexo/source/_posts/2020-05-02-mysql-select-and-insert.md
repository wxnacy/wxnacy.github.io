---
title: Mysql 查询一个表的数据并插入到另一个表中
date: 2020-05-02 16:09:17
tags: [mysql]
---

这种情况通常发生在需要迁移数据时

<!-- more -->
<!-- toc -->

如果两个表的结构完全一致，那比较简单

```mysql
insert into test_user1 select * from test_user;
```

如果只有部分字段符合，则需要将具体字段列出

```mysql
insert into test_user1 (name, age) select name, age from test_user;
```

当然也可以过滤掉一些重复数据在插入

```mysql
insert into test_user1 select * from test_user where not exists (select * from test_user1 where test_user1.id = test_user.id);
```
