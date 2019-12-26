---
title: 解决 Docker 日志文件太大的问题
date: 2019-12-26 14:51:31
tags: [docker]
---

Docker 在不重建容器的情况下，日志文件默认会一直追加，时间一长会逐渐占满服务器的硬盘的空间，内存消耗也会一直增加，本篇来了解一些控制日志文件的方法。

<!-- more -->
<!-- toc -->

Docker 的日志文件存在 `/var/lib/docker/containers` 目录中，通过下面的命令可以将日志文件夹根据升序的方式罗列出来。

```bash
$ sudo du -d1 -h /var/lib/docker/containers | sort -h

28K     /var/lib/docker/containers/0db860afe94df368335c2e96f290275f4c396b996b4e8d22770b01baafd9982c
36K     /var/lib/docker/containers/6ee184044661c436b44769d56c203f1fc296dbfe08f6ed4cf79aa6fb8cae6659
44K     /var/lib/docker/containers/66c44231981fcb5ecd33bf0fc3390e71c5cbbabb839d79441eb3317b8500d551
60K     /var/lib/docker/containers/bc4136199037e73d712614ef57de0915d294cbe51045d213f0d822d71a86cf2c
344K    /var/lib/docker/containers/7bd3a179cf67b1537e0965c1d1f518420ac5d4cd151ecb75c37ada8c2347ca6b
984K    /var/lib/docker/containers/6bd1f79f16b8b06f2bd203dd84443004ba08c150ac51d23fa620e8b2cbf4b773
1.7M    /var/lib/docker/containers/a93a4275571b0033367f9cab8213c467b21a03c600e2203195640b5a5bc7f523
4.4M    /var/lib/docker/containers/082564c5bdb19b642491b09419a69061122483c0f959a36eb186dd1fec53c163
14M     /var/lib/docker/containers/05fc24ef7a14e31e4557c9881482d350cfb05f2f1cb870638de344581154ca01
32M     /var/lib/docker/containers/5d70c82942083d16593670058aefed339cfe874c9027205b1e6eb8e569894d65
129M    /var/lib/docker/containers/a88d104d20e5ee58ffeaeecbb559b3231c5b8c73ad1443538928ebeae4ff705c
285M    /var/lib/docker/containers/b623602a667c0b31068563f244610a548ed055ff9802197f372ff436a294ab5c
917M    /var/lib/docker/containers/3d71c509ab6aea34400d37f6c006914eed2cb05e6e6cd07b3ee03eb783dc367b
1.4G    /var/lib/docker/containers
```

有三种方式可以清理日志文件

## 清理单个文件

感觉哪个容器的日志太大就清理哪个

```bash
$ sudo sh -c "cat /dev/null > ${log_file}"
```

`${log_file}` 就是日志文件，可以通过 `find` 命令查找全部日志

```bash
$ sudo find /var/lib/docker/containers -name *.log

/var/lib/docker/containers/3d71c509ab6aea34400d37f6c006914eed2cb05e6e6cd07b3ee03eb783dc367b/3d71c509ab6aea34400d37f6c006914eed2cb05e6e6cd07b3ee03eb783dc367b-json.log
/var/lib/docker/containers/0db860afe94df368335c2e96f290275f4c396b996b4e8d22770b01baafd9982c/0db860afe94df368335c2e96f290275f4c396b996b4e8d22770b01baafd9982c-json.log
/var/lib/docker/containers/bc4136199037e73d712614ef57de0915d294cbe51045d213f0d822d71a86cf2c/bc4136199037e73d712614ef57de0915d294cbe51045d213f0d822d71a86cf2c-json.log
/var/lib/docker/containers/5d70c82942083d16593670058aefed339cfe874c9027205b1e6eb8e569894d65/5d70c82942083d16593670058aefed339cfe874c9027205b1e6eb8e569894d65-json.log
/var/lib/docker/containers/6ee184044661c436b44769d56c203f1fc296dbfe08f6ed4cf79aa6fb8cae6659/6ee184044661c436b44769d56c203f1fc296dbfe08f6ed4cf79aa6fb8cae6659-json.log
/var/lib/docker/containers/082564c5bdb19b642491b09419a69061122483c0f959a36eb186dd1fec53c163/082564c5bdb19b642491b09419a69061122483c0f959a36eb186dd1fec53c163-json.log
/var/lib/docker/containers/b623602a667c0b31068563f244610a548ed055ff9802197f372ff436a294ab5c/b623602a667c0b31068563f244610a548ed055ff9802197f372ff436a294ab5c-json.log
/var/lib/docker/containers/66c44231981fcb5ecd33bf0fc3390e71c5cbbabb839d79441eb3317b8500d551/66c44231981fcb5ecd33bf0fc3390e71c5cbbabb839d79441eb3317b8500d551-json.log
/var/lib/docker/containers/a93a4275571b0033367f9cab8213c467b21a03c600e2203195640b5a5bc7f523/a93a4275571b0033367f9cab8213c467b21a03c600e2203195640b5a5bc7f523-json.log
/var/lib/docker/containers/a88d104d20e5ee58ffeaeecbb559b3231c5b8c73ad1443538928ebeae4ff705c/a88d104d20e5ee58ffeaeecbb559b3231c5b8c73ad1443538928ebeae4ff705c-json.log
/var/lib/docker/containers/6bd1f79f16b8b06f2bd203dd84443004ba08c150ac51d23fa620e8b2cbf4b773/6bd1f79f16b8b06f2bd203dd84443004ba08c150ac51d23fa620e8b2cbf4b773-json.log
/var/lib/docker/containers/05fc24ef7a14e31e4557c9881482d350cfb05f2f1cb870638de344581154ca01/05fc24ef7a14e31e4557c9881482d350cfb05f2f1cb870638de344581154ca01-json.log
/var/lib/docker/containers/7bd3a179cf67b1537e0965c1d1f518420ac5d4cd151ecb75c37ada8c2347ca6b/7bd3a179cf67b1537e0965c1d1f518420ac5d4cd151ecb75c37ada8c2347ca6b-json.log
```

或者查看具体容器名称的日志位置

```bash
$ docker inspect --format='{{.LogPath}}' redis
/var/lib/docker/containers/6ee184044661c436b44769d56c203f1fc296dbfe08f6ed4cf79aa6fb8cae6659/6ee184044661c436b44769d56c203f1fc296dbfe08f6ed4cf79aa6fb8cae6659-json.log
```

这样只是解决燃眉之急，并不是长久之计，最好是创建容器时就控制日志的大小.

## 运行时控制

启动容器时，我们可以通过参数来控制日志的文件个数和单个文件的大小

```bash
# max-size 最大数值
# max-file 最大日志数
$ docker run -it --log-opt max-size=10m --log-opt max-file=3 redis
```

一两个容器还好，但是如果有很多容器需要管理，这样就很不方便了，最好还是可以统一管理。

## 全局配置

创建或修改文件 `/etc/docker/daemon.json`，并增加以下配置

```json
{
    "log-driver":"json-file",
    "log-opts":{
        "max-size" :"50m","max-file":"1"
    }
}
```

随后重启 Docker 服务

```bash
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

不过已存在的容器不会生效，需要重建才可以

