---
title: 重新学 Java 系列：Maven 快速入门
tags:
  - java
date: 2019-01-10 10:24:40
---

> 这个是一个系列阅读，关于为什么重新学习，我在文章 [重新学 Java 系列：新系列、新开始](/2018/12/29/java-renew-why/)(https://wxnacy.com/2018/12/29/java-renew-why/) 中有提到，这个系列是在有 Java 基础的情况下，重新学习讨论一下以前可能忽略掉，或者没理解的知识细节，我想要永远在学习的路上。

<!-- more -->
<!-- toc -->

如果早几年，可能还会有公司不用 Maven 管理项目，还会有人不知道 Maven。但是现在如果你还不知道 Maven，那你跟门外汉差不多了。

Maven 是 Java 最好的项目管理软件，就像 npm 对于 Node 一样重要。

我们先来快速了解下，如何使用 Maven 快速创建一个项目。

## 下载

**MacOS**

```bash
$ brew install Maven
```

***需要：Java >= 1.7***

安装好后查看版本

```bash
$ mvn --version
Apache Maven 3.6.0 (97c98ec64a1fdfee7767ce5ffb20918da4f719f3; 2018-10-25T02:41:47+08:00)
Maven home: /usr/local/Cellar/maven/3.6.0/libexec
Java version: 11.0.1, vendor: Oracle Corporation, runtime: /Library/Java/JavaVirtualMachines/jdk-11.0.1.jdk/Contents/Home
Default locale: zh_US_#Hans, platform encoding: UTF-8
OS name: "mac os x", version: "10.14.2", arch: "x86_64", family: "mac"
```

## 创建项目

```bash
$ mvn archetype:generate \
    -DgroupId=com.wxnacy.app \
    -DartifactId=test-app \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DarchetypeVersion=1.4 \
    -DinteractiveMode=false \
```

如果你的电脑第一次运行该命令，可能需要一些时间，因为要下载一些必要包。

创建完成后，会出现一个目录 `test-app`，即为项目目录。

进入目录

```bash
$ cd test-app
```

**查看项目结构**

```bash
$ tree
.
├── pom.xml
└── src
    ├── main
    │   └── java
    │       └── com
    │           └── wxnacy
    │               └── app
    │                   └── App.java
    └── test
        └── java
            └── com
                └── wxnacy
                    └── app
                        └── AppTest.java

11 directories, 3 files
```

`src/main/java` 目录中存放源代码，`src/test/java` 目录中存在测试代码，`pom.xml` 文件为项目数据模型。具体内容如下：

```xml
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.wxnacy.app</groupId>
  <artifactId>test-app</artifactId>
  <version>1.0-SNAPSHOT</version>

  <name>test-app</name>
  <!-- FIXME change it to the project's website -->
  <url>http://www.example.com</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.7</maven.compiler.source>
    <maven.compiler.target>1.7</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>

  <build>
    <pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->
      <plugins>
        <!-- clean lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#clean_Lifecycle -->
        <plugin>
          <artifactId>maven-clean-plugin</artifactId>
          <version>3.1.0</version>
        </plugin>
        <!-- default lifecycle, jar packaging: see https://maven.apache.org/ref/current/maven-core/default-bindings.html#Plugin_bindings_for_jar_packaging -->
        <plugin>
          <artifactId>maven-resources-plugin</artifactId>
          <version>3.0.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.8.0</version>
        </plugin>
        <plugin>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>2.22.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-jar-plugin</artifactId>
          <version>3.0.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-install-plugin</artifactId>
          <version>2.5.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-deploy-plugin</artifactId>
          <version>2.8.2</version>
        </plugin>
        <!-- site lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#site_Lifecycle -->
        <plugin>
          <artifactId>maven-site-plugin</artifactId>
          <version>3.7.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-project-info-reports-plugin</artifactId>
          <version>3.0.0</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
</project>
```

内容很多，其实很简单，默认状态下，`pluginManagement` 节点中的内容为默认插件，已经集成在父 pom 中，所以删除掉也不影响。`dependencies` 节点为项目需要的数据包。

## 运行

**编译**

```bash
$ mvn compile
```

随后根目录下会生成 `target` 文件夹，class 文件都存放在 `target/classes` 文件夹中

**运行**

```bash
$ java -cp target/classes com.wxnacy.app.App
Hello World
```

**打包**

```bash
$ mvn package
```

随后会在 `target` 文件夹中生成 `test-app-1.0-SNAPSHOT.jar` 文件。

**运行**

```bash
$ java -cp target/test-app-1.0-SNAPSHOT.jar com.wxnacy.app.App
Hello World
```

- [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
