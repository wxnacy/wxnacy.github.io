---
title: Linux 神级流编辑器命令工具 sed
tags: [linux]
---

> sed（意为流编辑器，源自英语“stream editor”的缩写）是Unix常见的命令行程序。sed用来把文档或字符串里面的文字经过一系列编辑命令转换为另一种格式输出。sed通常用来匹配一个或多个正则表达式的文本进行处理。

<!-- more --><!-- toc -->
我们先简单了解下 sed

## 开始

**准备数据**

```bash
$ cat > test << "EOF"
This is my cat
  my cat's name is betty
This is my dog
  my dog's name is frank
This is my fish
  my fish's name is george
This is my goat
  my goat's name is adam
EOF
```

**替换**

```bash
$ sed 's/This/That/g' test
That is my cat
  my cat's name is betty
That is my dog
  my dog's name is frank
That is my fish
  my fish's name is george
That is my goat
  my goat's name is adam
```

我们将每行输出的 `This` 替换为 `That`，sed 默认输出是将修改的文件输出到屏幕上，如果想要修改原文件，则需要加上 `-i` 参数

```bash
$ sed -i 's/This/That/g' test
```

修改原文件的命令需要在 Linux 中运行，Mac 中略有不同。

原则上这个操作习惯并不好，安全的方式是将输出的结果通过管道输入到另一个文件中

```bash
$ sed 's/This/That/g' test > test1
```

## 动作

从上面的简单例子，可以得到 sed 的语法为

```bash
$ sed [参数] <动作> [file]
```

动作规则为：`n1,n2 action args`

`n1,n2` 为执行动作的行数范围，不是必传

action 取值为：

- a：新增，a 的后面可以接字符串，而这些字符串会在新的一行出现（目前的下一行）。
- c：替换，c 的后面可以接字符串，这些字符串可以替换n1，n2之间的行！
- d：删除，因为是删除，所以 d 后面通常不接任何参数。
- i：插入，i 的后面可以接字符串，而这些字符串会在新的一行出现（目前的上一行）。
- p：打印，也就是将某个选择的数据打印出来，通常 p 会与参数 sed -n 一起运行。
- s：替换，可以直接进行替换工作。通常这个 s 的动作可以匹配正则表达式！

### s

s 
