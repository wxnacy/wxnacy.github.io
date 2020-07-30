---
title: Mysql 实现字段拼接的几个函数
date: 2020-07-30 11:59:31
tags: [mysql]
---

给运营导出数据时，难免需要对字段进行拼接，如果 Mysql 可以完成的话，就可以少些很多代码。

<!-- more -->
<!-- toc -->

Mysql 确实有几个函数可以对字段进行拼接。

## concat()

将多个字段使用空字符串拼接为一个字段

```mysql
mysql> select concat(id, type) from mm_content limit 10;
+------------------+
| concat(id, type) |
+------------------+
| 100818image      |
| 100824image      |
| 100825video      |
| 100826video      |
| 100827video      |
| 100828video      |
| 100829video      |
| 100830video      |
| 100831video      |
| 100832video      |
+------------------+
10 rows in set (0.00 sec)
```

不过如果有字段值为 NULL，则结果为 NULL。

```mysql
mysql> select concat(id, type, tags) from mm_content limit 10;
+------------------------+
| concat(id, type, tags) |
+------------------------+
| NULL                   |
| NULL                   |
| NULL                   |
| NULL                   |
| NULL                   |
| NULL                   |
| NULL                   |
| NULL                   |
| NULL                   |
| NULL                   |
+------------------------+
10 rows in set (0.00 sec)
```

## concat_ws()

上面这种方式如果想要使用分隔符分割，就需要每个字段中间插一个字符串，非常麻烦。

`concat_ws()` 可以一次性的解决分隔符的问题，并且不会因为某个值为 NUll，而全部为 NUll。

```mysql
mysql> select concat_ws(' ', id, type, tags) from mm_content limit 10;
+--------------------------------+
| concat_ws(' ', id, type, tags) |
+--------------------------------+
| 100818 image                   |
| 100824 image                   |
| 100825 video                   |
| 100826 video                   |
| 100827 video                   |
| 100828 video                   |
| 100829 video                   |
| 100830 video                   |
| 100831 video                   |
| 100832 video                   |
+--------------------------------+
10 rows in set (0.00 sec)
```

## group_concat()

最后一个厉害了，正常情况下一个语句写成这样一定会报错的。

```mysql
mysql> select id from test_user group by age;
ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'test_user.id' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
```

但是 `group_concat()` 可以将分组状态下的其他字段拼接成字符串查询出来

```mysql
mysql> select group_concat(name) from test_user group by age;
+--------------------+
| group_concat(name) |
+--------------------+
| wen,ning           |
| wxnacy,win         |
+--------------------+
2 rows in set (0.00 sec)
```

默认使用逗号分隔，我们也可以指定分隔符

```mysql
mysql> select group_concat(name separator ' ') from test_user group by age;
+----------------------------------+
| group_concat(name separator ' ') |
+----------------------------------+
| wen ning                         |
| wxnacy win                       |
+----------------------------------+
2 rows in set (0.00 sec)
```

将字符串按照某个顺序排列

```mysql
mysql> select group_concat(name order by id desc separator ' ') from test_user group by age;
+---------------------------------------------------+
| group_concat(name order by id desc separator ' ') |
+---------------------------------------------------+
| ning wen                                          |
| win wxnacy                                        |
+---------------------------------------------------+
2 rows in set (0.00 sec)
```

如果想要拼接多个字段，默认是用空字符串进行拼接的，我们可以利用 `concat_ws()` 方法嵌套一层

```mysql
mysql> select group_concat(concat_ws(',', id, name) separator ' ') from test_user group by age;
+------------------------------------------------------+
| group_concat(concat_ws(',', id, name) separator ' ') |
+------------------------------------------------------+
| 1,wen 2,ning                                         |
| 3,wxnacy 4,win                                       |
+------------------------------------------------------+
2 rows in set (0.00 sec)
```

