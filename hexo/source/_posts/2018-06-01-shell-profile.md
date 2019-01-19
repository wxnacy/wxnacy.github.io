---
title: Shell 环境中 bash_profile 和 bashrc 的区别
tags:
  - shell
date: 2018-06-01 22:12:49
---


在 shell 环境中 `~/.bash_profile` 和 `~/.bashrc`  文件都可以都可以配置环境变量等信息，那到底该写到那个文件里边呢？

<!-- more --><!-- toc -->
首先来了解下 Linux 在登录时会按照如下顺序执行配置文件

```bash
/etc/profile -> (~/.bash_profile | ~/.bash_login | ~/.profile) -> ~/.bashrc -> /etc/bashrc -> ~/.bash_logout
```

## /etc/profile

该文件为系统所有用户设置环境信息，只在用户登录时执行一次，并且执行 `/etc/profile.d` 目录下的配置信息

## ~/.bash_profile ~/.bash_login ~/.profile

当前登录用户的环境信息，只在登录时执行一次。

三个文件只会按照顺序执行一个，并且都会执行 `~/.bashrc` 文件，因为在 `~/.bash_profile` 有如下语句

```bash
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi
```

其中 CentOS 会用 `~/.bash_profile` 文件，Ubuntu 用 `~/.profile` 文件

## ~/.bashrc

当前登录用户的 shell 配置，在执行 `~/.bash_profile` 后会执行该文件

它是交互式 `non-login` 方式，所以每次打开新 shell 都会执行

## /etc/bashrc

如果 `~/.bashrc` 文件中有

```bash
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
```

则也会执行它，同时会执行 `/etc/profile.d` 目录下的配置

## ~/.bash_logout

最后用户登出时还会执行 `~/.bash_logout`

最后总结下如果是配置环境变量等信息推荐写到 `~/.bash_profile` 文件中，shell 信息比如 `alias` 等配置推荐写到 `~/.bashrc` 中
