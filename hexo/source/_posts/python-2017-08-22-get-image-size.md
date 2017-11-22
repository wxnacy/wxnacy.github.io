---
title: Python 获取本地或网络图片的宽高
date: 2017-08-22
tags: [python]
---


## 本地
```python
from PIL import Image
fp = '/Users/wxnacy/Documents/WX20170412-190958@2x.png'
i = Image.open(fp)
print(i.size) # 获取宽高 (w,h)
print(i.format) # 获取图片格式
```

## 网络图片
```python
from PIL import Image
import io
import requests
url = ''
i = Image.open(io.BytesIO(requests.get(url).content))
print(i.size) # 获取宽高 (w,h)
print(i.format) # 获取图片格式
```
