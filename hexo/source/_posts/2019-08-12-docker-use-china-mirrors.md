---
title: Docker 配置国内仓库
tags:
  - docker
date: 2019-08-12 21:38:08
---


类似这种需要下载包的一般都要配置个国内的仓库源，同时使用默认的国外仓库，真的很慢。

<!-- more -->
<!-- toc -->

以阿里云仓库为例，配置方式很简单

```bash
$ sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://4qqg0972.mirror.aliyuncs.com"]
}
EOF
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```
