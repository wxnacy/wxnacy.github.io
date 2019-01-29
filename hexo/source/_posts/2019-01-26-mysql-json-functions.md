---
title: Mysql 查询 JSON 结果的相关函数
date: 2019-01-26 17:25:23
tags: [mysql]
---

JSON 格式字段是 Mysql 5.7 新加的属性，不够它本质上以字符串性质保存在库中的，刚接触时我只了解 `$.xx` 查询字段的方法，因为大部分时间，有这个就够了，其他交给程序就行了，但是最近一些操作需要更复杂的查询操作，所以赶紧了解下更多的方法。

<!-- more --><!-- toc -->

## JSON_EXTRACT(json_doc [,path])

查询字段


```mysql
mysql> set @j = '{"name":"wxnacy"}';
mysql> select JSON_EXTRACT(@j, '$.name');
+----------------------------+
| JSON_EXTRACT(@j, '$.name') |
+----------------------------+
| "wxnacy"                   |
+----------------------------+
```

还有一种更简洁的方式，但是只能在查询表时使用

```mysql
mysql> select ext -> '$.name' from test;
+-----------------+
| ext -> '$.name' |
+-----------------+
| "wxnacy"        |
+-----------------+
```

在 `$.` 后可以正常的使用 JSON 格式获取数据方式，比如数组

```mysql
mysql> set @j = '{"a": [1, 2]}';
mysql> select JSON_EXTRACT(@j, '$.a[0]');
+----------------------------+
| JSON_EXTRACT(@j, '$.a[0]') |
+----------------------------+
| 1                          |
+----------------------------+
```

## JSON_DEPTH(json_doc)

计算 JSON 深度，计算方式 `{} []` 有一个符号即为一层，符号下有数据增加一层，复杂 JSON 算到最深的一次为止，官方文档说 `null` 值深度为 0，但是实际效果并非如此，列举几个例子

![json_depth](http://wxnacy-img.oss-cn-beijing.aliyuncs.com/blog/json_depth_360.png)

## JSON_LENGTH(json_doc [, path])

计算 JSON 最外层或者指定 path 的长度，标量的长度为1。数组的长度是数组元素的数量，对象的长度是对象成员的数量。

```mysql
mysql> SELECT JSON_LENGTH('[1, 2, {"a": 3}]');
+---------------------------------+
| JSON_LENGTH('[1, 2, {"a": 3}]') |
+---------------------------------+
|                               3 |
+---------------------------------+
mysql> SELECT JSON_LENGTH('{"a": 1, "b": {"c": 30}}');
+-----------------------------------------+
| JSON_LENGTH('{"a": 1, "b": {"c": 30}}') |
+-----------------------------------------+
|                                       2 |
+-----------------------------------------+
mysql> SELECT JSON_LENGTH('{"a": 1, "b": {"c": 30}}', '$.b');
+------------------------------------------------+
| JSON_LENGTH('{"a": 1, "b": {"c": 30}}', '$.b') |
+------------------------------------------------+
|                                              1 |
+------------------------------------------------+
```

## JSON_TYPE(json_doc)

返回一个utf8mb4字符串，指示JSON值的类型。 这可以是对象，数组或标量类型，如下所示：

```mysql
mysql> SET @j = '{"a": [10, true]}';
mysql> SELECT JSON_TYPE(@j);
+---------------+
| JSON_TYPE(@j) |
+---------------+
| OBJECT        |
+---------------+
mysql> SELECT JSON_TYPE(JSON_EXTRACT(@j, '$.a'));
+------------------------------------+
| JSON_TYPE(JSON_EXTRACT(@j, '$.a')) |
+------------------------------------+
| ARRAY                              |
+------------------------------------+
mysql> SELECT JSON_TYPE(JSON_EXTRACT(@j, '$.a[0]'));
+---------------------------------------+
| JSON_TYPE(JSON_EXTRACT(@j, '$.a[0]')) |
+---------------------------------------+
| INTEGER                               |
+---------------------------------------+
mysql> SELECT JSON_TYPE(JSON_EXTRACT(@j, '$.a[1]'));
+---------------------------------------+
| JSON_TYPE(JSON_EXTRACT(@j, '$.a[1]')) |
+---------------------------------------+
| BOOLEAN                               |
+---------------------------------------+
```

可能的返回类型

- 纯JSON类型：
  - OBJECT：JSON对象
  - ARRAY：JSON数组
  - BOOLEAN：JSON真假文字
  - NULL：JSON null文字
- 数字类型：
  - INTEGER：MySQL TINYINT，SMALLINT，MEDIUMINT以及INT和BIGINT标量
  - DOUBLE：MySQL DOUBLE FLOAT标量
  - DECIMAL：MySQL DECIMAL和NUMERIC标量
- 时间类型：
  - DATETIME：MySQL DATETIME和TIMESTAMP标量
  - 日期：MySQL DATE标量
  - TIME：MySQL TIME标量
- 字符串类型：
  - STRING：MySQL utf8字符类型标量：CHAR，VARCHAR，TEXT，ENUM和SET
- 二进制类型：
  - BLOB：MySQL二进制类型标量，包括BINARY，VARBINARY，BLOB和BIT
所有其他类型：
OPAQUE（原始位）

## JSON_VALID

返回0或1以指示值是否为有效JSON。 如果参数为NULL，则返回NULL。

```mysql
mysql> SELECT JSON_VALID('{"a": 1}');
+------------------------+
| JSON_VALID('{"a": 1}') |
+------------------------+
|                      1 |
+------------------------+
mysql> SELECT JSON_VALID('hello'), JSON_VALID('"hello"');
+---------------------+-----------------------+
| JSON_VALID('hello') | JSON_VALID('"hello"') |
+---------------------+-----------------------+
|                   0 |                     1 |
+---------------------+-----------------------+
```

- [Functions That Return JSON Value Attributes](https://dev.mysql.com/doc/refman/8.0/en/json-attribute-functions.html)
