# 基础命令

## 表结构
- 创建表
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

- 查看列 ``` desc table_name```
- 修改表名 ``` alter table table_name rename to new_name;```
- 添加列 ``` alter table table_name add column col_name varchar(11) not null ...;```
- 删除列 ``` alter table table_name drop column col_name;```
- 修改列名 ``` alter table table_name change old_name new_name int(11)...;```
- 修改列属性 ``` alter table table_name modify col_name int(11) not null...;```



