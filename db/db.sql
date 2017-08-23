drop table if exists `visit_user`;
create table `visit_user`(
  id int(11) not null AUTO_INCREMENT,
  ip VARCHAR(32) not null COMMENT '访问ip',
  user_agent VARCHAR(1024) not null DEFAULT '' COMMENT '访问ua',
  md5 varchar(32) not null default '' comment '生成新访问用户的唯一标示，跟ip和user_agent生成',
  ext JSON  DEFAULT null COMMENT '扩展字段',
  is_del tinyint(1) not null default 0 comment '是否删除',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`)
) engine=InnoDB default charset=utf8mb4 COMMENT '访问用户';



drop table if exists `visit_log`;
create table `visit_log`(
  id int(11) not null auto_increment,
  visit_user_id int(11) not null comment '访问用户id',
  method varchar(10) not null comment '访问方式',
  url varchar(1024) not null default '' comment '访问地址',
  referrer varchar(1024) not null default '' comment '来源地址',
  ext JSON comment '扩展',
  is_del tinyint(1) not null default 0 comment '是否删除',
  create_ts timestamp not null default current_timestamp comment '创建时间',
  update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
  primary key(`id`)
) engine=InnoDB default charset=utf8mb4 comment '访问日志表';

drop table if exists `crawler`;
create table `crawler`(
	id int(11) not null auto_increment,
	url varchar(512) not null comment '地址',
	ext JSON null comment '扩展',
	is_del tinyint(1) not null default 0 comment '是否删除',
	create_ts timestamp not null default current_timestamp comment '创建时间',
	update_ts timestamp not null default current_timestamp on update current_timestamp comment '修改时间',
	primary key(`id`)
)engine=InnoDB default charset=utf8mb4 comment '爬虫表';