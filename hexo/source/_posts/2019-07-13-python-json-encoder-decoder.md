---
title: Python 对 JSON 中的特殊类型进行 Encoder
tags:
  - python
date: 2019-07-13 09:56:59
---


Python 处理 JSON 数据时，`dumps` 函数是经常用到的，当 JSON 数据中有特殊类型时，往往是比较头疼的，因为经常会报这样一个错误。

<!-- more -->
<!-- toc -->

## 自定义编码类

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import json
from datetime import datetime

USER_DATA = dict(
    id = 1, name = 'wxnacy', ts = datetime.now()
)
print(json.dumps(USER_DATA))
```

```bash
Traceback (most recent call last):
  File "/Users/wxnacy/PycharmProjects/study/python/office_module/json_demo/dumps.py", line 74, in <module>
    dumps_encoder()
  File "/Users/wxnacy/PycharmProjects/study/python/office_module/json_demo/dumps.py", line 68, in dumps_encoder
    print(json.dumps(USER_DATA))
  File "/Users/wxnacy/.pyenv/versions/3.6.0/Python.framework/Versions/3.6/lib/python3.6/json/__init__.py", line 231, in dumps
    return _default_encoder.encode(obj)
  File "/Users/wxnacy/.pyenv/versions/3.6.0/Python.framework/Versions/3.6/lib/python3.6/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/Users/wxnacy/.pyenv/versions/3.6.0/Python.framework/Versions/3.6/lib/python3.6/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/Users/wxnacy/.pyenv/versions/3.6.0/Python.framework/Versions/3.6/lib/python3.6/json/encoder.py", line 180, in default
    o.__class__.__name__)
TypeError: Object of type 'datetime' is not JSON serializable
```

原因在于 `dumps` 函数不知道如何处理 `datetime` 对象，默认情况下 `json` 模块使用 `json.JSONEncoder` 类来进行编码，此时我们需要自定义一下编码类。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class CustomEncoder(json.JSONEncoder):
    def default(self, x):
        if isinstance(x, datetime):
            return int(x.timestamp())
        return super().default(self, x)
```

定义编码类 `CustomEncoder` 并重写实例的 `default` 函数，对特殊类型进行处理，其余类型继续使用父类的解析。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import json
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, x):
        if isinstance(x, datetime):
            return int(x.timestamp())
        return super().default(self, x)

USER_DATA = dict(
    id = 1, name = 'wxnacy', ts = datetime.now()
)
print(json.dumps(USER_DATA, cls=CustomEncoder))
# {"id": 1, "name": "wxnacy", "ts": 1562938926}
```

最后整合起来，将类使用 `cls` 参数传入 `dumps` 函数即可。

使用 `CustomEncoder` 实例的 `encode` 函数可以对对象进行转码

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
print(CustomEncoder().encode(datetime.now()))
# 1562939035
```

在父类源码中，所有的编码逻辑都在 `encode` 函数中，`default` 只负责抛出 `TypeError` 异常，这就是文章开始报错的出处。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def default(self, o):
    """Implement this method in a subclass such that it returns
    a serializable object for ``o``, or calls the base implementation
    (to raise a ``TypeError``).

    For example, to support arbitrary iterators, you could
    implement default like this::

        def default(self, o):
            try:
                iterable = iter(o)
            except TypeError:
                pass
            else:
                return list(iterable)
            # Let the base class default method raise the TypeError
            return JSONEncoder.default(self, o)

    """
    raise TypeError(f'Object of type {o.__class__.__name__} '
                    f'is not JSON serializable')

def encode(self, o):
    """Return a JSON string representation of a Python data structure.

    >>> from json.encoder import JSONEncoder
    >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
    '{"foo": ["bar", "baz"]}'

    """
    # This is for extremely simple cases and benchmarks.
    if isinstance(o, str):
        if self.ensure_ascii:
            return encode_basestring_ascii(o)
        else:
            return encode_basestring(o)
    # This doesn't pass the iterator directly to ''.join() because the
    # exceptions aren't as detailed.  The list call should be roughly
    # equivalent to the PySequence_Fast that ''.join() would do.
    chunks = self.iterencode(o, _one_shot=True)
    if not isinstance(chunks, (list, tuple)):
        chunks = list(chunks)
    return ''.join(chunks)
```

## 单分派装饰器处理对象

`CustomEncoder` 如果处理的对象种类很多的话，需要写多个 `if elif else` 来区分，这样并不是不行，但是不够优雅，不够 pythonic

根据对象的类型不同，而做出不同的处理。刚好有个装饰器可以做到这点，它就是单分派函数 `functools.singledispatch`

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from datetime import datetime
from datetime import date
from functools import singledispatch

class CustomEncoder(json.JSONEncoder):
    def default(self, x):
        try:
            return encode(x)
        except TypeError:
            return super().default(self, x)

@singledispatch             # 1
def encode(x):
    raise TypeError('Unencode type')

@encode.register(datetime)  # 2
def _(x):
    return int(x.timestamp())

@encode.register(date)
def _(x):
    return x.isoformat()

print(json.dumps(dict(dt = datetime.now(), d = date.today()), cls=CustomEncoder))
# {"dt": 1562940781, "d": "2019-07-12"}
```

- 1 使用 `@singledispatch` 装饰 `encode` 函数，是他处理默认类型。同时给他添加一个装饰器构造函数变量。
- 2 `@encode.register()` 是一个装饰器构造函数，接收需要处理的对象类型作为参数。用它装饰的函数不需要名字，*_* 代替即可。

最后提一点，`json` 也可以在命令行中使用

```bash
$ echo '{"json": "obj"}' | python -m json.tool
{
    "json": "obj"
}
```

- [json](https://docs.python.org/3/library/json.html)
