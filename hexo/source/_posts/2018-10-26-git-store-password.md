---
title: Git 将用户名密码储存在本机，避免每次输入
date: 2018-10-26 11:33:53
tags: [git]
---

新机器上使用 Git，每次推送都需要使用密码，为了避免这种情况，需要将密码储存在本地。

<!-- more --><!-- toc -->

在提交文件之前使用命令

```bash
$ git config --global credential.helper store
```

随后再输入用户名和密码后会在根目录 `~` 中生成一个文件 `.git-credentials`

文件内容为

```bash
https://user:password@github.com
```

以后再次提交内容则不用在输入密码，也可以手动添加该文件。

Mac 中可以使用 `osxkeychain` 模式将密码加密储存。

```bash
$ git config --global credential.helper osxkeychain
```

**参考**

- [Git 工具 - 凭证存储](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%87%AD%E8%AF%81%E5%AD%98%E5%82%A8)
