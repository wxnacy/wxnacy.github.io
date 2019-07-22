---
title: Vagrant 使用 root 账号登录
tags:
  - vagrant
date: 2019-07-18 17:42:57
---


Vagrant 想要使用 root 身份登录要稍微麻烦一点。网上的文章大多是从一个地方抄过来的，并且还没抄对，所以我在这里总结一篇正确做法。

<!-- more -->
<!-- toc -->

## 修改 sshd 配置

首先以默认身份登录，并修改 `sshd` 配置文件

```bash
$ vagrant ssh
$ sudo vim /etc/ssh/sshd_config
```

做如下变动

```bash
# PermitRootLogin prohibit-password
PermitRootLogin yes             # 允许 root 身份登录
# PasswordAuthentication on
PasswordAuthentication yes      # 可以使用密码登录
```

重启 `sshd` 服务

```bash
$ sudo systemctl restart sshd
```

## 修改 Vagrantfile

增加如下配置

```ruby
config.ssh.username = 'root'
config.ssh.password = 'root'
config.ssh.insert_key = false
```

然后再次登录即可

```bash
$ vagrant ssh
```

这里注意，网上大部分给出的例子是设置 `config.ssh.insert_key = true`，如果你这样设置了，会发现 `config.ssh.password` 将会失效，每次登录都需要手动输入密码。

为什么呢？根据[官网](https://www.vagrantup.com/docs/vagrantfile/ssh_settings.html#config-ssh-insert_key)的定义，`config.ssh.insert_key` 代表了是否使用公私钥来登录虚拟机，如果你想要使用不那么安全的登录方式，比如密码登录，则可以将它设置为 `false`，它的默认值为 `true`

了解了这一点，就可以发现手动设置 `config.ssh.insert_key=true` 是有点蠢的做法。

## 使用公私钥登录

使用密码登录的缺点很明显，明文的密码就像只穿一个裤衩就出门一样让人不安，默认的 `vagrant` 就不需要密码，那它是怎么登录的呢？

关于怎么使用公私钥登录服务器可以查看这篇文章 [Linux SSH 登陆远程服务器和无密码操作](/2017/08/23/linux-2017-08-23-ssh/)

有了这篇文章作为基础，我们来查看下 `vagrant` 账号是否做了秘钥登录。

```bash
$ cat /home/vagrant/.ssh/authorized_keys
```

执行这条命令后会发现文件中包含一条记录，证明了确实使用了秘钥登录。

下面我们为 `root` 用户赋予秘钥登录的功能

首先将电脑的公钥内容

```bash
$ cat ~/.ssh/id_rsa.pub
```

复制到虚拟机中

```bash
$ echo '公钥内容' >> /home/vagrant/.ssh/authorized_keys
```

然后修改 `Vagrantfile` 配置

```ruby
config.ssh.username = 'root'                                # 使用 root 身份登录
config.ssh.private_key_path = '/Users/wxnacy/.ssh/id_rsa'   # 私钥位置
```

接下来在登录会发现如 `vagrant` 账号般顺滑

- [SSH Settings](https://www.vagrantup.com/docs/vagrantfile/ssh_settings.html#config-ssh-private_key_path)
