---
title: Mysql 插入表情
tags:
  - mysql
date: 2018-07-02 10:08:12
---


Mysql 建表时，默认 `varchar` 字段是不能保存表情符号的，会报编码错误。
<!-- more --><!-- toc -->
修改下表和字段的编码即可

```mysql
> ALTER TABLE wxnacy CHARSET=utf8mb4;
> ALTER TABLE wxnacy MODIFY name VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL default '';
```
