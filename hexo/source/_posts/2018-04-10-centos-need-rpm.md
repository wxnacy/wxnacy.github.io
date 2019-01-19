---
title: 整理 CentOS 需要的基础包
date: 2018-04-10 15:45:18
tags: [linux]
---

最近使用新的 CentOS 环境开发，碰到很多缺包的情况，今天整理下新环境需要安装的包。

<!-- more --><!-- toc -->

**安装基础工具**

```bash
$ yum install wget screen telnet perl perl-CPAN bash-completion ntp iptraf sysstat git subversion nfs-utils vim-common lrzsz patch
# bash-completion bash自动补全
# iptraf          ip诊断工具
# sysstat         sar等系统诊断工具
# lrzsz           rz/sz zmodem上传下载工具
```

**编译安装需要的开发包**

```bash
$ yum install gcc g++ gcc-c++ make cmake aclocal
```

**安装 Nginx 肯定需要的**

```bash
$ yum -y install pcre pcre-devel openssl openssl-devel
```

**安装 GeoIp 需要的**

```bash
$ yum -y install zlib zlib-devel
```

**开发包**

```bash
$ yum install db4 db4-devel libjs libjs-devel libcurl libpcap libtool sqlite sqlite-devel

$ yum install libevent libevent-devel readline readline-devel

$ yum install libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel tcl tcl-devel

$ yum install libxml2 libxml2-devel glibc glibc-devel glib2 glib2-devel

$ yum install ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5 krb5-devel

$ yum install bzip2  bzip2-devel libidn libidn-devel

$ yum install libffi libffi-devel

$ yum install cffi cryptography

$ yum install python python-devel

$ yum install python35 python35-devel
```
