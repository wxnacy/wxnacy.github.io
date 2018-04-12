---
title: MacOS 使用 SSHFS 将远程文件挂载到本地
date: 2018-04-12 15:41:54
tags: [mac]
---

> SSHFS允许您使用SFTP安装远程文件系统。 大多数SSH服务器默认支持并启用此SFTP访问，因此SSHFS使用起来非常简单，服务器端无需执行任何操作。

<!-- more --><!-- toc -->

在 MacOS 中使用 SSHFS 需要 FUSE 的支持

> 用于 macOS 的 FUSE 允许您通过第三方文件系统扩展 macOS 的本地文件处理功能。 它是 MacFUSE 的继任者，已被许多产品用作软件构建块，但不再维护;

## 安装

**下载安装**

你可以从[官网](https://osxfuse.github.io/)中下载最新版的 `FUSE for macOS` 和 `SSHFS` 直接安装。

**HomeBrew**

也可以使用 HomeBrew 安装

```bash
$ brew cask install osxfuse
$ brew cask install sshfs
```

## 使用

**新建本地挂载点**

```bash
$ mkdir local-file
```

**挂载**

```bash
$ sshfs user@hostname:/absolute/path/to/document local-file
```

远程的地址最好使用绝对路径。此时打开该文件夹就可以访问远程文件了。

**卸载挂载文件**

```bash
$ umount local-file
```

- [sshfs](https://github.com/libfuse/sshfs)
