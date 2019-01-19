---
title: Python 常用装饰器
tags:
  - python
date: 2018-03-08 10:01:36
---


收录一些常用的装饰器

<!-- more --><!-- toc -->
## JSONP
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from functools import wraps

def jsonp(func):
    """Wraps JSONified output for JSONP requests."""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)

    return decorated_function
```

## 跨域
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import make_response
from flask import current_app
from flask import request
from flask import Response
from flask import g
from functools import wraps
from functools import update_wrapper

def cross_domain(origin=None, methods=None, headers=None,
                 max_age=21600, attach_to_all=True,
                 automatic_options=True):
    """跨域"""
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator

```

## 检查必传参数
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from flask import make_response
from flask import current_app
from flask import request
from flask import Response
from flask import g
from flask import jsonify
from functools import wraps
from functools import update_wrapper

def args_required(*params):
    """
    检查参数
    """
    def _wrapper(func):
        @wraps(func)
        def _wrapped(*args, **kwargs):
            content_type = request.content_type
            _args = None
            if content_type == 'application/x-www-form-urlencoded':
                _args = request.form
            elif content_type == 'application/json':
                _args = request.json
            else:
                _args = request.args
            diff = list(params) - dict.fromkeys(list(_args.keys())).keys()
            if diff:
                return make_response(jsonify(
                    {
                        "message": 'args {} is necessary'.format(diff),
                        "status": 403,
                        "version": int(time.time())
                    }
                ), 403)
            return func(*args, **kwargs)

        return _wrapped

    return _wrapper
```
