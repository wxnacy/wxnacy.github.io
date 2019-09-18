---
title: 使用 Python 新建微信公众号临时素材
tags:
  - 微信
  - python
date: 2019-09-18 15:23:48
---


微信公众号相关的官方文档一直是以垃圾著称的，比如这个[新建临时素材](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1444738726)。

<!-- more -->
<!-- toc -->

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/wx-media1_1031.png)

接口调用的说明，只有一个 `curl` 的例子，真是 fuck 啊，

我也只能从 media 参数的说明中做一下文章，微信的文档要是没有点知识储备还真用不了。

这里说一下使用 Python 来完成的 demo

关键在于 media 字段包含的三个字段，可以使用 requests 模块来模拟上传文件

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

url = 'https://api.weixin.qq.com/cgi-bin/media/upload'
params = {"access_token": 'access_token', "type": 'image'}
files = { 'media' : ('tmp.jpg', content, content_type)}
res = requests.post(url, params=params, files=files)
res = json.loads(str(res.content, 'utf8'))
```

