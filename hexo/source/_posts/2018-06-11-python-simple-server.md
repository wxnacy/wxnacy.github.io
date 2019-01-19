---
title: Python 启动最简单服务
tags:
  - python
date: 2018-06-11 14:46:02
---


在 Nginx 做一些运维测试时，需要启动简单服务进行配合，这时候用 Python 是最简单的，可以一行代码搞定

<!-- more --><!-- toc -->

**py2**

```bash
$ python -m SimpleHTTPServer

Serving HTTP on 0.0.0.0 port 8000 ...
```

**py3**

```bash
$ python -m http.server

Serving HTTP on 0.0.0.0 port 8000 ...
```

这样就启动了一个 `8000` 端口的服务，访问

```bash
$ curl localhost:8000
```

得到当前目录列表

更多参数

```bash
$ python -m http.server 8001                # 修改端口
$ python -m http.server --bind 127.0.0.1    # 绑定 ip
```

更多使用见[文档](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.responses)
