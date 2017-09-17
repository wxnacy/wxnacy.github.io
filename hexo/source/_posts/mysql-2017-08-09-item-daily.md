---
title: 2017-08-09 新建collection合集表，新建trigger完成更新用户文章数
date: 2017-08-09
tags: [mysql]
---

> 今天练习新建collection合集表，并在article中添加user_id字段，在user_data中添加article_count字段，并新建trigger ```insert_article```完成用户文章数自动更新

专辑：[mysql每天练习](/?p=/doc/mysql/mysql_daily.md)


- 新建collection
```mysql
drop table if exists `collection`;
create table `collection`(
	id int(11) not null auto_increment,
	name varchar(256) not null default '' comment '合集名称',
	is_del tinyint(1) not null default 0 comment '是否删除',
	create_ts timestamp not null default current_timestamp comment '创建时间',
	update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
	primary key(`id`)
)engine=InnoDB default charset=utf8mb4 comment '合集表';
```
- article添加user_id
```mysql
alter table article add column user_id int(11) not null default 0 comment '用户id';
```
- ```user_data``` 中添加```article_count```字段
```mysql
alter table user_data add column article_count int(11) not null default 0 comment '发布文章数量';
```
- 新建trigger
```mysql
drop trigger if exists `insert_article`;
delimiter $
create trigger `insert_article` after insert on article for each row 
begin
	declare count int;
	if (new.user_id > 0) then
		select count(0) into count from user_data where user_id = new.user_id;
		if (count > 0) then
			update user_data set article_count = article_count +1 where user_id = new.user_id;
		else
			insert into user_data (user_id,article_count) values (new.user_id,1);
		end if;
	end if;
end $
delimiter ;
```
- 运行
```mysql
insert into article (name,url,user_id) values ('title','http://baidu.com',3);
insert into article (name,url,user_id) values ('title','http://baidu.com',3);
select * from user_data where user_id = 3;
```
运行后，article_count应该等于2

