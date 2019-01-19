---
title: Ubuntu 安装 Yarn
date: 2018-05-12 19:17:08
tags: [node]
---

在 Ubuntu 系统中不能直接通过 `apt` 安装，需要先添加 yarn 仓库。

<!-- more --><!-- toc -->

```bash
$ curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
$ echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
```

随后更新 `apt` 再下载即可。

```bash
$ sudo apt-get update && sudo apt-get install yarn
```

- [ubuntu 安装](https://yarnpkg.com/lang/zh-hans/docs/install/#debian-stable)
