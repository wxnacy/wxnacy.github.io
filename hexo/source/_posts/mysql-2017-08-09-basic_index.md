---
title: Mysql 索引的增删查
date: 2017-08-09
tags: [mysql]
---

原文：[http://www.cnblogs.com/tianhuilove/archive/2011/09/05/2167795.html](http://www.cnblogs.com/tianhuilove/archive/2011/09/05/2167795.html)

<!-- more --><!-- toc -->
## 索引类型
在创建索引时，可以规定索引能否包含重复值。如果不包含，则索引应该创建为PRIMARY KEY或UNIQUE索引。对于单列惟一性索引，这保证单列不包含重复的值。对于多列惟一性索引，保证多个值的组合不重复。 PRIMARY KEY索引和UNIQUE索引非常类似。事实上，PRIMARY KEY索引仅是一个具有名称PRIMARY的UNIQUE索引。这表示一个表只能包含一个PRIMARY KEY，因为一个表中不可能具有两个同名的索引。下面的SQL语句对students表在sid上添加PRIMARY KEY索引。

## 创建索引
在执行CREATE TABLE语句时可以创建索引，也可以单独用CREATE INDEX或ALTER TABLE来为表增加索引。

### alter table

其中table_name是要增加索引的表名，column_list指出对哪些列进行索引，多列时各列之间用逗号分隔。索引名index_name可选，缺省时，MySQL将根据第一个索引列赋一个名称。另外，ALTER TABLE允许在单个语句中更改多个表，因此可以在同时创建多个索引。
```mysql
alter table table_name add index index_name (column_list);
alter table table_name add unique index_name (column_list);
alter table table_name add primary key (column_list);
```
### create table
CREATE INDEX可对表增加普通索引或UNIQUE索引。
```mysql
create index index_name on table_name (column_list);
create unique index index_name on table_name (column_list);
```

## 删除索引
可利用ALTER TABLE或DROP INDEX语句来删除索引。类似于CREATE INDEX语句，DROP INDEX可以在ALTER TABLE内部作为一条语句处理，语法如下。
```mysql
drop index index_name on table_name;
alter table_name drop index index_name;
alter table_name drop primary key;
```
```
其中，前两条语句是等价的，删除掉table_name中的索引index_name。
第3条语句只在删除PRIMARY KEY索引时使用，因为一个表只可能有一个PRIMARY KEY索引，因此不需要指定索引名。
如果没有创建PRIMARY KEY索引，但表具有一个或多个UNIQUE索引，则MySQL将删除第一个UNIQUE索引。
如果从表中删除了某列，则索引会受到影响。对于多列组合的索引
如果删除其中的某列，则该列也会从索引中删除。如果删除组成索引的所有列，则整个索引将被删除。
```

## 查看索引

```mysql
show index from table_name;
show keys from table_name;
```

- **Table**: 表的名称。
- **Non_unique**: 如果索引不能包括重复词，则为0。如果可以，则为1。
- **Key_name**: 索引的名称。
- **Seq_in_index**: 索引中的列序列号，从1开始。
- **Column_name**: 列名称。
- **Collation**: 列以什么方式存储在索引中。在MySQL中，有值‘A’（升序）或NULL（无分类）。
- **Cardinality**: 索引中唯一值的数目的估计值。通过运行ANALYZE TABLE或myisamchk -a可以更新。基数根据被存储为整数的统计数据来计数，所以即使对于小型表，该值也没有必要是精确的。基数越大，当进行联合时，MySQL使用该索引的机会就越大。
- **Sub_part**: 如果列只是被部分地编入索引，则为被编入索引的字符的数目。如果整列被编入索引，则为NULL。
- **Packed**: 指示关键字如何被压缩。如果没有被压缩，则为NULL。
- **Null**: 如果列含有NULL，则含有YES。如果没有，则该列含有NO。
- **Index_type**: 用过的索引方法（BTREE, FULLTEXT, HASH, RTREE）。
- **Comment**: 备注

