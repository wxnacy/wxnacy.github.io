---
title: Java 11 新特性：String 增强
date: 2018-12-24 11:51:01
tags: [java]
---

虽然现在很少使用 Java 进行开发，但是仍然时不时的关注着它的动态，最近发现 Java 11 发布了，并且带来了很多新特性，关键它是 Java8 以后又一长期维护版本，可以在生产环境使用，这又增加了我关注它的动力，今天先介绍一个新特性：String 增强

<!-- more --><!-- toc -->
我们来看这段代码

```java
public class StringExample{
    public static void main(String args[]){
        Java11Upgrade();
    }

    public static void Java11Upgrade() {
        // 判断字符串是否为空白
        System.out.println(" ".isBlank());              // true
        // 去除首尾空格
        System.out.println(" Java ".strip());           // Java
        // 去除首部空格
        System.out.println(" Java".stripLeading());     // Java
        // 去除尾部空格
        System.out.println("Java ".stripTrailing());    // Java
        // 重复字符串
        System.out.println("Java".repeat(2));           // JavaJava
        // 获取字符串中的行数
        System.out.println("A\nB\nC".lines().count());  // 3
    }
}
```

还是一些其他语言早就有的特性，不过很高兴 Java 在逐渐补足这些东西，这也是让 Java 保持霸主地位的必要操作。
