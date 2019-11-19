---
title: Nginx 丢失头信息的解决方法
date: 2019-11-19 21:50:46
tags: [nginx]
---

最近在做 web 框架上的一些调整，在本地测试一个接口时发现莫名其妙的报错，调试发现是 Nginx 丢掉了带有下划线的头信息。

<!-- more -->
<!-- toc -->

对比了线上环境的配置文件，发现了确实有个配置不同，缺失了下面的部分

```bash
http {
    ...
    underscores_in_headers on;
    ...
}
```

Nginx 默认情况下配置 `underscores_in_headers off;`，加上上面的配置即可正常请求接口。
