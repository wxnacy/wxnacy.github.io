---
title: Ubuntu 18.04 安装 Mysql
date: 2018-10-11 16:57:37
tags: [linux, mysql]
---

本章介绍在 `Ubuntu 18.04` 版本中安装 Mysql

<!-- more --><!-- toc -->

**安装**

```bash
$ sudo apt update -y
$ sudo apt install -y mysql-server
```

与 `ubuntu 16.04` 版本不同，安装过程中不会提示输入密码，需要后续的设置完成。

**设置**

```bash
$ sudo mysql_secure_installation
```

执行该命令可以修改 Mysql 密码强度并修改密码。

Mysql 默认启动，并且状态为开机自启

如果没有启动可以手动启动

```bash
$ systemctl start mysql
```

在 `mysql_secure_installation` 的设置中，有一项默认设置为禁止 root 账户使用密码登录，而是使用 `auth_socket` 插件进行身份验证，这样提高了安全性，但是远程连接 mysql 将变得非常麻烦。

**登录 Mysql**

```bash
$ sudo mysql
```

**检查每个用户的验证方式**

```bash
> SELECT user，authentication_string，plugin，host FROM mysql.user;

+------------------+-------------------------------------------+-----------------------+-----------+
| user             | authentication_string                     | plugin                | host      |
+------------------+-------------------------------------------+-----------------------+-----------+
| root             |                                           | auth_socket           | localhost |
| mysql.session    | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password | localhost |
| mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password | localhost |
| debian-sys-maint | *82BAC2D99C04DC4A272F86365C7704C18576CAA8 | mysql_native_password | localhost |
+------------------+-------------------------------------------+-----------------------+-----------+
4 rows in set (0.00 sec)
```

**将 root 用户改为密码验证**

```bash
> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

**重新加载授权表使更改生效**

```bash
> FLUSH PRIVILEGES;
```

退出 Mysql 后，再次使用密码即可登录

```bash
$ mysql -uroot -p
```

**查看版本信息**

```bash
$ mysqladmin -p -u root version

Enter password:
mysqladmin  Ver 8.42 Distrib 5.7.22, for Linux on x86_64
Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Server version          5.7.22-0ubuntu0.16.04.1
Protocol version        10
Connection              Localhost via UNIX socket
UNIX socket             /var/run/mysqld/mysqld.sock
Uptime:                 18 min 33 sec

Threads: 1  Questions: 18  Slow queries: 0  Opens: 115  Flush tables: 1  Open tables: 34  Queries per second avg: 0.016
```

**修改密码**

```mysql
> set password=password('wxnacy');
```

因为 mysql 的安全策略，密码的最低长度为 8 位，所以这个命令会报错，想要修改它的安全策略可以参见[配置](/2018/06/10/centos7-install-mysql/#pei-zhi)

## 对外开放

**打开防火墙 3306 端口**

```bash
$ sudo ufw allow 3306
$ sudo ufw disable
$ sudo ufw enable
```

**注释绑定 ip**

```bash
$ sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

# bind-address      = 127.0.0.1
```

**允许所有ip访问**

```mysql
> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'wxnacy' WITH GRANT OPTION;
```

**重启 Mysql**

```bash
$ sudo systemctl restart mysql
```

- [A Quick Guide to Using the MySQL APT Repository](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/)
- [How To Install MySQL on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
- [CentOS 7 安装 Mysql](/2018/06/10/centos7-install-mysql/)
