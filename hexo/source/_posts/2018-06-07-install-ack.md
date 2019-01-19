---
title: 常用平台安装 ack
tags:
  - linux
date: 2018-06-07 11:04:22
---


介绍几个常用平台安装 ack

<!-- more --><!-- toc -->

## 使用 curl

```bash
$ curl https://beyondgrep.com/ack-2.22-single-file > ~/bin/ack && chmod 0755 ~/bin/ack
```

## 使用安装器

**macOS**

```bash
$ brew install ack
```

**Ubuntu**

```bash
$ sudo apt update -y
$ sudo apt install -y ack-grep
```

**CentOS**

```bash
$ sudo yum -y update
$ sudo yum -y install epel-release ack
```

更多平台安装见[文档](https://beyondgrep.com/install/)
