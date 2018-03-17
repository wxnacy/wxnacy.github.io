---
title: Mysql 自动生成 id 算法
tags:
  - mysql
date: 2018-03-15 17:27:51
---


本章介绍一种 Mysql 生成 id 的算法，主要用于某些特定数据表，希望有统一的 id 空间，但不是简单的自增
<!-- more --><!-- toc -->
需求是 id 为数值型，可以在 js 环境中安全的使用，每个表有独立的 id 空间，并且全局唯一

思路是这样的

为了在 js 中安全使用，长度最大为 52 位，所以分为区域位（8位）、表位（8位）、id 长度（36位）

为了生成效率直接在 Mysql 自定义方法，首先建立一个表来作为目标表的 id 生成器，利用 `replace INTO` 方法在达到生成自增 id 的目的，然后根据表名判断位移长度计算出最终 id，完整代码如下

```mysql
DROP TABLE IF EXISTS `auto_user_id`;
CREATE TABLE `auto_user_id` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `max_id` bigint(20) NOT NULL DEFAULT 0 COMMENT '占位字段',
  `create_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `auto_max_id_uindex` (`max_id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COMMENT='自动生成 id';

DROP TABLE IF EXISTS `auto_article_id`;
CREATE TABLE `auto_article_id` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `max_id` bigint(20) NOT NULL DEFAULT 0 COMMENT '占位字段',
  `create_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `auto_max_id_uindex` (`max_id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COMMENT='自动生成 id';

DROP TABLE IF EXISTS `auto_id`;
CREATE TABLE `auto_id` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `max_id` bigint(20) NOT NULL DEFAULT 0 COMMENT '占位字段',
  `create_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `auto_max_id_uindex` (`max_id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COMMENT='自动生成 id';

DROP FUNCTION IF EXISTS `func_gen_auto_id`;
DELIMITER $$
CREATE FUNCTION `func_gen_auto_id`(shard_seed BIGINT, item_name VARCHAR(10)) RETURNS BIGINT(20)
BEGIN
    DECLARE shard_offset    INT;
    DECLARE item_offset     INT;
    DECLARE item_seed       INT;

    DECLARE final_id        BIGINT;
    DECLARE shard_id        BIGINT;
    DECLARE item_type       BIGINT;
    DECLARE last_insert_id  BIGINT;

    SET shard_offset = 44;
    SET item_offset  = 36;

    CASE item_name
        WHEN 'user'         THEN SET item_seed = 1;
        WHEN 'article'      THEN SET item_seed = 2;
        ELSE                     SET item_seed = 0;
    END CASE;

    SET shard_id  = (SELECT shard_seed << shard_offset);
    SET item_type = (SELECT item_seed  << item_offset);

    CASE item_name
        WHEN 'user'         THEN replace INTO auto_user_id      (`max_id`) VALUES (1);
        WHEN 'article'      THEN replace INTO auto_article_id   (`max_id`) VALUES (1);
        ELSE                     replace INTO auto_id           (`max_id`) VALUES (1);
    END CASE;

    SET last_insert_id = (SELECT last_insert_id());

    SET final_id = (SELECT shard_id + item_type + last_insert_id);
    RETURN final_id;
END $$
DELIMITER ;
```

最后直接查询即可得到最终 id
```mysql
select func_gen_auto_id(1, 'user');
```

## 更好的写法

上边的写法可以完成任务，但是存在问题，第一如果需要生成多个空间的 id，需要手动创建很多“占位表”，第二没有充分利用空间，当 item 相同时，shard 的变化并没有重新生成 id 空间，会导致 id 浪费

对于 `auto_id` 可以稍加改动，`max_id` 改成 `shard_id, item_id` 两个字段，并建立联合索引，这样两个值任意变化都会从 0 重新开始自增 id

在方法调用时，第二个参数直接改为 int 值，这样就不在需要创建这么多的 `auto_id` 表

```bash
DROP TABLE IF EXISTS `auto_id`;
CREATE TABLE `auto_id` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `shard_id` int(11) NOT NULL DEFAULT '0' COMMENT '占位字段',
  `item_id` int(11) NOT NULL DEFAULT '0' COMMENT '占位字段',
  `create_ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `auto_shard_item_id_uindex` (`shard_id`, `item_id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COMMENT='自动生成 id';

DROP FUNCTION IF EXISTS `func_auto_id`;
DELIMITER $$
CREATE FUNCTION `func_auto_id`(shard_seed INT, item_seed INT) RETURNS BIGINT(20)
BEGIN
    DECLARE shard_offset    INT;
    DECLARE item_offset     INT;
    DECLARE final_id        BIGINT;
    DECLARE shard_id        BIGINT;
    DECLARE item_type       BIGINT;
    DECLARE last_insert_id  BIGINT;

    SET shard_offset = 44;
    SET item_offset  = 36;

    SET shard_id  = (SELECT shard_seed << shard_offset);
    SET item_type = (SELECT item_seed  << item_offset);


    replace INTO auto_id  (`shard_id`, `item_id`) VALUES (shard_seed, item_seed);
    SET last_insert_id = (SELECT last_insert_id());
    SET final_id = (SELECT shard_id + item_type + last_insert_id);
    RETURN final_id;
END $$
DELIMITER ;
```
这样第二个参数直接传入 int 型即可
```bash
select func_auto_id(1, 1);
```
