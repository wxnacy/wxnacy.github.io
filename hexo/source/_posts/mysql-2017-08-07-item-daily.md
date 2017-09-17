---
title: 2017-08-07 新建user和user_data表，完善`insert_commet_trigger`
date: 2017-08-07
tags: [mysql]
---

> 今天目标新建user、`user_data`表，并完善`insert_commet_trigger`，达到根据判断resource_type来更新video还是user_data的comment_count

专辑：[mysql每天练习](/?p=/doc/mysql/mysql_daily.md)
- 新建user表
```mysql
drop table if exists `user`;
create table `user`(
    id int(11) not null auto_increment,
    name varchar(32) not null comment '姓名',
    is_del int(1) not null default 0 comment '是否删除',
    create_ts timestamp not null default current_timestamp comment '创建时间',
    update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
    primary key(`id`)
)engine=InnoDB default charset=utf8mb4 comment '用户表';
```

- 新建user_data表
```mysql
drop table if exists `user_data`;
create table `user_data`(
    user_id int(11) not null,
    comment_count int(11) not null default 0 comment '评论数量',
    update_ts timestamp not null default current_timestamp on update current_timestamp comment '最后修改时间',
    primary key(`user_id`)
)engine=InnoDB default charset=utf8mb4 comment '用户数据表，记录用户额外数据';
```

- 重写 `insert_comment_trigger`
```mysql
drop trigger if exists `insert_comment`;
delimiter $
create trigger `insert_comment` after insert on comment for each row 
begin
    declare count int;
    if (new.resource_type = 'user') then
        select count(0) into count from user_data where user_id = new.resource_id;
        if (count > 0 ) then
            update user_data set comment_count = comment_count +1  where user_id = new.resource_id;
        else
            insert into user_data (user_id,comment_count) values (new.resource_id,1);
        end if;
    else
        update video set comment_count = comment_count +1 where id= new.resource_id;
    end if; 
end $
delimiter ;
```

- 执行相关语句
```mysql
insert into user(name) values ('wxnacy');
insert into comment (resource_id,resource_type,content) values (1,'user','好人');
insert into comment (resource_id,resource_type,content) values (1,'user','大好人');
select * from user_data;
```
执行语句后，user_data中comment_count应该等于2

