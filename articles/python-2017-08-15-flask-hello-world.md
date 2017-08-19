# flask 运行hello world
专辑: [python 如何构建完整项目](/python/2017/08/15/album-build-project)
## 新建项目myproject
首先新建myproject文件夹当做工作目录，进入目录pip下flask依赖包，创建并编辑run.py
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

