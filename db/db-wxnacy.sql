drop table if exists `blog`;
create table `blog`(
  id int(11) not null AUTO_INCREMENT,
  route VARCHAR(512) not null default '' COMMENT '路由地址',
  page_view int(11) not null default 0,
  ext JSON  DEFAULT null COMMENT '扩展字段',
  is_del tinyint(1) not null default 0 comment '是否删除',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`)
) engine=InnoDB default charset=utf8mb4 COMMENT '博客';

alter table `blog` add column name varchar(256) not null default '';

-- 2017.12.30
drop table if exists `user`;
create table `user`(
  id int(11) not null AUTO_INCREMENT,
  route VARCHAR(512) not null default '' COMMENT '路由地址',
  page_view int(11) not null default 0,
  ext JSON  DEFAULT null COMMENT '扩展字段',
  is_del tinyint(1) not null default 0 comment '是否删除',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`)
) engine=InnoDB default charset=utf8mb4 COMMENT '博客';

-- 2018-01-29
drop table if exists `code`;
create table `code`(
  id VARCHAR(32) not null ,
  name VARCHAR(128) not null default '' COMMENT '名字',
  description VARCHAR(128) not null default '' COMMENT '描述',
  type VARCHAR(32) not null default '' COMMENT '类型',
  code JSON  DEFAULT null COMMENT '代码',
  is_available tinyint(1) not null default 1 comment '是否有效',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`)
) engine=InnoDB default charset=utf8mb4 COMMENT '代码';
