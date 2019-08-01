---
title: Mysql 开始慢查询日志
tags:
  - mysql
date: 2019-08-01 17:09:32
---


项目长期运行过程中，Mysql 慢查询的监控是必不可少的一步日常工作，今天来说下配置过程。

<!-- more -->
<!-- toc -->

## 配置

先来查看默认慢查询日志开启状态

```mysql
mysql> show variables like "%slow_query_log%";
+---------------------+--------------------------------------+
| Variable_name       | Value                                |
+---------------------+--------------------------------------+
| slow_query_log      | OFF                                  |
| slow_query_log_file | /var/lib/mysql/1bcb14797cd4-slow.log |
+---------------------+--------------------------------------+
2 rows in set (0.01 sec)
```

- `slow_query_log` 是否开启慢查询日志，默认关闭
- `slow_query_log_file` 慢查询日志的默认位置，系统自动生成的文件名。自定义的日志名最好符合 `*-slow.log` 格式，后面会讲到原因。

因为慢查询日志本身比较耗性能，所以默认是关闭的，在需要的时候我们需要手动打开。

```mysql
mysql> set global slow_query_log=1;
Query OK, 0 rows affected (0.09 sec)
```

该命令可以全局开启该功能，但是如果 Mysql 服务重启则会还原默认值，想要持久化，需要修改配置文件，然后重启

```bash
$ vim /etc/mysql/my.cnf
```

```bash
[mysqld]
# 开启慢查询日志
slow_query_log=1
# 设置慢查询日志位置
slow_query_log_file=/var/lib/mysql/slow.log
```

```bash
$ sudo systemctl restart mysql
```

修改 `slow_query_log_file` 时需要注意，文件的目录位置必须已存在，否则会报错，慢查询日志功能自动关闭。

另外还一些其他的参数可以修改，方法跟上面的一样。

- `long_query_time` 慢查询阈值，当查询时间多于设定的阈值时记录日志。默认 10 秒。
- `log_queries_not_using_indexes` 未使用索引的查询也被记录到慢查询日志中（可选项）。
- `log_output` 日志存储方式。log_output='FILE'表示将日志存入文件，默认值是'FILE'。log_output='TABLE'表示将日志存入数据库，这样日志信息就会被写入到mysql.slow_log表中。MySQL数据库支持同时两种日志存储方式，配置的时候以逗号隔开即可，如：log_output='FILE,TABLE'。日志记录到系统的专用日志表中，要比记录到文件耗费更多的系统资源，因此对于需要启用慢查询日志，又需要能够获得更高的系统性能，那么建议优先记录到文件。

## 分析工具

Mysql 提供了慢查询日志的分析工具 mysqldumpslow，这要比自己查看日志文件要方便的多。

下面是几个常用的参数

- `-s` 是表示按照何种方式排序

```bash
c: 访问计数
l: 锁定时间
r: 返回记录
t: 查询时间
al:平均锁定时间
ar:平均返回记录数
at:平均查询时间
```

- `-t` 是top n的意思，即为返回前面多少条的数据
- `-g` 后边可以写一个正则匹配模式，大小写不敏感的

更多的参数可以查看帮助文档 `mysqldumpslow --help`

举个例子，查看记录最多的 10 个 sql

```bash
$ mysqldumpslow -s r -t 10
Can't find '/var/lib/mysql/*-slow.log'
```

如果我们自定义了日志文件，并且格式比较随意，那默认会报找不到文件的错误。

如果你的日志文件已经自定义为其它格式，那也可以通过传入文件名的方式分析

```bash
$ mysqldumpslow -s r -t 10 /var/lib/mysql/some-name.log
```

- [The Slow Query Log](https://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html)
- [mysqldumpslow — Summarize Slow Query Log Files](https://dev.mysql.com/doc/refman/5.7/en/mysqldumpslow.html)
