---
title: Nginx 报错 no resolver defined to resolve
tags:
  - nginx
date: 2019-07-16 14:49:25
---


起因是使用 `ngxin + lua` 链接外部机器 Redis 时产生的

<!-- more -->
<!-- toc -->

原因是 Nginx 0.6.18以后的版本中启用了一个resolver指令，在使用变量来构造某个server地址的时候一定要用resolver指令来指定DNS服务器的地址，所以解决这个问题的方法很简单：在nginx的配置文件中的http{}部分添加一行DNS地址即可

```bash
http {
    resolver 8.8.8.8;
    server {
        ...
    }
}
```

如果机器支持 ipv6，可以去掉对它的支持，免得产生类似错误。

```bash
resolver 8.8.8.8 ipv6=off;
```

- [No resolver defined to resolve](https://github.com/openresty/lua-resty-redis/issues/159)
