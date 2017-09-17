---
title: 2017-08-10 新建collection_resource表，新建trigger更新collection资源总数
date: 2017-08-10
tags: [mysql]
---

> 今天练习的目标，新建collection_resource表，并新建trigger更新collection的资源数

专辑：[mysql每天练习](/?p=/doc/mysql/mysql_daily.md)

## 新建collection_resource
```mysql
drop table if exists `collection_resource`;
CREATE TABLE `collection_resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `collection_id` int(11) NOT NULL,
  `resource_id` int(11) NOT NULL,
  `resource_type` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='合集资源对应表';
```
## collection表添加资源数量字段
```mysql
alter table collection add column resource_count int(11) not null default 0 comment '资源总数';
```
## 新建trigger
```mysql
drop trigger if exists `insert_collection_resource`;
delimiter $
create trigger `insert_collection_resource` after insert on collection_resource for each row 
begin
	declare count int;
	select count(0) into count from collection where id = new.collection_id;
	if (count > 0) then 
		update collection set resource_count = resource_count + 1 where id = new.collection_id;
	end if;
end $
delimiter ;
```
## 运行
```mysql
insert into collection(name) values ('合集');
insert into collection_resource (collection_id,resource_id,resource_type) values(1,1,'video');
select * from collection;
```

