---
title: Flask 操作 Cookie
date: 2018-07-12 18:01:33
tags: [flask]
---

在 FLask 中可以使用 `request, response` 来操作 Cookie

<!-- more --><!-- toc -->
## 设置

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import make_response

@app.route('/set_cookie')
def set_cookie():
    response=make_response('Hello World');
    response.set_cookie('Name','Hyman')
    return response
```

**设置有效期**

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import make_response
from datetime import datetime
from datetime import timedelta

@app.route('/set_cookie')
def set_cookie():
    response=make_response('Hello World');
    outdate=datetime.today() + timedelta(days=30)
    response.set_cookie('Name','Hyman',expires=outdate)
    return response
```

## 获取

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import request

@app.route('/get_cookie')
def get_cookie():
    name=request.cookies.get('Name')
    return name
```

## 删除

**方法一**

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import make_response

@app.route('/del_cookie')
def del_cookie():
    response=make_response('delete cookie')
    response.set_cookie('Name','',expires=0)
    return response
```

**方法二**

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import make_response

@app.route('/del_cookie2')
def del_cookie2():
    response=make_response('delete cookie2')
    response.delete_cookie('Name')
    return response
```
