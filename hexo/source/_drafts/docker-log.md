---
title: Docker 容器日志的位置
tags: [docker]
---

Docker 再启动容器后，可以用 `docker logs -f <container_name>` 来查看日志内容，那么日志文件存放在哪了呢？
<!-- more --><!-- toc -->

**查看日志位置**

```bash
$ docker inspect --format='{{.LogPath}}' <container_name>
```

**实时查询内容**

```bash
$ sudo tail -f `docker inspect --format='{{.LogPath}}' <container_name>`
```

有个问题是该文件所在目录，普通登录用户是没有权限进入的，我们可以将日志从写道一个方便的位置

```bash
$ nohup sudo bash -c "docker logs -f <container_name> >> /var/log/<container_name>.log" &
```

