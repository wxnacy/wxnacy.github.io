---
title: Python 使用 Pillow 模块给图片添加文字水印
tags:
  - python
date: 2019-08-29 21:32:37
---


像微博一类的平台上传图片时，平台都会添加一个水印，宣誓着对图片的所有权，我们自己的博客平台也可以给自己的图片添加上水印。

<!-- more -->
<!-- toc -->

还是用 [Pillow](https://github.com/python-pillow/Pillow) 模块来实现

先来看一个简单的例子

```python
>>> from PIL import Image
>>> from PIL import ImageDraw
>>>
>>> image = Image.open('/Users/wxnacy/Downloads/vm-error1.png')
>>> draw = ImageDraw.Draw(image)
>>> draw.text((10, 10), 'wxnacy')
>>> image.show()
```

随后图片的左上角就可以看到水印的添加效果

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/pillow-watermark1.png)

水印的颜色默认为白色，当然可以通过传参改变

```python
>>> draw.text((10, 10), 'wxnacy', (255, 255, 255))
```

添加一个参数，这和上面得到的结果是一样的，这里用的是三原色，`(255, 255, 255)` 分别为红色、绿色、蓝色

最后是字体

```python
>>> from PIL import ImageFont
>>> font=ImageFont.truetype('PingFang.ttc',40)
>>> draw.text((70,300),'This is wxnacy\'s website',(0,255,255), font=font)
>>> image.show()
```

`PingFang.ttc` 必须是本地有的字体文件，`40` 是字体大小，这样最后的水印结果为

![2](https://raw.githubusercontent.com/wxnacy/image/master/blog/pillow-watermark2.png)
