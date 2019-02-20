---
title: Mysql 复制表的几种方式
tags:
  - mysql
date: 2018-04-04 10:10:56
---


介绍几种复制表的方式

<!-- more --><!-- toc -->
首先创建一个表
```mysql
DROP TABLE IF EXISTS `user` ;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL COMMENT '标题',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='视频表';
insert into `user` (name) values ('wxnacy');
insert into `user` (name) values ('win');
```
## CREATE ... SELECT ...
使用语句
```mysql
mysql> CREATE TABLE `user2` SELECT * FROM user;
mysql> SHOW CREATE TABLE `user2`;

CREATE TABLE `user2` (
  `id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(32) CHARACTER SET utf8mb4 NOT NULL COMMENT '标题'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
可以拷贝表结构，并复制数据，然后索引等信息却无法复制，所以并不推荐

## SHOW CREATE TABLE
查询建表结构
```mysql
mysql> show create table `user`\G;
  Table: user
  Create Table: CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL COMMENT '标题' default 'win',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COMMENT='视频表';
```
复制建表信息并执行
```mysql
mysql> CREATE TABLE `user2` (
   ->  `id` int(11) NOT NULL AUTO_INCREMENT,
   ->  `name` varchar(32) NOT NULL COMMENT '标题' default 'win',
   ->  PRIMARY KEY (`id`),
   ->  UNIQUE KEY `index_name` (`name`)
   ->) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='视频表';
```
随后复制数据
```mysql
mysql> insert into `user2` select * from `user`;
```
这样可以完全复制表结构和数据，但是却不方便

## CREATE ... LIKE
使用该语句可以方便的完全复制表结构
```mysql
mysql> create table `user2` like `user`;
```
复制数据
```mysql
mysql> insert into `user2` select * from `user`;
```
