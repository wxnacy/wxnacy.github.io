---
title: Python 获取当前作用域全部参数的内置方法 locals()
date: 2019-04-17 18:23:31
tags: [python]
---

在写程序时，经常会碰见传递过多参数的情况。先看一个例子

<!-- more -->

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def func1(id, name, age, **kw):
    amount = 1
    duration = 10
    func2(id = id, name = name, age = age, amount = amount, **kw)


def func2(**kw):
    print(kw)
```

在 `func1()` 给 `func2()` 传递参数，一个一个的写真的很痛苦，写一次还好，关键是到处都有这种情况。

可不可以将想要的参数打包直接传递过去呢？

内置方法 `locals()` 就可以达到这个效果，它可以实时收集当前作用域的参数，并返回一个字典。

先在全局范围内看看有哪些参数

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

if __name__ == "__main__":
    print(locals())
```

```bash
$ python locals_demo.py
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x102c75860>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'locals_demo.py', '__cached__': None}
```

可能你到没注意到一个空文件里都有这么多的内置参数。

`locals()` 收集参数是实时进行的，比如我们定义一个参数

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)


if __name__ == "__main__":
    print(locals())
    name = 'wxnacy'
    print(locals())
```

```bash
$ python locals_demo.py

{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1083d5860>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'locals_demo.py', '__cached__': None}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1083d5860>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'locals_demo.py', '__cached__': None, 'name': 'wxnacy'}
```

第二次打印的结果中，就多出了刚刚定义的参数 `name`

在方法中使用也是如此

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def func(**kw):
    name = 'wxnacy'
    print(locals())

if __name__ == "__main__":
    func(url = 'https://wxnacy.com')
```

```bash
$ python locals_demo.py
{'kw': {'url': 'https://wxnacy.com'}, 'name': 'wxnacy'}
```

因为 `locals()` 方法的值是动态变的，所以我们可以先用变量储存起来，并且记得去掉不需要的参数

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def func(id, age, **kw):
    name = 'wxnacy'
    args = locals()
    args.pop('name')
    print(args)
```

或者

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def func(id, age, **kw):
    args = locals()
    name = 'wxnacy'
    print(args)
```

现在再来回顾下开始的问题，这下解决方式简单了很多

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

def func1(id, name, age, **kw):
    amount = 1
    args = locals()
    duration = 10
    func2(**args)

def func2(**kw):
    print(kw)
```

喔噢，我爱 Python。
