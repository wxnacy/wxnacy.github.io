---
title: Vagrant 中安装 Mysql 如何从外边链接
tags:
  - mysql
date: 2018-06-16 14:29:53
---


在 Vagrant 中安装 Mysql 后从外部链接需要三步

<!-- more --><!-- toc -->

## 设置私有 ip

修改 `Vagrantfile` 添加 `private_network`，这样外部可以通过该 ip 链接

```bash
config.vm.network "private_network", ip: "192.168.33.10"
```

这步需要放在第一步来完成，随后重新加载配置

```bash
$ vagrant reload
```

## 去掉绑定 127.0.0.1

如果你是使用 `rpm` 来安装的话，修改 `/etc/mysql/mysql.conf.d/mysql.cnf`，将绑定 `127.0.0.1` 这一行注释掉

```bash
# bind-address            = 127.0.0.1
```

## 对所有 ip 开放

登陆 Mysql 并对所有外网 ip 开放权限

```bash
$ mysql -uroot -p

> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'your_mysql_password' WITH GRANT OPTION;
```

这样从外部通过如下命令就可以访问了

```bash
$ mysql -uroot -p -h 192.168.33.10
```

**注意**

如果在生产环境上的话建议只对指定 ip 开放权限

```mysql
> GRANT ALL PRIVILEGES ON *.* TO 'root'@'213.1.2.1' IDENTIFIED BY 'your_mysql_password' WITH GRANT OPTION;
```
