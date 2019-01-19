---
title: Java 报错：type List does not take parameters
date: 2018-08-09 17:54:54
tags: [java]
---

在使用 List 类的时候会报一个错误。

<!-- more --><!-- toc -->

```java
List<String> list = new ArrayList<String>();
```
```bash
error: type List does not take parameters
```

这个错误是因为到错了包

```java
import java.awt.List;
```

正确的包为

```java
import java.util.List;
```
