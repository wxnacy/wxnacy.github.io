---
title: 2017-08-08 新建article表，完善`insert_comment_trigger`
date: 2017-08-08
tags: [mysql]
---

> 今天目标创建acticle表，并完善`insert_comment_trigger`，以支持更新article中的comment_count,comment表新增comment_id字段

专辑：[mysql每天练习](/?p=/doc/mysql/mysql_daily.md)
- 新建article
```mysql
drop table if exists `article`;
create table `article`(
	id int(11) not null auto_increment,
	name varchar(32) not null comment '标题',
	url varchar(512) not null comment '地址',
	comment_count int(11) not null default 0 comment '评论数量',
	is_del tinyint(1) not null default 0 comment '是否删除',
	create_ts timestamp not null default current_timestamp comment '创建时间',
	update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
	primary key(`id`)
)engine=InnoDB default charset=utf8mb4 comment '文章表';
```
- 修改`insert_comment`
```mysql
drop trigger if exists `insert_comment`;
delimiter $
create trigger `insert_comment` after insert on comment for each row 
begin
	declare count int;
	if (new.resource_type = 'video') then
		update video set comment_count = comment_count + 1 where id  = new.resource_id;
	elseif (new.resource_type = 'article') then
		update article set comment_count = comment_count + 1 where id = new.resource_id;
	elseif (new.resource_type = 'user') then
		select count(0) into count from user_data where user_id = new.resource_id;
		if (count >0) then
			update user_data set comment_count = comment_count + 1 where user_id = new.resource_id;
		else
			insert into user_data (user_id,comment_count) values (new.resource_id,1);
		end if;
	end if;
end $
delimiter ;
```
- 添加字段
```mysql
alter table comment add column comment_id int(11) not null default 0 comment '回复的评论注解id';
```
- 测试
```mysql
insert into article (name,url) values ('好文章','http://wen.com/wen.html');
insert into comment(resource_id,resource_type,content) values(1,'article','好文章');
select * from article;
```
执行完后，article中comment_count应该等于1

