---
title: Docker 改变镜像下载目录
tags:
  - docker
date: 2019-07-26 15:16:22
---


Docker 占用储存空间很大的部分在于下载的镜像，因为 Docker 包括容器、镜像等存储数据都默认保存在 `/var/lib/docker` 目录下，如果系统磁盘空间比较小的话就会很麻烦，我想将目录改为挂载的扩充磁盘上。

<!-- more -->
<!-- toc -->

先停止 Docker

```bash
$ sudo systemctl stop docker
```

确认没有 Docker 进程在跑

```bash
$ ps faux | grep docker
```

假设新的目录为 `/data/docker`，先将数据复制到新的目录下

```bash
$ sudo cp -r /var/lib/docker /data/docker
```

然后将该目录软连接到 `/var/lib/docker`

```bash
$ sudo ln -sf /data/docker /var/lib/docker
```

启动 Docker

```bash
$ sudo systemctl start docker
```

最后查看镜像列表是否正常

```bash
$ sudo docker image ls
```

这样软连接的方式是比较灵活的，不会改变我们熟知的存储目录。官方论坛中也有修改配置文件来全局修改存储位置的方法，感兴趣的同学可以点击下方链接进入。

- [How do I change the Docker image installation directory?](https://forums.docker.com/t/how-do-i-change-the-docker-image-installation-directory/1169/1)
