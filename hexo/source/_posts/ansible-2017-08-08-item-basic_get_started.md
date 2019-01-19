---
title: ansible入门笔记1 Get Started
date: 2017-08-08
tags: [ansible]
---

专辑：[ansible学习笔记](/2017/08/14/ansible-2017-08-14-album-study-notes/)

> Ansilbe 是一个部署一群远程主机的工具。远程的主机可以是远程虚拟机或物理机，也
可以是本地主机。Ansilbe 是一个部署一群远程主机的工具。远程的主机可以是远程虚拟机
或物理机，也可以是本地主机。

<!-- move -->

<!-- toc -->

## 安装ansible
### 命令
```bash
pip install ansible
```
### 配置hosts
修改/etc/ansible/hosts 全局hosts文件，没有的话自己创建
```bash
[wxnacy] # 如果服务器使用密码登录就用这个方式保存密码，避免每次输入
wxnacy.server.org ansible_ssh_pass=your_pass ansible_ssh_user=your_name

[prod] # 如果服务器使用sshkey登陆（推荐使用）
prod.server.org ansible_ssh_user=your_name ansible_ssh_private_key_file=key_path
```
## 第一条命令

- 首先执行ping，查看是否可以连接服务器

```bash
$ ansible all -m ping


wxnacy.server.org | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
prod.server.org | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```
得到如上样式结果即为正确,另外执行 `ansible wxnacy -m ping` 可以针对某一个服务器
组进行操作

- 现在我们用另一个命令看下是不是真的可以拿到远程服务器的信息

```bash
$ ansible prod -m shell -a "uname -a"

prod.server.org | SUCCESS | rc=0 >>
Linux ip-172-31-5-249 4.9.27-14.31.amzn1.x86_64 #1 SMP Wed May 10 01:58:40 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```

## 指定hosts文件
在一些项目中，全局hosts配置不能满足需求，需要指定hosts命令，可以执行如下命令
```bash
ansible my -i hosts_path -m ping
```


