---
title: mysql 小技巧
date: 2017-08-09
tags: [mysql]
---

## 使用tee指定输入日志
tee命令可以将mysql操作日志输出到指定文件中，如果文件已存在则追加。命令行参数可以使用--tee=file_path，命令中可以使用tee或\T,想要退出使用日志可以使用\t
```mysql
$ mysql -u root -p --tee=mysql.log
Logging to file 'mysql.log'
mysql> tee mysql.log 或 \T mysql.log
Logging to file 'mysql.log'
mysql> \t mysql.log
Outfile disabled
```
## 使用os命令
```mysql
mysql> system uname;
Darwin
mysql> \! uname;
Darwin
```
## 执行sql文件
```mysql
mysql> source mysql.sql
```

