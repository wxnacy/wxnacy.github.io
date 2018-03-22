drop table if exists `user`;
create table `user`(
  id bigint(20) not null AUTO_INCREMENT,
  name VARCHAR(32) not null default '' COMMENT '姓名',
  email VARCHAR(32) not null default '' COMMENT '邮箱',
  mobile VARCHAR(32) not null default '' COMMENT '手机号',
  password VARCHAR(64) not null default '' COMMENT '密码',
  status VARCHAR(32) not null default '' COMMENT '状态',
  type VARCHAR(32) not null default '' COMMENT '类型',
  ext_property JSON  DEFAULT null COMMENT '扩展字段',
  is_available tinyint(1) not null default 1 comment '是否有效',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`),
  UNIQUE KEY `index_email` (`email`, `is_available`),
  UNIQUE KEY `index_name` (`name`, `is_available`),
  UNIQUE KEY `index_mobile` (`mobile`, `is_available`)
) engine=InnoDB default charset=utf8mb4 COMMENT '用户';

drop table if exists `visitor_log`;
create table `visitor_log`(
  id bigint(20) not null AUTO_INCREMENT,
  ip VARCHAR(64) not null default '' COMMENT 'ip',
  url VARCHAR(512) not null default '' COMMENT 'url',
  referrer VARCHAR(512) not null default '' COMMENT 'referrer',
  user_agent VARCHAR(1024) not null default '' COMMENT 'ua',
  ext_property JSON  DEFAULT null COMMENT '扩展字段',
  is_available tinyint(1) not null default 1 comment '是否有效',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`)
) engine=InnoDB default charset=utf8mb4 COMMENT '访问记录';

alter table `visitor_log` add column browser varchar(32) not null default '' comment '浏览器';
alter table `visitor_log` add column os varchar(64) not null default '' comment '系统';
alter table `visitor_log` add column device varchar(64) not null default '' comment '设备';
alter table `visitor_log` add column device_type varchar(64) not null default '' comment '设备类型 mobile pc tablet';
alter table `visitor_log` add column is_bot tinyint(1) not null default '0' comment '是否为机器人';
alter table `visitor_log` add column md5 varchar(64) not null default '' comment 'md5';
