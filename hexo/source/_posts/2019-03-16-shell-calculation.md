---
title: Shell 几种算术运算方式
tags:
  - shell
date: 2019-03-16 16:40:29
---


Shell 脚本中，我们可以使用几种方式来实现算数运算。

<!-- more --><!-- toc -->

## expr

expr 本身是一个算数运算命令，Shell 可以直接拿到它的执行结果

```bash
$ echo `expr 1 + 2`
3
```

expr 有很多缺点，比如：只能运算整数、数字和符号之间必须都有空格、`*` 号需要转义、无法使用次方运算

```bash
$ expr 1+2
1+2

$ expr 1 +2
expr: syntax error

$ expr 1 \* 2
2

$ expr 1 + 2.3
expr: not a decimal number: '2.3'
```

## 小括号

下面我们来看 shell 本身的计算方式，第一个是小括号，这种方式需要把运算表达式用两层小括号包裹起来

```bash
$ echo $((1+2))
3

$ ((i=1+2))

$ echo $i
3

$ echo $((1 + 2.3))
3.2999999999999998

$ echo $((2 ** 3))  # 计算三次方
8
```

通过例子可以看到，这种方式比 `expr` 写起来更好更舒服，就是在计算浮点数字时会有精度损失。

## 中括号

中括号的方式必须加上 `$` 前缀，并不支持像小括号一样，在括号内赋值，其他与小括号无异。

```bash
$ echo $[1 + 2]
3

$ echo $[2 ** 3]
8
```

## let

let 用来指示运算表达式，也可以达到效果，但是同样的有很多缺点，比如运算符和数字不能有空格、不支持次方运算、浮点运算会忽略小数点部分、`*` 需要转义

```bash
> $ let i = 1 + 2
zsh: bad math expression: operand expected at =

> $ let i=1+2
> $ echo $i
3

> $ let i=1+2.3
> $ echo $i
3

> $ let i=2**3
zsh: no matches found: i=2**3

> $ let i=1+2.6
> $ echo $i
3

> $ let i=2\*3
> $ echo $i
6
```

经过对比可以发现，小括号和中括号的方式最好，两者只是书写存在细微差异，其他两个不建议使用。

- [SHELL脚本--expr命令全解](https://www.cnblogs.com/f-ck-need-u/p/7231832.html)
