---
title: CentOS 安装 Docker
date: 2018-05-15 18:43:23
tags: [docker]
---

简单介绍下 CentOS 环境下安装 Docker。

<!-- more --><!-- toc -->

**准备工作**

```bash
$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```

**添加 Docker 仓库**

```bash
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

**允许使用edge test 版本**

```bash
$ sudo yum-config-manager --enable docker-ce-edge
$ sudo yum-config-manager --enable docker-ce-test
```

**查看可下载版本**

```bash
$ yum list docker-ce --showduplicates | sort -r
```

**下载指定版本**

```bash
$ sudo yum install -y docker-ce-18.03.0.ce
```

**下载最新版本**

```bash
$ sudo yum install -y docker-ce
```

**启动**

```bash
$ sudo systemctl start docker
```

- [Get Docker CE for CentOS](https://docs.docker.com/install/linux/docker-ce/centos/)
