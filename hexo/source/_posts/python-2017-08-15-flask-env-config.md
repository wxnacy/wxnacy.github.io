---
title: Flask 如何配置多环境
date: 2017-08-15
tags: [python, flask]
---

> 一个完整的web项目都需要配置数据库连接和开发环境、生产环境灵活切换，今天来在
各个环境中切换数据库连接

<!-- more -->

<!-- toc -->

## 首先添加指定环境脚本
在项目根目录下创建环境脚本 `touch env.sh` 并编辑
```bash
#!/usr/bin/env bash

ENV=$1

if [ ! ${ENV} ]
then
    ENV=local
fi

export PYTHONPATH=./        # 项目跟目录
export FLASK_CONFIG=${ENV}  # 当前环境 可选 local product dev test
```

该文件起到两个作用
1、PYTHONPATH：项目根目录。
2、FLASK_CONFIG：当前环境,使用方法

然后执行命令，使配置生效
```bash
$ source env.sh ${env}      # env=local|product|dev|test 默认local
```

## 添加环境信息文件
```bash
$ mkdir app
$ cd app
$ touch local_config.py
$ vim local_config.py
```

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置文件程序'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."

class ProductionConfig():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@prod.server.org:3306/db_name?charset=utf8mb4'

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@dev.server.org:3306/db_name?charset=utf8mb4'

class TestingConfig():
    DEBUG = True

class LocalConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@127.0.0.1:3306/db_name?charset=utf8mb4'


```
该文件配置了各个环境数据库连接信息

## 添加文件config.py来根据环境读取当前环境内容
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置信息'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."


from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
import os

CONFIG_NAME_MAPPER = {
    'local': 'app.local_config.LocalConfig',
    'product': 'app.local_config.ProductionConfig',
    'dev': 'app.local_config.DevelopmentConfig',
    'test': 'app.local_config.TestingConfig'
}

def create_app(flask_config_name=None):
    """
    创建配置
    :return:
    """
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    env_flask_config_name = os.getenv('FLASK_CONFIG')
    config_mapper_name = flask_config_name or env_flask_config_name or 'local'
    config_name = CONFIG_NAME_MAPPER[config_mapper_name]
    app.config.from_object(config_name)

    return app


app = create_app()

```

## 修改run.py 来读取环境内容
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''配置信息'''
__author__ = "wxnacy(wxnacy@gmail.com)"
__copyright__ = "Copyright of wxnacy (2017)."


from app.config import app

@app.route('/test')
def mysql():
    return app.config['SQLALCHEMY_DATABASE_URI']

app.run()
```

现在项目的目录结构为
```bash
myproject:
    app:
        config.py
        local_config.py
    run.py
    env.sh
```

## 运行
### 本地环境
```bash
$ source env.sh
$ python run.py
$ curl http://localhost:5000/test
mysql+pymysql://root:pass@127.0.0.1:3306/db_name?charset=utf8mb4

$ source env.sh product
$ python run.py
$ curl http://localhost:5000/test
mysql+pymysql://root:pass@prod.server.org:3306/db_name?charset=utf8mb4
```
