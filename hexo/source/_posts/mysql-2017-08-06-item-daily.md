---
title: 2017-08-06 新建video和comment表，以及`insert_commet_trigger`
date: 2017-08-06
tags: [mysql]
---

> 今天的目标是新建一个video视频表和comment评论表，并编写trigger，达到当insert一条评论类型为video的数据到comment中时，video中comment_count字段可以自加一

专辑：[mysql每天练习](/?p=/doc/mysql/mysql_daily.md)
- 新建video表
```mysql
drop table if exists `video`;
create table `video`(
    id int(11) not null auto_increment,
    name varchar(32) not null comment '标题',
    url varchar(512) not null comment '视频地址',
    is_del int(1) not null default 0 comment '是否删除',
    create_ts timestamp not null default current_timestamp comment '创建时间',
    update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
    primary key(`id`)
)engine=InnoDB default charset=utf8mb4 comment '视频表';
```

- 添加comment_count字段（不是忘了，就是想练一下add column语句╭(╯^╰)╮）
```mysql
alter table video add column comment_count int(11) not null default 0 comment '评论数量';
```

- 新建comment表
```mysql
drop table if exists `comment`;
create table `comment`(
    id int(11) not null auto_increment,
    resource_id int(11) not null comment '被评论资源id',
    resource_type varchar(16) not null comment '被评论资源类型',
    content varchar(1024) not null comment '评论内容',
    is_del int(1) not null default 0 comment '是否删除',
    create_ts timestamp not null default current_timestamp comment '创建时间',
    update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
    primary key(`id`)
)engine=InnoDB default charset=utf8mb4 comment '评论表';
```
- 新建trigger
```mysql
drop trigger if exists `insert_comment`;
delimiter $
create trigger `insert_comment` after insert on comment for each row
begin
    if (new.resource_type = 'video') then 
        update video set comment_count = comment_count +1 where id = new.resource_id;
    end if;
end $
delimiter ;
```

- 执行相应操作语句

```mysql
insert into video (name,url) values ('蜘蛛侠：返校季','http://woyemeiyou/wangzhi.mp4');
insert into comment (resource_id,resource_type,content) values (1,'video','找不到资源');
select * from video;
```

最后结果中video表中的comment_count应该等于1

