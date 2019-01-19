---
title: Nginx 异常 unknown directive
tags:
  - nginx
date: 2018-03-30 21:43:14
---

记一个基础知识不好的异常

<!-- more --><!-- toc -->
```bash
nginx: [emerg] unknown directive "if(" in /usr/local/etc/openresty/nginx.conf:85
```
在做地区区分的时候遇到一个上述的异常，废了很大功夫，最后找到原因是 `if` 和 `()` 之间需要有一个空格，呵呵哒，发现真相的我心好累，不想说话，只能赶快记下来加强记忆。
