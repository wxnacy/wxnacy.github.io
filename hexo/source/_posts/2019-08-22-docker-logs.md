---
title: Docker logs 命令
tags:
  - docker
date: 2019-08-22 17:40:01
---


之前没有留意过 `docker logs` 的正确用法，总是直接使用 `docker logs -f` 来实时跟踪日志，但是每次都要全部显示日志后再跟踪，时间一长日志变多就是灾难，看一下帮助文档，学习下正确用法。

<!-- more -->
<!-- toc -->

## 基础命令

```bash
$ docker logs --help

Usage:  docker logs [OPTIONS] CONTAINER

Fetch the logs of a container

Options:
      --details        Show extra details provided to logs
  -f, --follow         Follow log output
      --since string   Show logs since timestamp (e.g. 2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes)
      --tail string    Number of lines to show from the end of the logs (default "all")
  -t, --timestamps     Show timestamps
      --until string   Show logs before a timestamp (e.g. 2013-01-02T13:23:37) or relative (e.g. 42m for 42 minutes)
```

想要跟 `tail -f` 命令一样从末尾10条以后开始跟踪，需要使用 `--tail` 参数，默认就是全部

**从末尾 10 条后开始跟踪**

```bash
$ docker logs -f --tail 10 <container-id>
```

除了行数限制，还可以根据时间戳来获取指定时间前后的是日志

**获取指定时间以后的日志**

```bash
$ docker logs -t --since="2019-08-20T13:23:37" <container-id>
```

**获取最后 10 分钟的日志**

```bash
$ docker logs -t --since=10m <container-id>
```

**获取指定时间范围的日志**

```bash
$ docker logs -t --since="2019-08-20T13:23:37" --until="2019-08-21T13:23:37" <container-id>
```

## 使用 grep

如果你使用 `grep` 会发现根本不起作用，因为 `docker logs` 命令并没有将日志打印到标准输出，这里我们需要先重定向下。

```bash
$ docker logs -f --tail 10 <container-id> 2>&1 | grep 'grep thing'
```
