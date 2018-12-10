---
title: Supervisord 启动报错
date: 2018-12-10 17:04:38
tags: [python]
---

> error: <class 'socket.error'>, [Errno 2] No such file or directory: file: /usr/lib/python2.7/socket.py line: 224

<!-- more --><!-- toc -->
如上，如果 supervisord 正常启动过，突然报这个错误，则有可能是非正常关闭导致的。

此时，需要强行关闭后，再正常启动即可。

关闭

```bash
$ sudo kill -9 `ps aux | grep supervisord | aws '{print $2}'`
```

启动

```bash
$ sudo /bin/supervisord -c /etc/supervisord/supervisord.conf
```
