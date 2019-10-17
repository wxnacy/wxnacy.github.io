---
title: Nginx 报警告 the "ssl" directive is deprecated
date: 2019-10-17 14:51:04
tags: [nginx]
---

一直用的一个配置文件，在用 docker 启动的 openresty 时，突然报了一堆警告

<!-- more -->
<!-- toc -->

```bash
nginx: [warn] the "ssl" directive is deprecated, use the "listen ... ssl" directive instead in /usr/local/openresty/nginx/conf/conf.d/biz.conf:4
```

因为只是警告，所以程序可以正常运行，但每次都报还是很闹心，经查后发现还是版本问题。

在升级[日志](http://nginx.org/en/CHANGES)中是这样说的

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/nginx-ssl-deprecated.png)

`ssl on;` 的用法已经过时了，现在 `https` 需要使用 `listen ... ssl` 格式来标记。

就像这样

```bash
server {
    listen 443 ssl;
    ...
}
```
