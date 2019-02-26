---
title: Mysql insert ... on duplicate key update 的用法及在 SQLAlchemy 中的使用
date: 2019-02-24 12:09:12
tags: [mysql, sqlalchemy]
---

在项目高并发时，很容易出现数据库插入相同数据的情况，虽然可以使用唯一索引避免插入相同数据，但是不断的程序报错也是我们也避免的。

<!-- more --><!-- toc -->

## 语法

使用 `insert ... on duplicate key update ..` 语法可以避免这种情况，举个例子

```mysql
drop table if exists `test`;
create table `test` (
	`id` int(11) not null AUTO_INCREMENT,
	`name` varchar(32) not null default '',
	`update_ts` timestamp not null default current_timestamp(),
	primary key (`id`)
) engine=InnoDB default charset=utf8mb4;
```

主键 `id` 是天然的唯一索引，我们插入重复数据时会报错

```mysql
> INSERT INTO test (id, name) VALUES (1, 'wxnacy');
> INSERT INTO test (id, name) VALUES (1, 'wxnacy');
Error 1062: Duplicate entry '1' for key 'PRIMARY'
```

查看数据

```mysql
> SELECT * FROM `test`;
| id | name   | update_ts           |
|------------------------------------
| 1  | wxnacy | 2019-02-24 12:26:58 |
```

下面我们来换个语句

```mysql
> insert into test (id, name) values (1, 'wxnacy') on duplicate key update update_ts = current_timestamp();
> SELECT * FROM `test`;

+----+--------+---------------------+
| id | name   | update_ts           |
+----+--------+---------------------+
|  1 | wxnacy | 2019-02-24 12:31:49 |
+----+--------+---------------------+
```

`on duplicate key update` 前面是正常的插入语句，其后跟着的是当唯一索引冲突时，想要更新的数据。

再换个使用场景，如果我想让数据库中用户名是唯一的，则可以先建立唯一索引，在使用该语法。

```mysql
> alter table test add unique index_name (name);
> insert into test (name) values ('wenn') on duplicate key update update_ts = current_timestamp();
> SELECT * FROM `test`;
+----+--------+---------------------+
| id | name   | update_ts           |
+----+--------+---------------------+
|  1 | wxnacy | 2019-02-24 12:31:49 |
|  2 | wenn   | 2019-02-24 12:39:25 |
+----+--------+---------------------+

> insert into test (name) values ('wenn') on duplicate key update update_ts = current_timestamp();
> SELECT * FROM `test`;

+----+--------+---------------------+
| id | name   | update_ts           |
+----+--------+---------------------+
|  1 | wxnacy | 2019-02-24 12:31:49 |
|  2 | wenn   | 2019-02-24 12:40:15 |
+----+--------+---------------------+
```

这样及保证了避免插入重复数据，同时程序也没有报错，我还可以根据 `update` 的数据来分析问题的根源。

## SQLAlchemy 中的使用

这个功能需要 SQLAlchemy 1.2 版本以上才支持，官方的例子

```python
from sqlalchemy.dialects.mysql import insert

insert_stmt = insert(my_table). \
    values(id='some_id', data='some data to insert')

on_conflict_stmt = insert_stmt.on_duplicate_key_update(
    data=insert_stmt.inserted.data,
    status='U'
)

conn.execute(on_conflict_stmt)
```

析出的 sql 语句为

```mysql
INSERT INTO my_table (id, data)
VALUES (:id, :data)
ON DUPLICATE KEY UPDATE data=VALUES(data), status=:status_1
```

参考资料

- [INSERT ... ON DUPLICATE KEY UPDATE Syntax](https://dev.mysql.com/doc/refman/8.0/en/insert-on-duplicate.html)
- [Support for INSERT..ON DUPLICATE KEY UPDATE](https://docs.sqlalchemy.org/en/latest/changelog/migration_12.html#support-for-insert-on-duplicate-key-update)
