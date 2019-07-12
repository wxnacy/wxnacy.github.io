---
title: Centos7 如何安装 Redis
date: 2019-07-12 17:02:08
tags: [linux]
---

Centos 默认仓库不包含 Redis 安装包，我们可以从 Remi 仓库中来安装。

<!-- more -->
<!-- toc -->

**安装 Remi 仓库**

```bash
$ sudo yum install epel-release yum-utils
$ sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm
$ sudo yum-config-manager --enable remi
```

**安装 Redis**

```bash
$ sudo yum install -y redis
```

**启动**

```bash
$ sudo systemctl start redis    # 启动
$ sudo systemctl enable redis   # 开机自启
```

**测试是否安装成功**

```bash
$ redis-cli ping
PONG
```

- [How To Install and Configure Redis on CentOS 7](https://linuxize.com/post/how-to-install-and-configure-redis-on-centos-7/)

