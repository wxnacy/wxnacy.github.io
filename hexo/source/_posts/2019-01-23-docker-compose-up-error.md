---
title: docker-compose 启动报错
date: 2019-01-23 11:01:41
tags: [docker]
---

```bash
ERROR: Couldn't connect to Docker daemon at http+docker://localunixsocket - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.
```

<!-- more --><!-- toc -->

```bash
$ docker-compose up -d
```

`docker-compose` 启动时报了如上错误，本身对该命令不太熟悉，所以开始一直在纠结 `http+docker://localunixsocket` 和 `DOCKER_HOST`，后来搜索下发现很简单。

`docker` 和 `sudo docker` 在机器里会有两个启动的可能，`docker-compose` 也要跟他相对应

```bash
$ sudo docker-compose up -d
```
