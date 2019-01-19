---
title: Nginx 分割日志
tags:
  - nginx
date: 2018-04-02 09:50:08
---

Nginx 有个非常大的缺点，就是日志不能自动分割，死磕着一个文件写到死

<!-- more --><!-- toc -->
如果你重度依赖 `access.log` 日志进行分析，那长时间面对动辄上 G 的文件，你会很头痛，所以只能自己来写脚本来分割

首先确定思路，最容易想到的方法就是将现在的日志文件挪走，然后期望 Nginx 重新生成一个日志，然后把这个动作定时执行，接下来我们一步一步实现

挪走日志
```bash
$ cd /usr/local/nginx/logs
$ sudo mv access.log access.log.1
$ ll

-rw-r--r--. 1 nginx root   97 Mar 31 23:12 access.log.1
-rw-r--r--. 1 nginx root 4575 Mar 31 23:12 error.log
```
做完后，Nginx 程序并没有停止，但是也没有生成新的 `access.log` 文件，查看日志
```bash
$ tail -f access.log.1
```
发现日志继续写在了 `access.log.1` 中，虽然名字改变了，但对于 Nginx 来说文件指向
依然是它，那就需要强迫它重新打开日志文件
```bash
$ nginx -s reopen
$ ll

-rw-r--r--. 1 nginx root   97 Mar 31 23:12 access.log
-rw-r--r--. 1 nginx root   97 Mar 31 23:12 access.log.1
-rw-r--r--. 1 nginx root 4575 Mar 31 23:12 error.log
```
执行后，我们会发现新的 `access.log` 生成了，至此单次流程完成。

我们总不能每次都手动完成这个操作，定时任务是必须的

首先完善下分割脚本
```bash
$ cd /usr/local/nginx/logs
$ touch split_log.sh
$ vim split_log.sh

#!/usr/bin/env bash
LOG_DIR=/usr/local/nginx/logs
LOG_FILE=${LOG_DIR}/access.log
DT=`date "+%Y%m%d%H%M%S"`
# 检查日志文件是否存在
test -f ${LOG_FILE} && mv ${LOG_FILE} ${LOG_FILE}.${DT}
nginx -s reopen
```
添加执行权限
```bash
$ chmod +x split_log.sh
```
添加定时任务
```bash
$ crontab -e

* */1 * * * /bin/bash /usr/local/nginx/logs/split_log.sh
```
然后执行 `:wq` 退出，系统会自动生成定时任务，每小时执行一次。

- [Linux Crontab 定时任务](/2018/01/15/linux-crontab/)
