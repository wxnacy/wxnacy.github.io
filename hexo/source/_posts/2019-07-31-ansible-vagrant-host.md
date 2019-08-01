---
title: Ansible 在 Vagrant 中使用
tags:
  - ansible
  - vagrant
date: 2019-07-31 17:38:41
---


Ansible 在 Vagrant 中使用的难点在于获取 ssh 登录需要的配置信息。

<!-- more -->
<!-- toc -->

在默认 `Vagrantfile` 中我们找不到这些信息，此时需要通过 `vagrant ssh-config` 命令查看

```bash
$ vagrant ssh-config
Host default
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /Users/wxnacy/.vagrant.d/boxes/wxnacy-VAGRANTSLASH-ubuntu1804/0/virtualbox/vagrant_private_key
  IdentitiesOnly yes
  LogLevel FATAL
```

啊，让我费解的 `IdentityFile` 文件终于露出来，关键就是这个文件。

接下来我们只需要配置 Ansible 的 hosts 文件，`/etc/ansible/hosts` 中添加，或者创建独立的 `hosts` 文件

```bash
[vagrant]
127.0.0.1 ansible_ssh_user=vagrant ansible_ssh_port=2222 ansible_ssh_private_key_file=/Users/wxnacy/.vagrant.d/boxes/wxnacy-VAGRANTSLASH-ubuntu1804/0/virtualbox/vagrant_private_key
```

最后查看是否能正常连接

```bash
$ ansible all -m command -a 'who' --inventory-file=hosts
127.0.0.1 | CHANGED | rc=0 >>
vagrant  pts/0        Jul 30 07:35 (10.0.2.2)
vagrant  pts/1        Jul 30 06:19 (10.0.2.2)
```

如果新建其他位置的 `hosts` 文件，需要 `--inventory-file, -i` 指定文件。
