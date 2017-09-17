---
title: 2017-08-12 新建等级表，完善`insert_user_event`
date: 2017-08-12
tags: [mysql]
---

> 今天练习目标，新建等级表，完善`insert_user_event`做到自动更新用户总积分和当前等级

## 新建等级表
```mysql
drop table if exists `rank`;
create table `rank`(
	id int(11) not null auto_increment,
	rank int(11) not null default 0 comment '等级',
	name varchar(32) not null  comment '等级名',
	score int(11) not null comment '等级所需值',
	primary key(`id`)
)engine=InnoDB default charset=utf8mb4 comment '登记表';
```

## 插入数据
```mysql
insert into rank (rank,name,score) values (1,'等级1',0);
insert into rank (rank,name,score) values (2,'等级2',200);
insert into rank (rank,name,score) values (3,'等级3',500);
insert into rank (rank,name,score) values (4,'等级4',1000);
insert into rank (rank,name,score) values (5,'等级5',2000);
insert into rank (rank,name,score) values (6,'等级6',5000);
insert into rank (rank,name,score) values (7,'等级7',10000);
insert into rank (rank,name,score) values (8,'等级8',20000);
```

## 重写trigger
```mysql
drop trigger if exists `insert_user_event`;
DELIMITER $
create trigger `insert_user_event` after insert on user_event for each row  
begin
	declare total_score int;
	declare rank_val int;
	if (new.type = 'get_score') then
		select sum(val_num) into total_score from user_event where user_id = new.user_id and type = 'get_score' and is_del = 0;
		select rank into rank_val  from rank where score <= total_score order by score desc limit 1;
		update user set rank = rank_val , score = total_score where id = new.user_id;
		
	end if;
end $
DELIMITER ;

```

## 运行
```mysql
update user set rank = 0 , score = 0 where id = 1;
update user_event set is_del = 1 where user_id = 1 and type = 'get_score';
insert into user_event (user_id,type,val_num) values (1,'get_score',501);
select * from user where id = 1;

```

运行后，用户rank=1 score=501

