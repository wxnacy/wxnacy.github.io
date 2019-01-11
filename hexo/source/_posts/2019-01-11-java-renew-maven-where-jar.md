---
title: 重新学 Java 系列：Maven 下载的 jar 包去哪了
tags:
  - java
date: 2019-01-11 18:18:45
---


> 这个是一个系列阅读，关于为什么重新学习，我在文章 [重新学 Java 系列：新系列、新开始](/2018/12/29/java-renew-why/)(https://wxnacy.com/2018/12/29/java-renew-why/) 中有提到，这个系列是在有 Java 基础的情况下，重新学习讨论一下以前可能忽略掉，或者没理解的知识细节，我想要永远在学习的路上。

<!-- more --><!-- toc -->
## 本地仓库
在 Maven 项目中，`pom.xml` 文件中的 `dependencies` 节点为项目需要的数据包，那编
译运行时 jar 包都下载到哪里呢？

Maven 有本地的仓库，地址默认为 `~/.m2/repository`

进入目录会发现，本地所以项目的依赖包都以包名加版本号的形式存放在里边，例如

```bash
$ cd ~/.m2/repository/org/jdom/jdom/1.1
$ tree
.
├── _remote.repositories
├── jdom-1.1.jar
├── jdom-1.1.jar.sha1
├── jdom-1.1.pom
└── jdom-1.1.pom.sha1

0 directories, 5 files
```

本地仓库的位置可以通过配置文件修改

```bash
$ vim /usr/local/Cellar/maven/3.6.0/libexec/conf/settings.xml
```

```bash
<localRepository>/path/to/local/repo</localRepository>
```

## 安装本地项目到仓库

假如我们写完一个项目，希望它可以像其他 jar 包一样，可以在其他项目中使用，首先我们可以先安装到本地仓库。

根目录下执行安装命令即可

```bash
$ mvn install
```

