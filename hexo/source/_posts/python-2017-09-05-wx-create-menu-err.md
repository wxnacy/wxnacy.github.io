---
title: Python 微信公众号接口创建菜单编码问题
date: 2017-09-05
tags: [python, 微信]
---

> 错误 {"errcode":40033,"errmsg":"invalid charset. please check your request, if include \\uxxxx will create fail!"}

<!-- more -->
## 方法
利用 Python 的 json 内置模块，在进行 dumps 操作时，使用 `ensure_ascii=False`
参数是中文不会被转码
```python
data = json.dumps(data,ensure_ascii=False).encode('utf-8')
```

## 完整实例
```python
import json
import requests

url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=...'
data = json.dumps(data,ensure_ascii=False).encode('utf-8')
res = requests.post(url,data=data)
print(res)
```
