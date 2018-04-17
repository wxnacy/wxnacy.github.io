---
title: Git ERROR Permission to XXX.git denied to user 的一种可能
date: 2018-04-17 09:46:04
tags: [git]
---

Git 的使用过程你一定会遇到一两次报错 `ERROR: Permission to XXX.git denied to user`，归根到底是当前用户对仓库没有对应的权限，然而造成这种错误的情况却有很多种，今天记录某一种可能。

<!-- more -->

我有两个用户 A 和 B，用户 A 创建了的仓库并邀请了 B，B 对其操作是没有问题的。但是如果 A 新建了组织，并在组织中新建仓库再邀请 B，就会报权限的错误。

**解决方法**

在 `~/.ssh/config` 中添加

```bash
Host github.com
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa
```

并修改项目的远程地址

```bash
$ vim .git/config

- https://github.com/wxnacy/wxnacy.github.io.git
+ git@github.com:wxnacy/wxnacy.github.io.git
```


