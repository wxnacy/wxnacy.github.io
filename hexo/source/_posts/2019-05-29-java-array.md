---
title: 重新学 Java 系列：数组
date: 2019-05-29 09:47:05
tags: [java]
---

> 这个是一个系列阅读，关于为什么重新学习，我在文章 [重新学 Java 系列：新系列、新开始](/2018/12/29/java-renew-why/)(https://wxnacy.com/2018/12/29/java-renew-why/) 中有提到，这个系列是在有 Java 基础的情况下，重新学习讨论一下以前可能忽略掉，或者没理解的知识细节，我想要永远在学习的路上。

<!-- more -->
<!-- toc -->

已经习惯了 Python 的列表对象，再回来看 Java 的数组和列表很是不适，这种不适已经上升到了生理反应，我为什么要重新学 Java？我是谁？我在哪？

Java 中数组是用来存储***固定大小***的***同类型***元素。

## 声明

`int` 类型数组有两种声明方式 `int[] varName` 或者 `int varName[]`，一般建议使用第一种声明方式。后者来源于 `c/c++`，是为了让 `c/c++` 程序员快速理解 Java。

## 定义

有三种定义方式

**静态初始化**

```java
int[] a = new int[]{0, 1, 2};
```

**静态初始化简化方式**

```java
int[] b = {0, 1, 2};
```

静态初始化不能指定元素个数，或者说初始化后元素个数已经固定了，不需要指定。

**动态初始化**

```java
int[] c = new int[3];
c[0] = 1
```

动态初始化后，数组每个元素会赋值当前类型的默认值，分别如下所以：

类型                               | 默认值
---                                | -----
整数类型（byte、short、int、long） | 0
浮点类型（float、double）          | 0.0
字符类型（char）                   | '\u0000'
布尔类型（boolean）                | false
引用类型（类、接口、数组）         | null

## 遍历

两种方式 `for` 和 `forEach`

**for**

```java
for(int i = 0; i < nums.length; i++){
    System.out.println(nums[i]);
}
```

**forEach**

```java
for ( int n: nums ) {
    System.out.println(n);
}
```

## 方法

数组本身不提供方法，只有一个变量 `length` 用来获取数组的大小。

```java
int n = nums.length
```

记得当年刚开始学习 Java 时，总是跟列表的 `size()` 方法搞混，不知道什么时候用 `length`，什么时候用 `size()`。现在看来只需要记住，数组的大小是不可变的，所以使用变量 `length` 即可获取数组大小。而列表是可变的，所以需要使用方法 `size()` 动态获取大小。

`java.util.Arrays` 类提供了操作数组的方法，都是静态方法。

方法|描述
----|----
public static void sort(Object[] a)                     |   排序数组，升序
public static int binarySearch(Object[] a, Object key)  |   使用二分搜索来搜索给定元素，数组需要先排序，返回索引
public static boolean equals(Object[] a, Object[] a2)   |   比较数组是否相同，返回 boolean 类型
public static void fill(Object[] a, Object val)         |   给数组的所有元素指定某个值

## 参考

- [Java 数组](https://www.runoob.com/java/java-array.html)
