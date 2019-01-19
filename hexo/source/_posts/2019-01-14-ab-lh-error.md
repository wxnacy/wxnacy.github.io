---
title: Linux ab 使用 localhost 报错
date: 2019-01-14 15:34:36
tags: [linux]
---

使用 ab 测试本地接口时报错

<!-- more --><!-- toc -->
```bash
This is ApacheBench, Version 2.3 <$Revision: 1826891 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)...
Test aborted after 10 failures

apr_socket_connect(): Invalid argument (22)
```

原因在于它无法识别 `localhost` 地址替换为 `127.0.0.1` 即可
