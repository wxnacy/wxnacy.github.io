---
title: Python 使用 Pillow 包实现图片叠加
date: 2019-08-15 17:39:29
tags: [python]
---

[Pillow](https://github.com/python-pillow/Pillow) 包实现图片叠加非常简单

<!-- more -->
<!-- toc -->

## 简单使用

**安装**

```bash
$ pip install Pillow
```

**简单实现**

```python
from PIL import Image

big_image =Image.open('big.jpg')
small_image=Image.open('small.jpg')
# small_image.thumbnail((400,400))  可以实现压缩
big_image.paste(small_image,(157, 45))
big_image.show()
```

**原图**

![1](https://wxnacy.com/images/rss.png)
![2](https://wxnacy.com/images/mp.jpg)

**叠加效果**

![3](https://raw.githubusercontent.com/wxnacy/image/master/blog/pillow_overlay.png)

## 项目中使用

在 web 项目中往往我们不会使用本地图片，大多是对网络图片进行处理，再传到线上，所以首先需要能解析网络图片，其次处理后需要拿到图片二进制，再进行上传处理。

这套逻辑的代码在 https://github.com/wxnacy/study/blob/master/python/pillow_demo/overlay.py

这里复制一份

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 图片叠加

import io

from PIL import Image
import requests


def get_image(path):
    '''通过地址获取 image 对象'''
    image = None
    if path.startswith('http'):
        res = requests.get(path)
        image = Image.open(io.BytesIO(res.content))
    else:
        image = Image.open(path)
    return image

def image2bytes(image):
    '''图片转二进制'''
    img_bytes = io.BytesIO()
    image.save(img_bytes, image.format)
    return img_bytes.getvalue()

def overlay(big_path, small_path, width, height, small_thumbnail=()):
    '''叠加'''
    big_image = get_image(big_path)
    small_image = get_image(small_path)
    if small_thumbnail:
        small_image.thumbnail(small_thumbnail)
    big_image.paste(small_image,(width, height))
    big_image.show()    # 显示图片
    #  big_image.save('/Users/wxnacy/Downloads/pillow_overlay.png')  # 保存
    # 或者返回图片的二进制
    return image2bytes(big_image)


if __name__ == "__main__":
    overlay('https://wxnacy.com/images/rss.png',
            'https://wxnacy.com/images/mp.jpg', 157, 45)
```
