---
title: Python 最常用的网络请求模块 Requests
date: 2018-10-10 15:49:06
tags: [python]
---

> Requests是一个优雅而简单的Python HTTP库，专为人类而构建。

<!-- more --><!-- toc -->
## 安装

```bash
$ pip install requests
```

## Request

```python
>>> import requests

>>> r = requests.get('https://httpbin.org/get', params= {'key': 'value'})
>>> r = requests.put('https://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('https://httpbin.org/delete', headers={'key': 'value'})
>>> r = requests.head('https://httpbin.org/get', cookies={'key': 'value'})
>>> r = requests.options('https://httpbin.org/get', timeout=0.01)
```

### Cookies

```python
>>> url = 'https://httpbin.org/cookies'
>>> cookies = dict(cookies_are='working')

>>> r = requests.get(url, cookies=cookies)
>>> r.text
'{"cookies": {"cookies_are": "working"}}'
```

```python
>>> jar = requests.cookies.RequestsCookieJar()
>>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
>>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
>>> url = 'https://httpbin.org/cookies'
>>> r = requests.get(url, cookies=jar)
>>> r.text
'{"cookies": {"tasty_cookie": "yum"}}'
```

### 上传文件

```python
>>> url = 'https://httpbin.org/post'
>>> files = {'file': open('report.xls', 'rb')}

>>> r = requests.post(url, files=files)
>>> r.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
```

```python
>>> url = 'https://httpbin.org/post'
>>> files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

>>> r = requests.post(url, files=files)
>>> r.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
```

```python
>>> url = 'https://httpbin.org/post'
>>> files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

>>> r = requests.post(url, files=files)
>>> r.text
{
  ...
  "files": {
    "file": "some,data,to,send\\nanother,row,to,send\\n"
  },
  ...
}
```

## Response

```python
>>> import requests

>>> r = requests.get('https://api.github.com/events')
>>> r.status_code
200

>>> r.url
'https://api.github.com/events'

>>> r.text
u'[{"repository":{"open_issues":0,"url":"https://github.com/...

>>> r.encoding
'utf-8'

>>> r.content
b'[{"repository":{"open_issues":0,"url":"https://github.com/...

>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...

>>> r.raw
<urllib3.response.HTTPResponse object at 0x101194810>

>>> r.raw.read(10)
'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
```

### 头信息

```python
>>> r.headers
{
    'content-encoding': 'gzip',
    'transfer-encoding': 'chunked',
    'connection': 'close',
    'server': 'nginx/1.0.4',
    'x-runtime': '148ms',
    'etag': '"e1ca502697e5c9317743dc078f67693f"',
    'content-type': 'application/json'
}

>>> r.headers['Content-Type']
'application/json'

>>> r.headers.get('content-type')
'application/json'
```

### Cookies

```python
>>> url = 'http://example.com/some/cookie/setting/url'
>>> r = requests.get(url)

>>> r.cookies['example_cookie_name']
'example_cookie_value'
```

- [Requests](http://docs.python-requests.org/en/master/user/quickstart/)
