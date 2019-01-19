---
title: Docker 容器的自动启动
date: 2018-05-25 15:51:19
tags: [docker]
---

使用 docker 时需要这样的需求，在服务器重启后，docker 自动启动，但是容器没有启动。

<!-- more --><!-- toc -->
想要做到容器自动启动需要配合 `--restart` 参数，取值如下：
- `no` 不会重启，默认值
- `on-failure` 如果容器由于错误而退出，则将其重新启动，该错误表现为非零退出代码。
- `unless-stopped` 重新启动容器，除非它明确停止或者Docker本身停止或重新启动。
- `always` 如果停止，请始终重新启动容器。

一般使用 `on-failure` 参数即可，可以指定重试次数。

```bash
$ docker run --restart on-failure:10
```

需要注意的是  `--restart` 与 `--rm` 参数不能共同存在

- [Start containers automatically](https://docs.docker.com/config/containers/start-containers-automatically/)
