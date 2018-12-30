---
title: 重新学 Java 系列：public private protected friendly 的区别
tags:
  - java
date: 2018-12-30 22:28:56
---


> 这个是一个系列阅读，关于为什么重新学习，我在文章 [重新学 Java 系列：新系列、新开始](/2018/12/29/java-renew-why/)(https://wxnacy.com/2018/12/29/java-renew-why/) 中有提到，这个系列是在有 Java 基础的情况下，重新学习讨论一下以前可能忽略掉，或者没理解的知识细节，我想要永远在学习的路上。

<!-- more --><!-- toc -->
Java 共有四种修饰：`public, private, protected, friendly`，（默认为：friendly）

可能调用他们修饰变量和函数的有的作用域有：当前类、当前包、子类、外部类

从网上找他们的对应的调用权限，很多是各种摘抄，并且存在各种错误，所以我认真对他们进行了实验，得到如下结论


| 对比      | 当前类 | 当前包 | 子类 | 外部类 |
| --------- | ------ | ------ | ---- | ------ |
| public    | √      | √      | √    | √      |
| private   | √      | ×      | ×    | ×      |
| protected | √      | √      | √    | ×      |
| friendly  | √      | √      | √    | ×      |

如表格，简单总结如下

- `public`: 所有地方都可以调用。
- `private`: 只有当前类可以调用。
- `protected`: 只有外部类不可调用。
- `friendly`: 与 `protected` 完全相同。

下载 demo [https://github.com/wxnacy/study/tree/master/java/modification](https://github.com/wxnacy/study/tree/master/java/modification) 到电脑中，确保电脑中有 Java 运行环境，可以执行跟目下的 `./run.sh` 脚本。

```bash
$ ./run.sh
        public  private protected       friendly
当前类  √       √       √               √
当前包  √       ×       √               √
子类    √       ×       √               √
外部类  √       ×       ×               ×
```
