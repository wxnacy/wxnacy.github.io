---
title: Docker 简单实用
date: 2018-05-16 11:02:59
tags: [docker]
---

Docker 简单实用

<!-- more --><!-- toc -->

**避免每次输入 sudo**

```bash
$ vim ~/.bash_profile

alias docker="sudo docker"
```

**版本信息**

```bash
$ docker --version
$ docker version
$ docker info
```

**登陆**

```bash
$ docker login
```

**创建镜像**

```bash
$ docker build -t <image-name> .
```

**查看镜像列表**

```bash
$ docker image ls
```

**运行镜像**

```bash
$ docker run --rm --name <container-name> -d -p 8080:80 <image-name>
```

**删除镜像**

```bash
$ docker image rm <image-id>[<image-name>]  # id 输入前几位即可
$ docker rmi <image-id>[<image-name>]
```

**容器列表**

```bash
$ docker container ls           # 在运行的容器列表
$ docker container ls --all     # 全部容器列表
$ docker container ls -aq
```

**停止容器**

```bash
$ docker container stop <container-name>[<container-id>]
```

**使用镜像运行demo**

```bash
$ docker run -it --rm --name <demo-name> -v "$PWD":/usr/src/myapp -w /usr/src/myapp -p 8006:8005 python:3.5 python app.py
```

- [Get Started](https://docs.docker.com/get-started/)
