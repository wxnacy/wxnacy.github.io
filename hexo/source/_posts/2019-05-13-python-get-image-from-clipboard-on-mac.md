---
title: Python 在 Mac 系统中从剪切板中获取图片
date: 2019-05-13 15:46:09
tags: [python]
---

最近想给 [goss](https://github.com/wxnacy/goss) 加点料，就是省去截完图后，保存本地图片的步骤，而是直接从剪切板里获取图片并上传 Github，这样，如何从剪切板中获取图片就成了关键。

<!-- more -->
<!-- toc -->

本来想着直接使用 `pbcopy` 和 `pbpaste` 命令组合，不过可惜的是它们只能适用于文本。

此时我们需要借助三方包 [Pillow](https://pillow.readthedocs.io/en/stable/)

## 安装

```bash
$ pip install pillow
```

## 获取并保存本地

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from PIL import ImageGrab
from PIL import Image

img = ImageGrab.grabclipboard()
if isinstance(img, Image.Image):
    img.save('test.png', 'png')
```

截图并保存剪切板后，`grabclipboard()` 方法可以获取剪切板中的图片，为了防止出错，我们还要判断取出的数据是否 `Image.Image` 图片类型，随后调用 `save()` 方法保存本地即可。

## 获取并写入到流

不过我希望的不是保存到本地，而是直接写入到流中，再进行二次操作，此时需要借助 io 包，将图片保存到 io 流中。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from PIL import ImageGrab
from PIL import Image
import io

img = ImageGrab.grabclipboard()
img_bytes = io.BytesIO()
if isinstance(img, Image.Image):
    #  img.save('test.png', 'png')
    img.save(img_bytes, 'png')
    print(img_bytes.getvalue())
```

能拿到字节流就可以对其操作，在转换为其它格式，比如 base64，具体方法可以参考 [Convert bytes to base64 HTML img tag](https://www.devdungeon.com/content/grab-image-clipboard-python-pillow#convert_bytes_to_html_base64_img_tag)

- [How to copy a image from clipboard in Python?](https://stackoverflow.com/questions/35254655/how-to-copy-a-image-from-clipboard-in-python?rq=1)
- [Grab Image from Clipboard in Python with Pillow](https://www.devdungeon.com/content/grab-image-clipboard-python-pillow)
