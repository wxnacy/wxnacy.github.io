---
title: Linux 安装 Vagrant
date: 2018-07-11 11:11:31
tags: [vagrant]
---

本章介绍如何在 Linux 中安装 Vagrant

<!-- more --><!-- toc -->

**Ubuntu**

```bash
$ sudo apt update -y && sudo apt install vagrant
```

**CentOS**

首先从地址 https://releases.hashicorp.com/vagrant 中查找你需要的版本，比如

```bash
https://releases.hashicorp.com/vagrant/2.1.2/vagrant_2.1.2_x86_64.rpm
```

安装

```bash
$ sudo yum install -y https://releases.hashicorp.com/vagrant/2.1.2/vagrant_2.1.2_x86_64.rpm
```
