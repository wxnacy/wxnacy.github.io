# Python 微信公众号接口创建菜单编码问题

> 错误 {"errcode":40033,"errmsg":"invalid charset. please check your request, if include \\uxxxx will create fail!"}

## 方法
利用python的json内置模块，在进行dumps操作时，使用ensure_ascii=False 参数是中文
不会被转码
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
