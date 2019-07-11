---
title: Nginx http 强制跳转 https 地址
tags:
  - nginx
date: 2018-05-30 13:55:35
---

`https` 越来越普及，但是当用户自己访问 `http` 是控制不了的，所以强制跳转的功能就必不可少了，下面是几种强制跳转的方法

<!-- more -->
<!-- toc -->

## return 301

返回 301 错误，并跳转到 https 地址
```bash
server {
    listen       80;
    server_name  wxnacy.com;
    return       301 https://$server_name$request_uri;
}
```

## rewrite

将 http 请求重写到 https 地址

```bash
rewrite ^ https://$server_name$request_uri? permanent;
```

两者相比，`301` 的方式在搜索引擎速度上要块一些。

## error_page 497

```bash
error code 497: normal request was sent to HTTPS
```

在一个站点只允许 https 访问时, 如果使用 http 访问会报出497错误码

```bash
error_page 497  https://$host$uri?$args;
```

## index.html refresh

百度页面 `http://baidu.com` 自动跳转 `http://www.baidu.com` 是灵活利用了 `meta` 的刷新属性

```bash
> $ curl http://baidu.com

<html>
<meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
</meta>html>
```


