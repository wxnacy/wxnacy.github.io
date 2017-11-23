---
title: Linux CentOS 各个版本启动SSHD服务命令
date: 2017-08-22
tags: [linux]
---

> 本篇介绍如何在 CentOS 系统中怎样启动sshd服务，如何开机自启

## 命令概况

CentOS < 7.x
```bash
service command     # 使用service命令做start|stop|restart sshd
chkconfig command   # turn on or off 机器自启sshd
```

CentOS >= 7.x
```bash
systemctl command # 管理 start|stop|start 自启sshd
```

## CentOS < 7.x

### chkconfig
```bash
$ chkconfig sshd on     # 开机自启sshd
$ chkconfig sshd off    # 开机关闭自启sshd
$ chkconfig --list sshd # 查看每个运行级别类型中服务的当前状态
```

### service

```bash
$ service sshd start | stop | restart
or
$ /etc/init.d/sshd start | stop | restart
```

## CentOS >= 7.x

```bash
$ systemctl enable sshd.service     # 开机自启sshd
$ systemctl disable sshd.service    # 开机关闭自启sshd
$ systemctl start sshd.service      # 启动sshd
$ systemctl restart sshd.service    # 重启
$ systemctl stop sshd.service       # 停止
$ systemctl reload sshd.service     # 重新加载
$ systemctl status sshd.service     # 查看启动状态
```
