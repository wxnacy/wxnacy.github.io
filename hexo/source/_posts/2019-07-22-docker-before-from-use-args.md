---
title: Docker 报错 Please provide a source image with `from` prior to commit
tags:
  - docker
date: 2019-07-22 09:38:03
---


在使用 openresty 的 [docker](https://hub.docker.com/r/openresty/openresty/) 版本时，需要重构镜像，本地测试通过，但服务器上报错。

<!-- more -->
<!-- toc -->

```bash
Please provide a source image with `from` prior to commit
```

Google 后发现问题出在这里

```bash
ARG RESTY_IMAGE_BASE="ubuntu"
ARG RESTY_IMAGE_TAG="bionic"

FROM ${RESTY_IMAGE_BASE}:${RESTY_IMAGE_TAG}
```

在老版本中是不支持 `FROM` 前使用 `ARG` 的，这个问题在 [docker 17.05.0-ce](https://github.com/moby/moby/pull/31352) 版本中得到了修改，而服务器上的版本比较老，所以才报错，只要升级版本即可。
