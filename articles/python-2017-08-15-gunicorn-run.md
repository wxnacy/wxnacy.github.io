# 使用 gunicorn 启动你的项目

专辑: [python 如何构建完整项目](/python/2017/08/15/album-build-project)

> 虽然python自带服务器服务，但是最多只能用作开发环境调试用，在生产环境中如同玩具一样，一碰就坏，今天给大家介绍使用gunicorn启动python项目

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
其中``` -b 或 --bind ``` 指定项目启动绑定域名和端口，``` -w 或 --workers``` 指定启动几个线程

### 配置参数文件
touch gunicorn_config.py && vim gunicorn.py
```bash
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

```
启动
```bash
$ gunicorn -c gunicorn_config.py run:app
```

更多配置:[http://docs.gunicorn.org/en/stable/settings.html](http://docs.gunicorn.org/en/stable/settings.html)