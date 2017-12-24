---
title: Mysql 实现 Rank 排名查询
tags:
  - mysql
date: 2017-12-24 10:12:26
---


Mysql 中没有像 Oracle 中那样的 Rank 函数来实现查询的排名排序，但是我们可以用一
些基础查询语句来实现同样的效果。

<!-- more -->
先创建一个表来作为例子
```mysql
drop table if exists `post`;
create table `post`(
  id int(11) not null AUTO_INCREMENT,
  url VARCHAR(512) not null default '' COMMENT '地址',
  pv int(11) not null default 0 COMMENT '访问量',
  primary key(`id`)
) engine=InnoDB default charset=utf8mb4 COMMENT '博客';
INSERT INTO `post` (`url`, `pv`) VALUES
('/p/1', 22),
('/p/2', 21),
('/p/3', 50),
('/p/4', 5),
('/p/5', 15),
('/p/6', 23),
('/p/7', 45),
('/p/8', 35),
('/p/9', 20);
```
我们想要对 pv 字段进行倒序排名
```mysql
select @rank := @rank +1 as rank, url, pv from `post` p, (select @rank := 0) r order by pv desc;
```
如果你按照我上边的语句执行，你会得到如下的结果
```bash
1    /p/3    50
2    /p/7    45
3    /p/8    35
4    /p/6    23
5    /p/1    22
6    /p/2    21
7    /p/9    20
8    /p/5    15
9    /p/4    5
```
有结果来看，我们已经得到了想要的结果，下面我们来看看怎么实现的。

首先简单说下 Mysql 中的变量，需要以 `@` 开头，及 `@rank`，想要给变量赋值分两种。
SET 语句
```mysql
set @name = 'wxnacy';
select @name;
```
SELECT 语句
```mysql
select @name := 'wxnacy';
```
两者的区别在于 set 命令需要两条命令查询，select 命令中使用 `:=` 赋值
而 `@rank := @rank + 1` 就是在查询语句中达到自增的目的，也就变相的实现了 `rank` 函数。
