---
title: Python 使用 Requests 模块进行身份验证
tags:
  - python
date: 2019-07-17 10:46:27
---


[Requests](https://github.com/kennethreitz/requests) 可以说是 Python 最好用的 http 模块，没有之一。

<!-- more -->

它对于身份验证有非常方便的使用规则。

**基本身份验证**

```python
>>> from requests.auth import HTTPBasicAuth
>>> requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
<Response [200]>
```

因为这种验证非常常用，所以也提供了方便的写法。

```python
>>> requests.get('https://api.github.com/user', auth=('user', 'pass'))
<Response [200]>
```

**摘要式身份认证**

```python
>>> from requests.auth import HTTPDigestAuth
>>> url = 'http://httpbin.org/digest-auth/auth/user/pass'
>>> requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
<Response [200]>
```

**OAuth 1**

```python
>>> import requests
>>> from requests_oauthlib import OAuth1
>>> url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
>>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
...               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
>>> requests.get(url, auth=auth)
<Response [200]>
```

更多复杂验证如 OAuth 2，请参看[文档](http://docs.python-requests.org/zh_CN/latest/user/authentication.html?highlight=requests.auth#oauth-2-openid)
