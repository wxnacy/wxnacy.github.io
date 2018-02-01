---
title: 微信网页授权登录获取用户信息乱码
tags:
  - python
  - 微信
date: 2018-02-01 09:54:25
---


微信网页授权登录获取用户信息乱码
<!-- more -->
讨厌的微信，经常遇到乱码问题，这次是在网页授权获取用户信息的时候
```bash
https://api.weixin.qq.com/cgi-bin/user/info?access_token=ACCESS_TOKEN&openid=OPENID&lang=zh_CN
```
通过这个接口拿到的用户名等中文信息全都是如下格式的东西
```bash
æ³\x9bæ³\x9bä¹\x8bè¾\x88
```
玛德，一查他们竟然是用 `ISO-8859-1` 格式来编码的，没办法手动转换下

Python 方式如下
```python
res = name.encode('ISO-8859-1').decode('UTF-8')
```
