---
title: Ubuntu 16.04 安装 JDK
tags:
  - linux
  - java
date: 2018-06-19 12:34:16
---

***现以更新安装 Java 11 版本，传送门 [Ubuntu 如何安装 Java 11](/2018/12/26/ubuntu-install-jdk11/)***

Ubuntu 安装 JDK 与 CentOS 很相似，但更简单。

<!-- more --><!-- toc -->

## OpenJDK

查找 JDK

```bash
$ sudo apt update -y
$ sudo apt search jdk

default-jdk/xenial 2:1.8-56ubuntu2 amd64
  Standard Java or Java compatible Development Kit

default-jdk-doc/xenial 2:1.8-56ubuntu2 amd64
  Standard Java or Java compatible Development Kit (documentation)

default-jdk-headless/xenial 2:1.8-56ubuntu2 amd64
  Standard Java or Java compatible Development Kit (headless)

default-jre/xenial 2:1.8-56ubuntu2 amd64
  Standard Java or Java compatible Runtime

default-jre-headless/xenial 2:1.8-56ubuntu2 amd64
  Standard Java or Java compatible Runtime (headless)

openjdk-8-dbg/xenial-updates,xenial-security 8u171-b11-0ubuntu0.16.04.1 amd64
  Java runtime based on OpenJDK (debugging symbols)

openjdk-8-demo/xenial-updates,xenial-security 8u171-b11-0ubuntu0.16.04.1 amd64
  Java runtime based on OpenJDK (demos and examples)

openjdk-8-doc/xenial-updates,xenial-security 8u171-b11-0ubuntu0.16.04.1 all
  OpenJDK Development Kit (JDK) documentation

openjdk-8-jdk/xenial-updates,xenial-security 8u171-b11-0ubuntu0.16.04.1 amd64
  OpenJDK Development Kit (JDK)

openjdk-8-jdk-headless/xenial-updates,xenial-security 8u171-b11-0ubuntu0.16.04.1 amd64
  OpenJDK Development Kit (JDK) (headless)

openjdk-8-jre/xenial-updates,xenial-security 8u171-b11-0ubuntu0.16.04.1 amd64
  OpenJDK Java runtime, using Hotspot JIT

openjdk-8-jre-headless/xenial-updates,xenial-security 8u171-b11-0ubuntu0.16.04.1 amd64
  OpenJDK Java runtime, using Hotspot JIT (headless)

openjdk-8-jre-jamvm/xenial-updates,xenial-security 8u171-b11-0ubuntu0.16.04.1 amd64
  Transitional package for obsolete JamVM for OpenJDK

openjdk-8-source/xenial-updates,xenial-security 8u171-b11-0ubuntu0.16.04.1 all
  OpenJDK Development Kit (JDK) source files
```

下载指定版本

```bash
$ sudo apt install -y openjdk-8-jdk
```

或直接下载默认版本

```bash
$ sudo apt install -y default-jdk
```

## Oracle JDK

Ubuntu 安装 Oracle JDK 要方便的很多

添加 Oracle PPA 到软件仓库中

```bash
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt update -y
```

下载

```bash
$ sudo apt-get install oracle-java8-installer
```

## 选择版本

```bash
$ sudo update-alternatives --config java

There are 2 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                            Priority   Status
------------------------------------------------------------
  0            /usr/lib/jvm/java-8-oracle/jre/bin/java          1081      auto mode
  1            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      manual mode
* 2            /usr/lib/jvm/java-8-oracle/jre/bin/java          1081      manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

`*` 为当前选中版本，输入相应数字即可更改版本

- [How To Install Java with Apt-Get on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04)
