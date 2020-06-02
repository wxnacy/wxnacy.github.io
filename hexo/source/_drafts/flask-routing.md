---
title: flask-routing
tags: [python, flask]
---

<!-- more -->
<!-- toc -->

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

>>> from flask import Flask
>>> from pprint import pprint
>>> app = Flask(__name__)
>>> pprint(app.url_map.converters)
{'any': <class 'werkzeug.routing.AnyConverter'>,
 'default': <class 'werkzeug.routing.UnicodeConverter'>,
 'float': <class 'werkzeug.routing.FloatConverter'>,
 'int': <class 'werkzeug.routing.IntegerConverter'>,
 'path': <class 'werkzeug.routing.PathConverter'>,
 'string': <class 'werkzeug.routing.UnicodeConverter'>,
 'uuid': <class 'werkzeug.routing.UUIDConverter'>}
```

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

>>> from flask import Flask
>>> app = Flask(__name__)
>>> @app.route('/<path:wikipage>')
... def wikipage(wikipage):
...     return wikipage
...
>>> app.test_client().get("/test").data
b'test'
>>> app.test_client().get("/test/1").data
b'test/1'
>>> @app.route('/other')
... def other():
...     return 'hello world'
...
>>> app.test_client().get("/other").data
b'hello world'
>>> app.test_client().get("/other/1").data
b'other/1'
```
