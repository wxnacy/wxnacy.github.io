---
title: Mysql '/tmp/mysql.sock' 错误类型解决方法
date: 2017-09-15
tags: [mysql]
---

> Can't connect to local MySQL server through socket '/tmp/mysql.sock'

一般情况下我装好 mysql 后就不会在动它了，因为一不留神就出各种错误信息，在不记得
多少次 google 这个错误之后，我决定把它记下来
<!-- more -->
网上很多解决方法都是说 mysql 服务找不到 **/tmp/mysql.sock** 文件，那我们找到它
不就行了，
```bash
$ find / -name mysql.sock
/var/lib/mysql/mysql.sock
$ ln -s /var/lib/mysql/mysql.sock   /tmp/mysql.sock
```
先找到这个文件，然后建立软连接到 */tmp/mysql.sock* ，然而到我试验的时候，完全找
不到这个文件

在翻阅资料后，发现 */tmp/mysql.sock* 是在 mysql 启动后生成的临时文件，也就是说
不成功启动 mysql 就不会有这个文件，我的方向完全错误，折腾到筋疲力尽，最后我只得
找到各种日志查看
```bash
$ mysqld status
```
通过查看 mysql 运行状态状态发现这货
```bash
[ERROR] unknown variable 'prompt=\c \U[\d] \D> '
```
不管为啥不通过先干掉再说，重启 mysql 继续查看状态，又出现这货
```bash
[ERROR] InnoDB: Unable to lock ./ibdata1 error
```
说明当前又进行 mysql 进程再启动
```bash
$ kill -9 `ps aux | grep mysql | awk '{print $2}'`
```
通过这段命令强行 kill 掉所以 mysql 进程
```bash
$ mysql.service start
```
成功

通过这次解决问题，报错 **/tmp/mysql.sock** 不一定是它的问题，关键还是看日志，对
的错的全在日志里
