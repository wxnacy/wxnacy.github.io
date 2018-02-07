---
title: React 发布到 Nginx 中
tags:
  - react
date: 2018-02-07 22:02:46
---


在开发 React 时使用 [create-react-app](https://github.com/facebook/create-react-app) 是非常方便的，它封装的打包功能，让发布 React 应用非常的方便
<!-- more -->
首先在项目根目录下使用 `yarn build` 命令打包，生成的静态文件会在 `myproject/build` 中

Nginx 中作如下配置即可
```bash
server {
    server_name wxnacy.com;
    root /myproject/build;

    location / {
        try_files $uri /index.html;
        add_header   Cache-Control public;
        expires      1d;
    }
}
```
