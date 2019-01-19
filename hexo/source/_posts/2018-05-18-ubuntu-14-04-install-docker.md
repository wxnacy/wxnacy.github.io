---
title: Ubuntu 14.04 LTS 安装 Docker
date: 2018-05-18 14:19:39
tags: [docker]
---

Ubuntu Trusty 14.04 版本安装 Docker。

<!-- more --><!-- toc -->

**删掉老版本**

```bash
$ sudo apt-get remove docker docker-engine docker.io
```

## 安装 `linux-image-extra-`

安装 Docker 的 `aufs` 储存驱动程序

```bash
$ sudo apt-get update
$ sudo apt-get install  linux-image-extra-$(uname -r) linux-image-extra-virtual
```

## 使用仓库安装

**允许 apt 使用 HTTPS 仓库**

```bash
$ sudo apt-get update
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

**添加 Docker 官方 GPG 秘钥**

```bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

**添加仓库**

```bash
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

## 安装 Docker ce

**安装最新稳定版**

```bash
$ sudo apt-get update
$ sudo apt-get install -y docker-ce
```

**查看所有可安装版本**

```bash
$ apt-cache madison docker-ce

docker-ce | 18.03.0~ce-0~ubuntu | https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages
```

**安装指定版本**

```bash
$ sudo apt-get install -y docker-ce=18.03.0.ce
```

**运行 helloworld 镜像**

```bash
$ sudo docker run hello-world
```

- [Get Docker CE for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
