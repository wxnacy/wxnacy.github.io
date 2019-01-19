---
title: CentOS 7 如何安装 Java 11
tags:
  - java
date: 2018-12-27 09:26:01
---


几个月前我写过文章 [CentOS 安装 JDK](/2018/06/15/centos-install-jdk/) ，当时是以 JDK 8 为例子，现在 Java 11 出来了，相应的更新一版。

<!-- more --><!-- toc -->

## OpenJDK

首先搜索可安装的 JDK

```bash
$ sudo yum search java-11
```

从结果中我们可以找出两个条目

```bash
java-11-openjdk.x86_64 : OpenJDK Runtime Environment 11
java-11-openjdk-devel.x86_64 : OpenJDK Development Environment 11
```

他们分别是 JRE 和 JDK，根据你的需求安装即可，比如安装 JRE

```bash
$ sudo yum install java-11-openjdk -y
```

安装目录为

```bash
/usr/lib/jvm/java-11-openjdk-11.0.1.13-3.el7_6.x86_64
```

查看版本

```bash
$ java -version

openjdk version "11.0.1" 2018-10-16 LTS
OpenJDK Runtime Environment 18.9 (build 11.0.1+13-LTS)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.1+13-LTS, mixed mode, sharing)
```

## Oracle

Oracle 的 JDK 安装要稍微麻烦点，首先获取[官网](https://www.oracle.com/technetwork/java/javase/downloads/jdk11-downloads-5066655.html)的 JDK RPM 地址

```bash
https://download.oracle.com/otn-pub/java/jdk/11.0.1+13/90cf5d8f270a4347a95050320eef3fb7/jdk-11.0.1_linux-x64_bin.rpm
```

下载到服务器

```bash
$ wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/11.0.1+13/90cf5d8f270a4347a95050320eef3fb7/jdk-11.0.1_linux-x64_bin.rpm
```

安装

```bash
$ sudo yum -y localinstall jdk-11.0.1_linux-x64_bin.rpm
```

安装目录为

```bash
/usr/java/jdk-11.0.1
```


## 选择版本

查看所有本机 JDK 版本

```bash
$ sudo alternatives --config java

There are 2 programs which provide 'java'.

  Selection    Command
-----------------------------------------------
 + 1           java-11-openjdk.x86_64 (/usr/lib/jvm/java-11-openjdk-11.0.1.13-3.el7_6.x86_64/bin/java)
*  2           /usr/java/jdk-11.0.1/bin/java

Enter to keep the current selection[+], or type selection number: 2
```

`*+` 代表当前使用的版本，该命令下输入版本对应的数字即可更改版本，我们输入 2 更
改为 oracle 版本，然后查看版本

```bash
$ java -version
java version "11.0.1" 2018-10-16 LTS
Java(TM) SE Runtime Environment 18.9 (build 11.0.1+13-LTS)
Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.1+13-LTS, mixed mode)
```

