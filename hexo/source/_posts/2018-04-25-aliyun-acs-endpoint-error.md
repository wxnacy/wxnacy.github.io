---
title: aliyun 媒体转码报错 Can not find endpoint to access
tags:
  - 开发
date: 2018-04-25 11:25:47
---


在用阿里云没媒体转码功能时报了半天的错误

<!-- more --><!-- toc -->

```bash
Can not find endpoint to access
```

程序里用的是 `oss-cn-beijing` 忽略了是 oss 专用的，换成 `cn-beijing` 则成功。

