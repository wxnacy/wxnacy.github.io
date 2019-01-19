---
title: HTTP Accept-Ranges 头信息的作用
tags:
  - http
date: 2018-09-05 17:17:54
---


最近想写一个断点下载视频的小工具，发现头信息 `Accept-Ranges` 在里面发挥了非常大的作用。

<!-- more --><!-- toc -->

比如请求百度官网

```bash
$ curl https://www.baiud.com -I

HTTP/1.1 200 OK
Accept-Ranges: bytes
Cache-Control: private, no-cache, no-store, proxy-revalidate, no-transform
Connection: Keep-Alive
Content-Length: 277
Content-Type: text/html
Date: Tue, 04 Sep 2018 09:41:52 GMT
Etag: "575e1f60-115"
Last-Modified: Mon, 13 Jun 2016 02:50:08 GMT
Pragma: no-cache
Server: bfe/1.0.8.18
```

其中 `Accept-Ranges` 返回值为 `bytes`，这代表了该服务器可以接受范围请求，这样我们就可以做断点下载的功能了。如果该值为 `none`，则代表不允许范围请求。

我们可以通过请求头 `Range` 来定义获取的字节范围，格式为 `bytes=0-8`

**使用 curl 来请求**

```bash
$ curl https://www.baidu.com --header "Range: bytes=0-8"

<!DOCTYPE%
```

看到请求回来的数据只有 9 个字节

我们也可以使用更简单的方式请求

```bash
$ curl https://www.baidu.com -r 0-8

<!DOCTYPE%
```

利用这个特性，再加上多线程运行，即可写出下载更快的工具。

- [译-实践HTTP206状态:部分内容和范围请求](http://www.cnblogs.com/ziyunfei/archive/2012/11/18/2775499.html)
- [Accept-Ranges](https://cloud.tencent.com/developer/section/1189892)
