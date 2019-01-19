---
title: Linux 使用 ifconfig 查看本机 ip
date: 2018-10-23 09:59:54
tags: [linux]
---

在终端中使用 `ifconfig` 可以查看本地 ip

<!-- more --><!-- toc -->

在终端中输入 `ifconfig` 可以看到很多的信息，其中包含了本机的 ip，但是信息过多，及时你知道从哪查找，每次看也会头晕，我们需要的精确找到本机 ip 的方法。

在 Linux 中使用命令

```bash
$ ifconfig eth0
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.8.241  netmask 255.255.240.0  broadcast 172.17.15.255
        ether 00:16:3e:0c:ec:10  txqueuelen 1000  (Ethernet)
        RX packets 215013189  bytes 59080762287 (55.0 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 125960779  bytes 124345275246 (115.8 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

第二行的第一个 ip 就是本机 ip `172.17.8.241`

在 MaxOS 中稍有不同，命令为

```bash
$ ifconfig en0
```

接下来我们使用 `grep awk` 来进行精准获取

**CentOS**

```bash
$ ifconfig eth0 | grep inet | grep -v inet6 | awk '{print $2}'
```

**Ubuntu**

```bash
$ ifconfig eth0 | grep inet | grep -v inet6 | awk '{print $2}' | awk -v FS=":" '{print $2}'
```

**MacOS**

```bash
$ ifconfig en0 | grep inet | grep -v inet6 | awk '{print $2}'
```
