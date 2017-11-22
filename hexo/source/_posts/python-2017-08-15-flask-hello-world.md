---
title: Flask 运行 Hello World
date: 2017-08-15
tags: [python, flask]
---

### 新建项目 myproject
首先新建 myproject 文件夹当做工作目录，进入目录 pip 下 Flask 依赖包，创建并编辑
run.py

<!-- more -->

```bash
$ mkdir myproject
$ cd myproject
$ pip install flask
$ touch run.py
$ vim run.py
```
### run.py
```python
#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello world"

app.run()
```
### 运行
```bash
$ python run.py

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### 访问服务
```bash
$ curl http://127.0.0.1:5000/hello
hello world%
```

### 外部可访问服务器
```python
app.run(host='0.0.0.0')
```

