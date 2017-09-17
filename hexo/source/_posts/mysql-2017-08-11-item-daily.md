---
title: 2017-08-11 新建用户行为表，新建trigger完成用户总分数更新
date: 2017-08-11
tags: [mysql]
---

> 今天练习新建用户行为表user_event，并新建trigger做到更新用户总分数

## 新建user_event
```mysql
drop table if exists `user_event`;
create table `user_event`(
	id int(11) not null auto_increment,
	user_id int(11) not null comment '用户id',
	type varchar(32) not null comment '行为类型',
	resource_id int(11) not null default 0 comment '资源id',
	resource_type varchar(32) not null default '' comment '资源类型',
	val_num int(11) not null default 0 comment '备用int值',
	val_str varchar(512) not null default '' comment '备用str值',
	ext JSON default null comment '扩展',
	is_del tinyint(1) not null default 0 comment '是否删除',
	create_ts timestamp not null default current_timestamp comment '创建时间',
	update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
	primary key(`id`)
)engine=InnoDB default charset=utf8mb4 comment '用户行为表';
```

## 用户表添加总分数和等级字段
```mysql
alter table user add column rank int(11) not null default 0 comment '排行';
alter table user add column score int(11) not null default 0 comment '积分';
```

## 新建trigger
```mysql
drop trigger if exists `insert_user_event`;
delimiter $
create trigger `insert_user_event` after insert on `user_event` for each row 
begin
	declare total_score int;
	if (new.type = 'get_score') then
		select sum(val_num) into total_score from user_event where user_id = new.user_id and type  = 'get_score';
		update user set score = total_score where id = new.user_id;
	end if;
end $
delimiter ;
```

## 运行
```mysql
insert into user_event (user_id,type,val_num) values (1,'get_score',200);
insert into user_event (user_id,type,val_num) values (1,'get_score',200);
select * from user where id = 1;
```
运行后user中score应该等于400

