---
title: Docker 镜像 latest 仅仅只是一个标签名
tags:
  - docker
date: 2020-07-24 00:28:18
---


之前没有验证过，一直一厢情愿的认为 `latest` 标签就是最新的意思。

<!-- more -->
<!-- toc -->

然而，然而。

它仅仅只是一个叫 `latest` 的标签而已。

如果说它还有点特殊含义，那就是作为默认标签使用的。

我们试验一下，以 `hello-world` 镜像为例，我们先把它推送到自己的仓库里，标签取名 `1.0.0`

```bash
$ docker pull hello-world
$ docker tag hello-world wxnacy/hello-world:1.0.0
$ docker push wxnacy/hello-world:1.0.0
```

然后删掉本地的镜像

```bash
$ docker image rm wxnacy/hello-world:1.0.0
```

最后试下重新拉取

```bash
$ docker pull wxnacy/hello-world:latest
Error response from daemon: manifest for wxnacy/hello-world:latest not found

$ docker pull wxnacy/hello-world
Using default tag: latest
Error response from daemon: manifest for wxnacy/hello-world:latest not found

$ docker pull wxnacy/hello-world:1.0.0
1.0.0: Pulling from wxnacy/hello-world
Digest: sha256:90659bf80b44ce6be8234e6ff90a1ac34acbeb826903b02cfa0da11c82cbc042
Status: Downloaded newer image for wxnacy/hello-world:1.0.0
```

按照实验结果，只有准确输入标签名 `1.0.0` 时，才能正确下载镜像

而第二次不使用任何标签拉取时，结果提示 `Using default tag: latest`，说明默认标签为 `latest`

总结一下，Docker 的这个行为还是挺违背常理的，如果是默认标签，使用关键字 `default` 岂不是更直观。
