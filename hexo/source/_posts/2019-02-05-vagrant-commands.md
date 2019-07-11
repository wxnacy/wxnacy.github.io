---
title: Vagrant 常用命令
date: 2019-02-05 22:33:10
tags: [vagrant]
---

记录些 Vagrant 经常用到的命令

<!-- more -->
<!-- toc -->

## 工作目录中

```bash
$ vagrant init centos/7             # 初始化系统"
$ vagrant up                        # 启动虚拟机"
$ vagrant ssh                       # 登陆虚拟机"
$ vagrant halt                      # 登陆虚拟机"
$ vagrant destroy                   # 销毁虚拟机"
$ vagrant destroy -f                # 销毁虚拟机，并对询问回答 yes"
$ vagrant package                   # 打包 box"
$ vagrant package --ouput box-name  # 打包 box，并指定包名"
$ vagrant box update                # 更新 box 版本"
$ vagrant status                    # 当前虚拟机状态
$ vagrant reload                    # 重新加载虚拟机配置
```

## 全局命令

查看所有虚拟机状态

```bash
$ vagrant global-status

id       name    provider   state        directory
-----------------------------------------------------------------------------------------
2ed1547  default virtualbox running      /Users/wxnacy/VagrantProjects/centos7-wshell
1a7c506  default virtualbox inaccessible /Users/wxnacy/VagrantProjects/wxnacy-centos7
a980255  default virtualbox inaccessible /Users/wxnacy/VagrantProjects/centos6
d6edb01  default virtualbox running      /Users/wxnacy/VagrantProjects/wxnacy-ubuntu1604
908baa1  default virtualbox running      /Users/wxnacy/VagrantProjects/xenial64
da8e118  default virtualbox running      /Users/wxnacy/VagrantProjects/bionic64
7a1fc36  default virtualbox poweroff     /Users/wxnacy/VagrantProjects/ubuntu1804
40aa16f  default virtualbox running      /Users/wxnacy/VagrantProjects/centos7
```

销毁指定虚拟机

```bash
$ vagrant destroy name|id
```

查看所有 box 列表

```bash
$ vagrant box list

centos/7          (virtualbox, 1811.02)
debian/jessie64   (virtualbox, 8.11.0)
ubuntu/bionic64   (virtualbox, 20190212.1.0)
wxnacy/ubuntu1804 (virtualbox, 0)
```

添加本地 box 到仓库

```bash
$ vagrant box add my-box-name box-path
```

删除 box

```bash
$ vagrant box remove my-box-name
$ vagrant box remove my-box-name --box-version <version>    # 指定版本
```

更新 box

```bash
$ vagrant box update --box <box-name>
```

- [Command-Line Interface](https://www.vagrantup.com/docs/cli/)
