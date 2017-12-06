---
title: Linux 远程文件传输 SFTP 和 SCP
date: 2017-08-22
tags: [linux]
---

> 熟悉linux的朋友都知道 SSH 可以登录远程服务器进行工作，但是如果想从远程服务器下载文件或上传到服务器呢，SSH 就做不到了，这时候我们可以用 SFTP 和 SCP 完成任务，这两个指令也是使用 SSH 的通道（Port 22），只是模拟 FTP 与复制的操作而已。下面我们一一介绍.

<!-- more -->
## SFTP

SFTP 登陆主机和 SSH 一样，也是用 用户名@主机名的方式连接
```bash
$ sftp root@localhost
root@localhost's password: # 输入密码
sftp> exit # 输入FTP 相关命令
```

进入主机后，就与一般 FTP 模式下操作方式一样了！下面是具体可用命令:
### 远程服务器
```bash
# 切换某个目录
$ cd PATH

# 列出当前目录文件名
$ ls

# 建立目录
$ mkdir DIR

# 删除目录
$ rmdir DIR

# 显示当前目录
$ pwd

# 更改文件或目录的属组
$ chgrp groupname PATH

# 更改文件或目录的属主
$ chown username PATH

# 更改文件或目录的权限
$ chmod 664 PATH

# 建立连接文件
$ ln oldname newname

# 删除文件或目录
$ rm PATH

# 更改文件或目录名称
$ rename oldname newname

# 离开远程主机
$ exit | bye | quit
```

### 本机
都在普通命令前加上l(L的小写)
```bash
# 切换某个目录
$ lcd PATH

# 列出当前目录文件名
$ lls

# 建立目录
$ lmkdir DIR


# 显示当前目录
$ lpwd
```

### 上传下载操作

```bash
# 将文件由本机上传到远程主机
$ put [本机目录或文件] [远程]
$ put [本机目录或文件]
# 如果用第二种格式，则文件会上传到远程主机当前目录下

# 将文件由远程主机下载到本地
$ get [远程目录或文件] [本地]
$ get [远程目录或文件]
# 如果用第二种格式，则文件会下载到本地当前目录下

put 和 get 都可以使用通配符 如: get * ,put *.pem
```

就整体而言，如果不考虑图形接口，SFTP 在 Linux 中完全可以取代 FTP 了，因为所有功能都已经涵盖

## 文件异地直接复制: SCP

通常使用 SFTP 是因为可能还不知道服务器上面存在文件的信息，如果已经知道服务器上的文件名和地址，那么最简单的文件传输方式 SCP 指令

```bash
$ scp [-pr] [-l 速率] file [账号@]主机:目录名 # 上传
$ scp [-pr] [-l 速率] [账号@主机]:file 目录名 # 下载

# 参数
-p : 保留文件原有的权限信息
-r : 复制来源为目录时,可以复制整个目录(包含子目录)
-l : 可以限制传输的速率,单位为 Kbits/s , 例如 [-l 800 ] 代表传输速率 100Kbytes/s
```
