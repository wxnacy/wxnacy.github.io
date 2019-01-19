---
title: Python 装饰器 decorator
tags:
  - python
date: 2017-12-27 09:12:51
---


为什么会用到装饰器？

<!-- more --><!-- toc -->
## Why
首先谈一个场景，在项目迭代开发过程中，有些函数已经过时，需要删除，但是为了项目的平稳过度又不能立马物理删除，但是需要在别人用到这个函数时，给他一个提醒“这个函数已经过期了，继续使用将不再安全”，当别人看到这个提醒就会意识到以后不再使用，久而久之当所有人都不用时，我们就可以真的删掉这个函数。

如果是在 Java 中那太简单了，使用注解 `@Deprecated` 即可搞定
```java
@Deprecated
private String getName() {
    return 'Hello World'
}
```
Python 中也有类似 `注解` 的功能 `装饰器`。

## What
装饰器是什么？
简单点概况，装饰器允许将**方法或类当做函数传入**，最后**返回一个方法或函数**，并在**不改变原来方法结构**的基础上，完成**额外**的任务。
如果你是 Python 初学者可能对把 `方法当参数传入` 感到困惑，它其实就像这样。
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

def func1():
    print('this is func1')

def func2(func):
    print('{} is deprecated'.format(func))
    func()
    return func

if __name__ == "__main__":
     res = func2(func1)
     print(res)
```
```python
<function func1 at 0x1014f8f28> is deprecated
this is func1
<function func1 at 0x1014f8f28>
```
`func1` 传入 `func2` 中，`func2` 会打印 `func1` 已经过期，并执行它，最后返回它。这样好像已经把 `deprecated` 的功能实现了，但这种用法太别扭了，就好像把装饰器倒过来用了。这只是解释下原理，下面我们来看装饰器该怎么写。
## How
Python 中是没有一个现成的 `@deprecated` 装饰器来让我们用的，需要我们自己来实现一个。
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from functools import wraps

def deprecated(func):
    @wraps(func)
    def warpped(*args, **kwargs):
        """warpped doc"""
        print('args {}'.format(args))
        print('kwargs {}'.format(kwargs))
        print('this {} method is deprecated'.format(func))
        return func(*args, **kwargs)
    return warpped

@deprecated
def get_name(*args, **kwargs):
    """get_name doc"""
    return 'Hello World'

if __name__ == "__main__":
     get_name('wxnacy', 'blog')
     get_name(name='wxnacy')
```
```python
args ('wxnacy', 'blog')
kwargs {}
this <function get_name at 0x10e2ae158> method is deprecated
args ()
kwargs {'name': 'wxnacy'}
this <function get_name at 0x10e2ae158> method is deprecated
```
你大可以先将上面这段代码执行一下，应该会得到后边的结果。如果成功了，那它已经可以工作了，如果你还想要了解装饰器应该怎么写，请往下看。
在方法 `get_name()` 上面跟上 `@deprecated` ，是装饰器的使用方法，没什么可说的。
再看 `deprecated()` 方法，我们可以分为下面几个部分
- **deprecated(func)** 装饰器方法名，将一个方法作为参数
- **@wraps(func)** 内置装饰器，一会儿我再深讲，现在你要知道我们应该带着它
- `warpped(*args, **kwargs)` 内部处理方法，参数为 `func` 所带的参数
- `return func(*args, **kwargs)` 将 `func` 和参数原封不动返回
- `return warpped` 返回内置方法的结果
通过这样的分解，装饰器的构造就已经一目了然了

## wraps
如果你试下把 `@wraps` 去掉，再次运行，它仍然可以工作。你要问了，有它没它都一样，还那么麻烦带着它干啥，网上很多文章也都没有带着它，但是真的没关系吗？先看个例子。
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

def deprecated(func):
    def warpped(*args, **kwargs):
        """warpped doc"""
        print('this {} method is deprecated'.format(func))
        return func(*args, **kwargs)
    return warpped

@deprecated
def get_name(*args, **kwargs):
    """get_name doc"""
    return 'Hello World'

if __name__ == "__main__":
     print(get_name.__name__)   # ==> warpped
     print(get_name.__doc__)    # ==> warpped doc
```
很明显是有问题的，这次我们没有带上 `@wraps` ，然后打印方法的 `__name__, __doc__` ，不管得到的是什么，反正不是我们想要的结果。
> Without the use of this decorator factory, the name of the example function would have been 'wrapper', and the docstring of the original example() would have been lost.

装饰器已经将所调函数包装为另一个函数了，`@wraps` 装饰器就是为了消除这样的副作用。

## 带参数的装饰器
刚才我们使用的装饰器没有额外传递参数，`func` 是默认传递过去的，肯定会有情况需要我们手动传入参数。设想一种情况，我们有一个方法，原来应该从 Mysql 中读取数据，但因为数据量比较大，我们希望每次先从缓存 Redis 中读取数据，如果没有在走 Mysql，我们来模拟一下这种情况。
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from functools import wraps

REDIS_DATA = {"name": "redis-wxnacy"}
MYSQL_DATA = {"name": "mysql-wxnacy"}

def from_cache(key):
    def warpper(func):
        @wraps(func)
        def warpped(*args, **kwargs):
            res = REDIS_DATA.get(key)
            if res:
                return res
            return func(*args, **kwargs)
        return warpped
    return warpper

@from_cache('name')
def get_data():
    res = MYSQL_DATA.get('name')
    return res

def get_data1():
    res = MYSQL_DATA.get('name')
    return res

if __name__ == "__main__":
     print(get_data())      # ==> redis-wxnacy
     print(get_data1())     # ==> mysql-wxnacy
```
同样的方法，区别在于有没有使用装饰器 `@from_cache()` ，分别得到了各自源的数据。

`from_cache()` 方法就是一个可以传递额外参数的装饰器，咋一看很吓人，那么多层，但其实它只是在简单装饰器外边又包了一层，供参数传入，并在 `warpped` 发放中判断应该直接返回数据，还是返回当前传入的方法。

掌握这两种方法，在开发中可以节省很多时间，希望你能多联系，熟能生巧
## 更多模块
### functools.update_wrapper
功能和 `wraps` 类似
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from functools import update_wrapper

def deprecated(func):
    def warpped(*args, **kwargs):
        """warpped doc"""
        print('this {} method is deprecated'.format(func))
        return func(*args, **kwargs)
    return update_wrapper(warpped, func)
```

## 参考资料
- [wraps](https://docs.python.org/2/library/functools.html#functools.wraps)
