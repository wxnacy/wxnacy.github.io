---
title: Supervisord 启动报错：unknown error making dispatchers for xxx ： EISDIR
date: 2018-07-15 16:05:13
tags: [python]
---

同事在使用 Supervisord 来启动进程时，报了一个错误。

<!-- more --><!-- toc -->
```bash
unknown error making dispatchers for 'tmd'： EISDIR
```

该错误只看最后的标示即可 `EISDIR` 是目录错误的意思，随后仔细查看配置文件，发现 `stdout_logfile` 配置的文件名与当前系统一个文件夹重名导致，修改后，重启搞定
