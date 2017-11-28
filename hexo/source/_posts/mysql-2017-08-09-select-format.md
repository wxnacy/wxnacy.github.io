---
title: mysql select 格式化输出
date: 2017-08-09
tags: [mysql]
---

## 使用\G输出结果按行垂直显示结果
当使用命令 select 结果，如果表属性特别多的时候，查看起来非常难受，在 select 语句
后使用`\G`(必须大写)，可以让结果按行垂直显示
```mysql
mysql> select * from user\G;
```
```mysql

*************************** 1. row ***************************
       id: 1
     name: wxnacy
   is_del: 0
create_ts: 2017-08-08 07:46:42
update_ts: 2017-08-08 07:46:42
1 row in set (0.00 sec)
```
## 以html格式输出
使用mysql客户端的参数–html或者-T，则所有SQL的查询结果会自动生成为html的table代码
```mysql
$ mysql -u root --html -p
mysql> select * from user;
```
```html
<TABLE BORDER=1><TR><TH>id</TH><TH>name</TH><TH>is_del</TH><TH>create_ts</TH> <TH>update_ts</TH></TR><TR><TD>1</TD><TD>wxnacy</TD><TD>0</TD><TD>2017-08-08 07:46:42</TD><TD>2017-08-08 07:46:42</TD></TR></TABLE>
```
## 以xml格式输出
使用mysql客户端的参数–xml或者-X选项，可以将结果输出为xml格式
```mysql
$ mysql -u root --xml -p
mysql> select * from user;
```
```xml
<?xml version="1.0"?>

<resultset statement="select * from user;" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <row>
	<field name="id">1</field>
	<field name="name">wxnacy</field>
	<field name="is_del">0</field>
	<field name="create_ts">2017-08-08 07:46:42</field>
	<field name="update_ts">2017-08-08 07:46:42</field>
  </row>
</resultset>
```
## 使用pager进入more或less查看结果
当select查询结果很多时，一屏幕往往无法装下。使用pager命令后在进行select命令，可以进入类似linux中more或less查看文件的效果
```mysql
mysql> pager more
PAGER set to 'more'
mysql> select * from user;
...
mysql> nopager #退出pager状态
PAGER set to stdout
```


