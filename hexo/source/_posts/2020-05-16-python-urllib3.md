---
title: Python urllib3 模块
date: 2020-05-16 22:52:35
tags: [python]
---

urllib3 是一个功能强大且友好的 Python HTTP 客户端。大多数 Python 生态系统已经使用 urllib3，包括 [Requests](https://requests.readthedocs.io/) 和 [Pip](https://pip.pypa.io/)

<!-- more -->
<!-- toc -->

## 入门使用

导入模块

```python
>>> import urllib3
```

然后需要一个 PoolManager 实例来发出请求。该对象处理连接池和线程安全性的所有详细信息

```python
>>> http = urllib3.PoolManager()
```

生成一个请求

```python
>>> r = http.request('GET', 'http://httpbin.org/robots.txt')
>>> r.data
b'User-agent: *\nDisallow: /deny\n'
```

`r.data` 以字节的形式返回请求的返回数据

## 常用的返回数据

状态码

```python
>>> r = http.request('GET', 'http://httpbin.org/ip')
>>> r.status
200
```

返回数据

```python
>>> r.data
b'{\n  "origin": "104.232.115.37"\n}\n'
```

头信息

```python
>>> r.headers
HTTPHeaderDict({'Content-Length': '33', ...})
```

获取 JSON 结构数据

```python
>>> import json
>>> json.loads(r.data.decode('utf-8'))
{'origin': '104.232.115.37'}
```

字节数据

```python
>>> r = http.request('GET', 'http://httpbin.org/bytes/8')
>>> r.data
b'\xaa\xa5H?\x95\xe9\x9b\x11'
```

## 常用请求方式

添加头信息

```python
>>> r = http.request(
...     'GET',
...     'http://httpbin.org/headers',
...     headers={
...         'X-Something': 'value'
...     })
```

**地址参数**

GET, HEAD, DELETE 请求添加地址参数

```python
>>> r = http.request(
...     'GET',
...     'http://httpbin.org/get',
...     fields={'arg': 'value'})
>>> json.loads(r.data.decode('utf-8'))['args']
{'arg': 'value'}
```

POST, PUT 请求通常需要将参数进行 urlencode 编码

```python
>>> from urllib.parse import urlencode
>>> encoded_args = urlencode({'arg': 'value'})
>>> url = 'http://httpbin.org/post?' + encoded_args
>>> r = http.request('POST', url)
>>> json.loads(r.data.decode('utf-8'))['args']
{'arg': 'value'}
```

表单参数

```python
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     fields={'field': 'value'})
>>> json.loads(r.data.decode('utf-8'))['form']
{'field': 'value'}
```

JSON 参数


```python
>>> import json
>>> data = {'attribute': 'value'}
>>> encoded_data = json.dumps(data).encode('utf-8')
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     body=encoded_data,
...     headers={'Content-Type': 'application/json'})
>>> json.loads(r.data.decode('utf-8'))['json']
{'attribute': 'value'}
```

文件和字节数据参数

上传文件使用 `multipart/form-data` 编码并制定文件参数为一个元组，内容为 `(file_name, file_data)`

```python
>>> with open('example.txt') as fp:
...     file_data = fp.read()
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     fields={
...         'filefield': ('example.txt', file_data),
...     })
>>> json.loads(r.data.decode('utf-8'))['files']
{'filefield': '...'}
```

也可以指定文件的 `MIME` 类型

```python
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     fields={
...         'filefield': ('example.txt', file_data, 'text/plain'),
...     })
```

要发送原始二进制数据，只需指定 body 参数。最好设置 Content-Type 头字段

```python
>>> with open('example.jpg', 'rb') as fp:
...     binary_data = fp.read()
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     body=binary_data,
...     headers={'Content-Type': 'image/jpeg'})
```

## 设置超时

单次请求可以设置一个 float 类型的超时时间

```python
>>> http.request(
...     'GET', 'http://httpbin.org/delay/3', timeout=4.0)
<urllib3.response.HTTPResponse>
```

也可以使用 `Timeout` 实例来精准的控制连接超时和读取超时

```python
>>> http.request(
...     'GET',
...     'http://httpbin.org/delay/3',
...     timeout=urllib3.Timeout(connect=1.0, read=2.0))
```

或者在`PoolManager` 中设置一个全局的超时配置

```python
>>> http = urllib3.PoolManager(timeout=3.0)
>>> http = urllib3.PoolManager(
...     timeout=urllib3.Timeout(connect=1.0, read=2.0))
```

## 重复请求

默认情况下 urllib3 每次请求会会有 3 次重试的机会和 3 次重定向跳转，也可以使用 `retries` 参数进行设置

比如设置为 10 次

```python
>>> http.requests('GET', 'http://httpbin.org/ip', retries=10)
```

可以设置 `retries=False` 来同时关掉重试和重定向

```python
>>> http.request(
...     'GET', 'http://nxdomain.example.com', retries=False)
NewConnectionError
>>> r = http.request(
...     'GET', 'http://httpbin.org/redirect/1', retries=False)
>>> r.status
302
```

或者只关闭重定向

```python
>>> r = http.request(
...     'GET', 'http://httpbin.org/redirect/1', redirect=False)
>>> r.status
302
```

使用 `Retry` 实例可以分别来控制重试和重定向的次数

比如进行 3 次重试和 2 次重定向

```python
>>> http.request(
...     'GET',
...     'http://httpbin.org/redirect/3',
...     retries=urllib3.Retry(3, redirect=2))
```

最后同样的可以交给 `PoolManager` 进行全局配置

```python
>>> http = urllib3.PoolManager(retries=False)
>>> http = urllib3.PoolManager(
...     retries=urllib3.Retry(5, redirect=2))
```

[更多文档](https://urllib3.readthedocs.io/en/latest/user-guide.html)
