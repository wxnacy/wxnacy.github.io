---
title: CentOS 安装 JDK
date: 2018-06-15 14:49:09
tags: [linux, java]
---

***现以更新安装 Java 11 版本，传送门 [CentOS 7 如何安装 Java 11](/2018/12/27/centos7-install-java11/)***

Java 最常用的安装方式是从[官网](http://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html)下载 `tar.gz` 文件，解压后配置环境变量，这样的安装方式并不利于自动化，今天来看下通过 `rpm` 的安装方式。

<!-- more --><!-- toc -->

## OpenJDK

首先搜索可安装的 JDK

```bash
$ sudo yum search jdk
```

```bash
java-1.6.0-openjdk.x86_64 : OpenJDK Runtime Environment
java-1.6.0-openjdk-demo.x86_64 : OpenJDK Demos
java-1.6.0-openjdk-devel.x86_64 : OpenJDK Development Environment
java-1.6.0-openjdk-javadoc.x86_64 : OpenJDK API Documentation
java-1.6.0-openjdk-src.x86_64 : OpenJDK Source Bundle
java-1.7.0-openjdk.x86_64 : OpenJDK Runtime Environment
java-1.7.0-openjdk-accessibility.x86_64 : OpenJDK accessibility connector
java-1.7.0-openjdk-demo.x86_64 : OpenJDK Demos
java-1.7.0-openjdk-devel.x86_64 : OpenJDK Development Environment
java-1.7.0-openjdk-headless.x86_64 : The OpenJDK runtime environment without audio and video support
java-1.7.0-openjdk-javadoc.noarch : OpenJDK API Documentation
java-1.7.0-openjdk-src.x86_64 : OpenJDK Source Bundle
java-1.8.0-openjdk.i686 : OpenJDK Runtime Environment
java-1.8.0-openjdk.x86_64 : OpenJDK Runtime Environment
java-1.8.0-openjdk-accessibility.i686 : OpenJDK accessibility connector
java-1.8.0-openjdk-accessibility.x86_64 : OpenJDK accessibility connector
java-1.8.0-openjdk-accessibility-debug.i686 : OpenJDK accessibility connector for packages with debug on
java-1.8.0-openjdk-accessibility-debug.x86_64 : OpenJDK accessibility connector for packages with debug on
java-1.8.0-openjdk-debug.i686 : OpenJDK Runtime Environment with full debug on
java-1.8.0-openjdk-debug.x86_64 : OpenJDK Runtime Environment with full debug on
java-1.8.0-openjdk-demo.i686 : OpenJDK Demos
java-1.8.0-openjdk-demo.x86_64 : OpenJDK Demos
java-1.8.0-openjdk-demo-debug.i686 : OpenJDK Demos with full debug on
java-1.8.0-openjdk-demo-debug.x86_64 : OpenJDK Demos with full debug on
java-1.8.0-openjdk-devel.i686 : OpenJDK Development Environment
java-1.8.0-openjdk-devel.x86_64 : OpenJDK Development Environment
java-1.8.0-openjdk-devel-debug.i686 : OpenJDK Development Environment with full debug on
java-1.8.0-openjdk-devel-debug.x86_64 : OpenJDK Development Environment with full debug on
java-1.8.0-openjdk-headless.i686 : OpenJDK Runtime Environment
java-1.8.0-openjdk-headless.x86_64 : OpenJDK Runtime Environment
java-1.8.0-openjdk-headless-debug.i686 : OpenJDK Runtime Environment with full debug on
java-1.8.0-openjdk-headless-debug.x86_64 : OpenJDK Runtime Environment with full debug on
java-1.8.0-openjdk-javadoc.noarch : OpenJDK API Documentation
java-1.8.0-openjdk-javadoc-debug.noarch : OpenJDK API Documentation for packages with debug on
java-1.8.0-openjdk-javadoc-zip.noarch : OpenJDK API Documentation compressed in single archive
java-1.8.0-openjdk-javadoc-zip-debug.noarch : OpenJDK API Documentation compressed in single archive for packages with debug on
java-1.8.0-openjdk-src.i686 : OpenJDK Source Bundle
java-1.8.0-openjdk-src.x86_64 : OpenJDK Source Bundle
java-1.8.0-openjdk-src-debug.i686 : OpenJDK Source Bundle for packages with debug on
java-1.8.0-openjdk-src-debug.x86_64 : OpenJDK Source Bundle for packages with debug on
```

我们选取两个条目

```bash
java-1.8.0-openjdk.x86_64 : OpenJDK Runtime Environment
java-1.8.0-openjdk-devel.x86_64 : OpenJDK Development Environment
```

他们分别是 JRE 和 JDK，根据你的需求安装即可，比如安装 JRE

```bash
$ sudo yum install java-1.8.0-openjdk -y
```

安装目录为

```bash
/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.171-8.b10.el7_5.x86_64
```

查看版本

```bash
$ java -version

openjdk version "1.8.0_171"
OpenJDK Runtime Environment (build 1.8.0_171-b10)
OpenJDK 64-Bit Server VM (build 25.171-b10, mixed mode)
```

## Oracle

Oracle 的 JDK 安装要稍微麻烦点，首先获取[官网](http://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html)的 JDK RPM 地址

```bash
http://download.oracle.com/otn-pub/java/jdk/10.0.1+10/fb4372174a714e6b8c52526dc134031e/jdk-10.0.1_linux-x64_bin.rpm
```

下载到服务器

```bash
wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/10.0.1+10/fb4372174a714e6b8c52526dc134031e/jdk-10.0.1_linux-x64_bin.rpm
```

安装

```bash
$ sudo yum -y localinstall jdk-10.0.1_linux-x64_bin.rpm
```

安装目录为

```bash
/usr/java/jdk-10.0.1
```

查看版本


```bash
$ java -version

java version "10.0.1" 2018-04-17
Java(TM) SE Runtime Environment 18.3 (build 10.0.1+10)
Java HotSpot(TM) 64-Bit Server VM 18.3 (build 10.0.1+10, mixed mode)
```

## 选择版本

查看所有本机 JDK 版本

```bash
$ sudo alternatives --config java

There are 2 programs which provide 'java'.

  Selection    Command
-----------------------------------------------
*+ 1           /usr/java/jdk-10.0.1/bin/java
   2           java-1.8.0-openjdk.x86_64 (/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.171-8.b10.el7_5.x86_64/jre/bin/java)

Enter to keep the current selection[+], or type selection number:
```

`*+` 代表当前使用的版本，该命令下输入版本对应的数字即可更改版本

- [How To Install Java on CentOS and Fedora](https://www.digitalocean.com/community/tutorials/how-to-install-java-on-centos-and-fedora#set-default-java)
