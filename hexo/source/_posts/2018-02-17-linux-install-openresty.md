---
title: Linux 安装 openresty
tags:
  - linux
date: 2018-02-17 21:19:33
---


Linux 系统在安装 openresty 时，无法直接用 `yum, apt` 等安装包工具，需要手动添加 openresty 的仓库。
<!-- more --><!-- toc -->
## Ubuntu
```bash
# 导入我们的 GPG 密钥：
wget -qO - https://openresty.org/package/pubkey.gpg | sudo apt-key add -

# 安装 add-apt-repository 命令
# （之后你可以删除这个包以及对应的关联包）
sudo apt-get -y install software-properties-common

# 添加我们官方 official APT 仓库：
sudo add-apt-repository -y "deb http://openresty.org/package/ubuntu $(lsb_release -sc) main"

# 更新 APT 索引：
sudo apt-get update
# 然后就可以像下面这样安装软件包，比如 openresty：
sudo apt-get install openresty
```

## CentOS
```bash
# 添加仓库
sudo yum install yum-utils
sudo yum-config-manager --add-repo https://openresty.org/package/centos/openresty.repo

# 然后就可以像下面这样安装软件包，比如 openresty：
sudo yum install openresty
```

- [OpenResty® Linux 包](https://openresty.org/cn/linux-packages.html)
