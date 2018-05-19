---
title: macOS 使用 Vagrant
tags: [vagrant]
---

Vagrant 是非常强大好用的虚拟机管理工具，它依赖于 virtualbox，可以非常方便的在电脑中起各种系统的虚拟机。

<!-- more --><!-- toc -->

## 安装

```bash
$ brew cask install virtualbox
$ brew cask install vagrant
```

## 使用

**初始化 box **

使用 `centos7` 系统，你也可以从 [Discover Vagrant Boxes](https://app.vagrantup.com/boxes/search) 查找其他系统

```bash
$ mkdir vagrant && cd vagrant
$ vagrant init centos/7
```

**启动虚拟机**

第一次启动时，vagrant 检查到没有指定的系统，会自动下载该镜像，下载目录为 `~/.vagrant.d/boxes`

```bash
$ vagrant up
```

**链接**

```bash
$ vagrant ssh
```

**关机**

```bash
$ vagrant halt
```

**销毁**

```bash
$ vagrant destroy
$ vagrant destroy -f    # 不询问
```

- [官网](https://www.vagrantup.com/)
- [Vagrant](http://sourabhbajaj.com/mac-setup/Vagrant/)
- [Vagrant Manager](http://vagrantmanager.com/)
