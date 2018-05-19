---
title: CentOS 安装 Htop
tags:
  - linux
date: 2018-05-19 15:34:01
---


Htop 的强大和方便不在赘述，直说一下在 CentOS 系统中如何安装。
<!-- more -->

**使用 EPEL 仓库**

```bash
$ yum -y install epel-release
$ yum -y update
```

接下来正常安装即可

```bash
$ yum -y install htop
```

