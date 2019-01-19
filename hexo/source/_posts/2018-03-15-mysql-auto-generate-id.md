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

