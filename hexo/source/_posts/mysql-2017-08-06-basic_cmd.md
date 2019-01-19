---
title: Mysql 基础命令
date: 2017-08-06
tags: [mysql]
---

整理 Mysql 的一些基础命令以便查阅

<!-- more --><!-- toc -->
## 数据库
###  创建库
```mysql
create database name character utf8mb4;
```
## 表结构
### 创建表
```mysql
drop table if exists `user`;
create table `user`(
    id int(11) not null auto_increment,
    name varchar(32) not null comment '姓名',
    mobile varchar(11) not null default '' comment '手机号',
    ext JSON default null comment '扩展信息',
    create_ts timestamp not null default current_timestamp comment '创建时间',
    update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
    primary key(`id`)
) engine=InnoDB default charset=utf8mb4 comment '用户表';
```

### 查看列
```mysql
desc table_name
```
### 修改表名
```mysql
alter table table_name rename to new_name;
```
### 添加列
```mysql
alter table table_name add column col_name varchar(11) not null ...;
```
### 删除列
```mysql
alter table table_name drop column col_name;
```
### 修改列名
```mysql
alter table table_name change old_name new_name int(11)...;
```
### 修改列属性
```mysql
alter table table_name modify col_name int(11) not null...;
```
### 查看列属性
```mysql
show columns from table_name;
show full columns from table_name; # 全部信息
```

- **Field** ：字段名
- **Type**：字段类型
- **Collation**：字符集（mysql 5.0以上有）
- **Null** ：是否可以为NULL
- **Key**：索引（PRI,unique,index)
- **Default**：缺省值
- **Extra**：额外（是否 auto_increment)
- **Privileges**：权限
- **Comment**：备注（mysql 5.0以上有)

## 查询

### 去掉重复数据
```mysql
select distinct name from user;
```
需要注意亮点，第一，`distinct` 必须放到查询字段最前边。第二，如果查询的字段很多，必须所有字段都相同才会过滤

