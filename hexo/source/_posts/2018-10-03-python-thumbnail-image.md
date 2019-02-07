---
title: Python 压缩图片
date: 2018-10-03 16:44:08
tags: [python]
---

Python 可以使用 Pillow 模块操作图片。

<!-- more --><!-- toc -->

安装详见文档 [https://pillow.readthedocs.io/en/stable/installation.html](https://pillow.readthedocs.io/en/stable/installation.html)

```python
from PIL import Image

def thumbnail(path, savefile='', q=50):
    '''压缩并保存到文件'''
    img = Image.open(path)
    w, h = img.size
    width, height = w * q // 100, h * q // 100
    img.thumbnail((width, height))
    if not savefile:
        savefile = '{}_{}x{}.{}'.format(
            path, width, height, img.format.lower())
    img.save(savefile, img.format)

def thumbnail_to_bytes(cls, path, q=50):
    '''压缩并返回字节数据'''
    img = Image.open(path)
    w, h = img.size
    width, height = w * q // 100, h * q // 100
    img.thumbnail((width, height))
    img_bytes = io.BytesIO()
    img.save(img_bytes, img.format)
    return img_bytes.getvalue()

thumbnail('test.png', 'new_test.png')
thumbnail_to_bytes('test.png')
```
