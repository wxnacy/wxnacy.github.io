---
title: Mysql REPLACE INTO 语法
tags:
  - mysql
date: 2018-03-26 21:29:36
---


Mysql 中插入数据的语法除了 `INSERT INTO`，还有一个 `REPLACE INTO` 语法，只不过该语法在没有插入数据时是插入，表中有时是替换，并且会更改主键 id
<!-- more -->
更改主键 id 这个设定，就决定了正常的业务程序是用不到这个语法的，一条数据老改 id 谁受得了。

但是换一种情况就会显得很有用，比如，你就是想要得到每次都变化的 id，举个例子
```mysql
DROP TABLE IF EXISTS `auto_id`;
CREATE TABLE `auto_id` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `max_id` bigint(20) NOT NULL DEFAULT 0 COMMENT '占位字段',
  `create_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `auto_max_id_uindex` (`max_id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COMMENT='自动生成 id';
```
新建一个表，我通过不断的插入相同的 `mac_id` 字段来获取自增的 id
```mysql
replace into auto_id(max_id) values (1);
select last_insert_id();    -- 1
replace into auto_id(max_id) values (1);
select last_insert_id();    -- 2
```
想要达到这样的效果需要一个条件，想要替换的数据字段需要设为唯一键
```mysql
UNIQUE KEY `auto_max_id_uindex` (`max_id`)
```

`REPLACE INTO` 一共三种写法分别为
```mysql
replace into auto_id(max_id) values (1);
replace into auto_id(max_id) select 1;
replace into auto_id set max_id = 1;
```

只是为了得到这个自增 id，多少有点脱裤子放屁，不过配合一些算法，我们可以根据表来得到对应的命名空间的 id，详见 [Mysql 自动生成 id 算法](Mysql 自动生成 id 算法)
