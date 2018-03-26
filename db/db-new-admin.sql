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
alter table `visitor_log` add column visit_date date not null default '2018-03-22' comment '';

-- 2018-03-23
drop table if exists `visitor_log_date`;
create table `visitor_log_date`(
  id bigint(20) not null AUTO_INCREMENT,
  visit_date DATE not null default '2001-01-01' COMMENT '日期',
  pv INT(11) not null default '0' COMMENT 'page views',
  uv INT(11) not null default '0' COMMENT 'user views',
  ext_property JSON  DEFAULT null COMMENT '扩展字段',
  is_available tinyint(1) not null default 1 comment '是否有效',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`),
  UNIQUE KEY `index_visitor_date` (`visit_date`, `is_available`)
) engine=InnoDB default charset=utf8mb4 COMMENT '每天的访问统计';

drop table if exists `article`;
create table `article`(
  id bigint(20) not null AUTO_INCREMENT,
  name VARCHAR(256) not null default '' COMMENT 'name',
  url VARCHAR(512) not null default '' COMMENT 'url',
  tag VARCHAR(128) not null default '' COMMENT 'tag',
  pv INT(11) not null default '0' COMMENT '访问量',
  init_pv INT(11) not null default '0' COMMENT '初始值访问量',
  publish_date DATE not null default '2001-01-01' COMMENT '发布时间',
  ext_property JSON  DEFAULT null COMMENT '扩展字段',
  is_available tinyint(1) not null default 1 comment '是否有效',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`),
  UNIQUE KEY `index_url` (`url`, `is_available`)
) engine=InnoDB default charset=utf8mb4 COMMENT '访问记录';

-- 2018-03-26
drop table if exists `nav`;
create table `nav`(
  id bigint(20) not null AUTO_INCREMENT,
  name VARCHAR(256) not null default '' COMMENT 'name',
  url VARCHAR(512) not null default '' COMMENT 'url',
  ext_property JSON  DEFAULT null COMMENT '扩展字段',
  is_available tinyint(1) not null default 1 comment '是否有效',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`)
) engine=InnoDB default charset=utf8mb4 COMMENT '导航栏';

drop table if exists `article_data`;
create table `article_data`(
  id bigint(20) not null AUTO_INCREMENT,
  article_id  bigint(20) not null comment '文章 id',
  visit_date DATE not null default '2001-01-01' COMMENT '日期',
  pv INT(11) not null default '0' COMMENT 'page views',
  uv INT(11) not null default '0' COMMENT 'user views',
  ext_property JSON  DEFAULT null COMMENT '扩展字段',
  is_available tinyint(1) not null default 1 comment '是否有效',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`),
  UNIQUE KEY `index_article_id_visitor_date` (`article_id`, `visit_date`, `is_available`)
) engine=InnoDB default charset=utf8mb4 COMMENT '文章数据';
