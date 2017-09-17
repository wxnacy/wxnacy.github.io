---
title: mysql prompt 提示符
date: 2017-08-09
tags: [mysql]
---

原文：[http://www.thegeekstuff.com/2010/02/mysql_ps1-6-examples-to-make-your-mysql-prompt-like-angelina-jolie/](http://www.thegeekstuff.com/2010/02/mysql_ps1-6-examples-to-make-your-mysql-prompt-like-angelina-jolie/)
## 在命令行中使用
```mysql
mysql> prompt \u@\d>
PROMPT set to '\u@\d> '
root@(none)> use test
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
root@test>
```

## 在命令行参数中使用
需要使用双引号括起来
```mysql
wxnacy@wxnacydeMacBook-Pro: ~ $ mysql -u root -p --prompt="\u@\d> "    
root@(none)> use test;
root@test>
```
### 在bash层修改 MYSQL_PS1 变量
```bash
wxnacy@wxnacydeMacBook-Pro: ~ $ export MYSQL_PS1="\u@\d> "                              
wxnacy@wxnacydeMacBook-Pro: ~ $ mysql -u root -p                            
root@(none)>
```
## 在/etc/my.cnf中配置
也可以在配置中一劳永逸
```bash
[mysql]  
prompt=\\u@\\d>\\ # 要多加一个反斜线\
  
又或者：  
[mysql]  
prompt="\u@\d> "  
```
### 更多参数
```bash
Option  Description  
  
\c  A counter that increments for each statement you issue  
\D  The full current date  
\d  The default database  
\h  The server host  
\l  The current delimiter (new in 5.0.25)  
\m  Minutes of the current time  
\n  A newline character  
\O  The current month in three-letter format (Jan, Feb, …)  
\o  The current month in numeric format  
\P  am/pm  
\p  The current TCP/IP port or socket file  
\R  The current time, in 24-hour military time (0–23)  
\r  The current time, standard 12-hour time (1–12)  
\S  Semicolon  
\s  Seconds of the current time  
\t  A tab character  
\U  Your full user_name@host_name account name  
   
\u  Your user name  
\v  The server version  
\w  The current day of the week in three-letter format (Mon, Tue, …)  
\Y  The current year, four digits  
\y  The current year, two digits  
\_  A space  
\   A space (a space follows the backslash)  
\'  Single quote  
\"  Double quote  
\\  A literal “\” backslash character  
\x  x, for any “x” not listed above  

```



