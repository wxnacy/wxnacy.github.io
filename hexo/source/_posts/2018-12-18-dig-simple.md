---
title: dig 写一条最简单的查询 DNS 命令
date: 2018-12-18 18:24:31
tags: [linux]
---

dig（域信息搜索器）命令是一个用于询问 DNS 域名服务器的灵活的工具。它执行 DNS 查询，显示从已查询名称服务器返回的应答。

<!-- more --><!-- toc -->
dig 的功能非常强大，我们这篇不展开讨论，只看最简单的查询域名的 DNS 映射。

```bash
$ dig baidu.com

; <<>> DiG 9.8.3-P1 <<>> baidu.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 28439
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;baidu.com.			IN	A

;; ANSWER SECTION:
baidu.com.		110	IN	A	220.181.57.216
baidu.com.		110	IN	A	123.125.115.110

;; Query time: 198 msec
;; SERVER: 1.1.1.1#53(1.1.1.1)
;; WHEN: Tue Dec 18 18:25:21 2018
;; MSG SIZE  rcvd: 59
```

我们取关键的应答部分

```bash
;; ANSWER SECTION:
baidu.com.		110	IN	A	220.181.57.216
baidu.com.		110	IN	A	123.125.115.110
```

从这里我们可以看到目前 `baidu.com` 域名映射了两个 ip 地址。

这虽然是非常简单的命令行，但却是非常好用的检测工具。如果你不是专业的运维，了解到这个命令，就已经在工作中帮了大忙。
