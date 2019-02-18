---
title: Python 使用 gunicorn 启动你的项目
date: 2017-08-15
tags: [python]
---

> 虽然 Python 自带服务器服务，但是最多只能用作开发环境调试用，在生产环境中如同玩具一样，一碰就坏，今天给大家介绍使用 gunicorn 启动 Python 项目

<!-- more --><!-- toc -->

## 安装
```bash
$ pip install gunicorn
```

## 启动
```bash
$ gunicorn run:app

[2017-08-15 15:25:28 +0800] [26628] [INFO] Starting gunicorn 19.7.1
[2017-08-15 15:25:28 +0800] [26628] [INFO] Listening at: http://127.0.0.1:8000 (26628)
[2017-08-15 15:25:28 +0800] [26628] [INFO] Using worker: sync
[2017-08-15 15:25:28 +0800] [26631] [INFO] Booting worker with pid: 26631
```

## 配置参数
### 命令行参数

```bash
$ gunicorn -w 2 -b 0.0.0.0:8000 run:app
```
其中` -b 或 --bind ` 指定项目启动绑定域名和端口，` -w 或 --workers` 指定启动几个进程

**异步进程**

虽然启动了两个进程，但它并不是异步进行，我需要指定实现异步进程的类，通常我们使用 `gevent`

下载

```bash
$ pip install gevent
```

使用

```bash
$ gunicorn -w 2 -b 0.0.0.0:8000 -k gevent run:app
```

其中 `-k, --worker-class` 可以指定异步进程类

### 配置参数文件
在项目根目录下创建配置文件 `touch gunicorn_config.py` 并编辑
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
配置信息
https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

import multiprocessing

bind = '0.0.0.0:8002' # 绑定地址
workers =  multiprocessing.cpu_count() * 2 + 1 # 根据cpu数量指定线程数量
worker_class = 'gevent' # 异步进程类

```
启动
```bash
$ gunicorn -c gunicorn_config.py run:app
```

[更多配置](http://docs.gunicorn.org/en/stable/settings.html)
