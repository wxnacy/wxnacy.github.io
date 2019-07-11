---
title: apt 下载报错 [Could not get lock /var/lib/dpkg/lock-frontend]
date: 2019-07-11 21:15:29
tags: [linux]
---

有两种情况会导致软件安装工具报这种错
- `Synaptic Package Manager` 或 `Software Updater` 是打开的。
- 一些apt命令在终端中运行或者在后台有进程正在运行。

<!-- more -->
<!-- toc -->

```bash
$ sudo apt install -y redis
E: Could not get lock /var/lib/dpkg/lock-frontend - open (11: Resource temporarily unavailable)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), is another process using it?
```

**查看进程**

```bash
$ ps aux | grep apt
root 1747 0.0 0.0 4628 808 ? Ss 07:06 0:00 /bin/sh /usr/lib/apt/apt.systemd.daily update
root 1769 0.0 0.0 4628 1820 ? S 07:06 0:00 /bin/sh /usr/lib/apt/apt.systemd.daily lock_is_held update
_apt 16225 3.0 0.2 80192 8796 ? S 07:07 0:04 /usr/lib/apt/methods/http
_apt 16226 0.7 0.2 80188 8800 ? S 07:07 0:01 /usr/lib/apt/methods/http
```

**停掉进程**

```bash
$ sudo killall apt apt-get
```

这是比较快捷的方式，但是还不够，前两条都无法关闭，只能将 pid 杀死

```bash
$ sudo kill -9 <pid>
```

**删除加锁文件**

```bash
$ sudo rm /var/lib/apt/lists/lock
$ sudo rm /var/cache/apt/archives/lock
$ sudo rm /var/lib/dpkg/lock*
```

**重新配置 dpkg**

```bash
$ sudo dpkg --configure -a
dpkg: error: parsing file '/var/lib/dpkg/updates/0004' near line 0:
newline in field name '#padding'
```

这时候有可能还会出现一个错误，这时要手动删除该文件

```bash
$ sudo rm -rf /var/lib/dpkg/updates/0004
```

再次执行配置命令，然后继续安装软件即可

```bash
$ sudo apt update -y
$ sudo apt install -y redis
```

