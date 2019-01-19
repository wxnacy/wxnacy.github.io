---
title: Ubuntu 如何安装 Java 11
tags:
  - java
date: 2018-12-26 10:56:36
---


几个月前我写过文章 [Ubuntu 16.04 安装 JDK](/2018/06/19/ubuntu-install-jdk/) ，当时是以 JDK 8 为例子，现在 Java 11 出来了，相应的更新一版。

<!-- more --><!-- toc -->

我们首选使用 apt 来进行安装管理

## Oracle JDK

首先添加 LinuxUprising Java PPA 仓库到软件源中，并下载 Oracle Java 11

```bash
$ sudo add-apt-repository ppa:linuxuprising/java
$ sudo apt update
$ sudo apt install oracle-java11-installer
```

```bash
$ java -version
java version "11.0.1" 2018-10-16 LTS
Java(TM) SE Runtime Environment 18.9 (build 11.0.1+13-LTS)
Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.1+13-LTS, mixed mode)
```

## OpenJDK

### 18.04 LTS

首先我们使用 `apt` 进行搜索

```bash
$ sudo apt search openjdk
```

如果你的系统版本足够新，比如 18.04 LTS，那么很有可能搜索出这样的条目

```bash
openjdk-11-jdk/bionic-updates,bionic-security,now 10.0.2+13-1ubuntu0.18.04.4 amd64 [installed,automatic]
  OpenJDK Development Kit (JDK)
```

这代表软件源已经更新了 Java 11，这样直接安装默认版本即可

```bash
$ sudo apt install -y default-jdk
```

### 更老版本

如果是更早的版本，那么很大程度上并没有更新该源，那么这时候我们需要使用 tar 包进行安装

```bash
$ wget https://download.java.net/java/GA/jdk11/28/GPL/openjdk-11+28_linux-x64_bin.tar.gz -O /tmp/openjdk-11+28_linux-x64_bin.tar.gz
$ sudo tar xfvz /tmp/openjdk-11+28_linux-x64_bin.tar.gz --directory /usr/lib/jvm
$ rm -f /tmp/openjdk-11+28_linux-x64_bin.tar.gz
```

使用 `update-alternatives` 对它进行管理

```bash
$ sudo sh -c 'for bin in /usr/lib/jvm/jdk-11/bin/*; do update-alternatives --install /usr/bin/$(basename $bin) $(basename $bin) $bin 100; done'
$ sudo sh -c 'for bin in /usr/lib/jvm/jdk-11/bin/*; do update-alternatives --set $(basename $bin) $bin; done'
```

最后查看 java 版本

```bash
$ java -version
openjdk version "10.0.2" 2018-07-17
OpenJDK Runtime Environment (build 10.0.2+13-Ubuntu-1ubuntu0.18.04.4)
OpenJDK 64-Bit Server VM (build 10.0.2+13-Ubuntu-1ubuntu0.18.04.4, mixed mode)
```

## 切换版本

现在我们已经有两个版本的 Java，我们可以通过 `update-alternatives` 来选择一个作为默认版本

```bash
$ sudo update-alternatives --config java
There are 2 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                  Priority   Status
------------------------------------------------------------
  0            /usr/lib/jvm/java-11-oracle/bin/java   1091      auto mode
* 1            /usr/lib/jvm/java-11-oracle/bin/java   1091      manual mode
  2            /usr/lib/jvm/jdk-11/bin/java           100       manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

随后输入 `Selection` 对应的数字即可完成切换

- [Java SE Development Kit 11 Downloads](https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html)
- [Installing OpenJDK 11 on Ubuntu 18.04](https://dzone.com/articles/installing-openjdk-11-on-ubuntu-1804-for-real)
- [How To Install Oracle Java 11 In Ubuntu, Linux Mint Or Debian (From PPA Repository)](https://www.linuxuprising.com/2018/10/how-to-install-oracle-java-11-in-ubuntu.html)
