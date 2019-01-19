---
title: CentOS 7 安装 Mysql
tags:
  - mysql
date: 2018-06-10 11:03:49
---


CentOS7 安装 Mysql 要不 Ubuntu 复杂不少。

<!-- more --><!-- toc -->

## 添加仓库

访问地址

```bash
https://dev.mysql.com/downloads/repo/yum/
```

查找最新的 rpm
![mysqlrpm](/images/mysqlrpm.png)

下载

```bash
$ wget https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm
```

确定 md5 值

```bash
$ md5sum mysql80-community-release-el7-1.noarch.rpm

739dc44566d739c5d7b893de96ee6848  mysql80-community-release-el7-1.noarch.rpm
```

安装

```bash
$ sudo rpm -ivh mysql80-community-release-el7-1.noarch.rpm
```



## 安装

### 8.0 版本

添加完成仓库，直接下载即可得到最新的 `8.0` 版本
```bash
$ sudo yum update -y
$ sudo yum install -y mysql-server
```

### 5.7 版本

但是现在比较稳定的版本还是 `5.7`，想要下载这个版本，还需要做一些工作。

**查看可安装版本**

```bash
$ yum repolist all | grep mysql

mysql-cluster-7.5-community/x86_64 MySQL Cluster 7.5 Community    disabled
mysql-cluster-7.5-community-source MySQL Cluster 7.5 Community -  disabled
mysql-cluster-7.6-community/x86_64 MySQL Cluster 7.6 Community    disabled
mysql-cluster-7.6-community-source MySQL Cluster 7.6 Community -  disabled
mysql-connectors-community/x86_64  MySQL Connectors Community     enabled:    51
mysql-connectors-community-source  MySQL Connectors Community - S disabled
mysql-tools-community/x86_64       MySQL Tools Community          enabled:    63
mysql-tools-community-source       MySQL Tools Community - Source disabled
mysql-tools-preview/x86_64         MySQL Tools Preview            disabled
mysql-tools-preview-source         MySQL Tools Preview - Source   disabled
mysql55-community/x86_64           MySQL 5.5 Community Server     disabled
mysql55-community-source           MySQL 5.5 Community Server - S disabled
mysql56-community/x86_64           MySQL 5.6 Community Server     disabled
mysql56-community-source           MySQL 5.6 Community Server - S disabled
mysql57-community/x86_64           MySQL 5.7 Community Server     disabled
mysql57-community-source           MySQL 5.7 Community Server - S disabled
mysql80-community/x86_64           MySQL 8.0 Community Server     enabled:    17
mysql80-community-source           MySQL 8.0 Community Server - S disabled
```

**选择默认版本为 5.7**

```bash
$ sudo yum-config-manager --disable mysql80-community
$ sudo yum-config-manager --enable mysql57-community
```

**下载**

```bash
$ sudo yum install mysql-community-server
```

**启动**

```bash
$ sudo systemctl start mysqld
```

查看运行状态

```bash
$ sudo systemctl status mysqld

● mysqld.service - MySQL Server
   Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2018-06-01 10:35:58 UTC; 1h 39min ago
     Docs: man:mysqld(8)
           http://dev.mysql.com/doc/refman/en/using-systemd.html
  Process: 7474 ExecStartPre=/usr/bin/mysqld_pre_systemd (code=exited, status=0/SUCCESS)
 Main PID: 7542 (mysqld)
   Status: "SERVER_OPERATING"
   CGroup: /system.slice/mysqld.service
           └─7542 /usr/sbin/mysqld

Jun 01 10:35:49 bogon systemd[1]: Starting MySQL Server...
Jun 01 10:35:58 bogon systemd[1]: Started MySQL Server.
```

默认是开机自启的，可以手动关闭

```bash
$ sudo systemctl disable mysqld
```

## 配置

Mysql 在安装时会默认设置一个随机密码，需要在第一次使用时修改

**查看密码**

```bash
$ sudo grep 'temporary password' /var/log/mysqld.log

2018-06-01T10:35:51.710406Z 5 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: Vq9wOQ&trFs*
```

**配置**

```bash
$ sudo mysql_secure_installation
```

执行该命令后，输入刚查询的密码即可进行后续操作，但是在修改密码后你可能会遇到错误

```bash
Failed! Error: Your password does not satisfy the current policy requirements
```

提示你的密码不符合当前策略，Mysql 密码策略有三种

```bash

There are three levels of password validation policy:

# 长度大于 8 位
LOW    Length >= 8
# 长度大于 8 位，数字，混合大小写和特殊字符
MEDIUM Length >= 8, numeric, mixed case, and special characters
# 长度大于 8 位，数字，混合大小写，特殊字符和字典
STRONG Length >= 8, numeric, mixed case, special characters and dictionary

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG:
```

他们分别对应了数字 `0, 1, 2`，Mysql 默认的等级为 `MEDIUM`，所以输入普通的密码就会报错，怎样修改策略呢？

首先使用默认密码登录 Mysql

```bash
$ mysql -uroot -p
```

查看所有 `validatei_password`

```mysql
mysql> SHOW VARIABLES LIKE 'validate_password%';

+--------------------------------------+-------+
| Variable_name                        | Value |
+--------------------------------------+-------+
| validate_password.check_user_name    | ON    |
| validate_password.dictionary_file    |       |
| validate_password.length             | 8     |
| validate_password.mixed_case_count   | 1     |
| validate_password.number_count       | 1     |
| validate_password.policy             | MEDIUM|
| validate_password.special_char_count | 1     |
| validate_password_check_user_name    | ON    |
| validate_password_dictionary_file    |       |
| validate_password_length             | 8     |
| validate_password_mixed_case_count   | 1     |
| validate_password_number_count       | 1     |
| validate_password_policy             | MEDIUM|
| validate_password_special_char_count | 1     |
+--------------------------------------+-------+
14 rows in set (0.00 sec)
```

将策略改为 `LOW`

```mysql
> set global validate_password.policy=0;
> set global validate_password_policy=0;
```

如果你不想让长度必须大于 8 位，也可以改为 4，这是最低长度

```bash
> set global validate_password_length=4;
> set global validate_password.length=4;
```

随后执行 sql 修改密码即可

```bash
> set password=password('wxnacy');
```

最后可以将访问权限全部对外开放

```bash
> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'wxnacy' WITH GRANT OPTION;
```

也可以指定 ip 开放

```bash
> GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.33.11' IDENTIFIED BY 'wxnacy' WITH GRANT OPTION;
```


- [A Quick Guide to Using the MySQL Yum Repository](https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/)
- [How To Install MySQL on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-centos-7)
- [解决 MySQL 5.7 中 Your password does not satisfy the current policy requirements. 问题](https://blog.csdn.net/maxsky/article/details/51171474)

