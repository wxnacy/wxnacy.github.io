---
title: Python Flask 程序热启动的几种方式
date: 2020-05-19 17:29:02
tags: [python, flask]
---

记录几种热启动的方式

<!-- more -->
<!-- toc -->

## app.run

使用 `app.run(debug=True)`

编辑文件 `app.py`

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import Flask

app = Flask(__name__)

@app.route('/')
async def main():
    return "Hello World"

if __name__ == "__main__":
     app.run(debug=True)
```

运行即可

```bash
$ python app.py
```

或者

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

...
    app.debug = True
    app.run()
```

## flask run

使用 `flask` 运行

```bash
$ FLASK_APP=app FLASK_ENV=development flask run
```

或者


```bash
$ FLASK_APP=app FLASK_DEBUG=1 flask run
```

脚本运行则这样编写

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
