---
title: 可能会用到的 Linux 组合命令
date: 2018-10-22 18:21:07
tags: [linux]
---

记录一些可能会用到的组合命令

<!-- more --><!-- toc -->

**删除当前目录下 0 字节文件**

```bash
$ rm `ls -l | awk '$5 == "0" {print $9}'`
```

**MacOS 系统查看本机 ip**

```bash
$ ifconfig en0 | grep inet | grep -v inet6 | awk '{print $2}'
```

**CentOS 系统查看本机 ip**

```bash
$ ifconfig eth0 | grep inet | grep -v inet6 | awk '{print $2}'
```

**Ubuntu 系统查看本机 ip**

```bash
$ ifconfig eth0 | grep inet | grep -v inet6 | awk '{print $2}' | awk -v FS=":" '{print $2}'
```
