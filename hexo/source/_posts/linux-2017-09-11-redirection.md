---
title: Linux 数据流重定向(Redirection)
date: 2017-09-11
tags: [linux]
---

<!-- toc -->
<!-- more -->
## 重定向
```bash
标准输入　　(stdin) ：代码为 0 ，使用 < 或 <<
标准输出　　(stdout)：代码为 1 ，使用 > 或 >>
标准错误输出(stderr)：代码为 2 ，使用 2> 或 2>>
```

## 标准输出（stdout）
*1>* 或 *>* 会将应该输出到屏幕的信息，输入到指定文件中
```bash
$ ll > ll.txt       # 此时屏幕不再输出信息，而是输入到 ll.txt 中
# > 会在每次使用时覆盖相同文件名的内容，如果想要追加内容使用 >>
```

## 标准输出错误（stderr）
*2>* 会将错误信息单独输出到指定文件中
```bash
$ z                             # 我随便输入了指令

pyenv: z: command not found     # 错误信息

The `z' command exists in these Python versions:
  2.7.12/envs/env_hamster
  env_hamster

$ z 2> err.log                  # 使用重定向将错误输出到文件
```
如果我们不想将错误单独写到一个文件而是和标准输出一同输出到同一文件中，应该怎么
做呢

也可能你在了解到标准输出和错误输出后会想当然的用这种写法
```bash
$ z > file.log 2> file.log
```
这样是错误的，应该两股数据会交叉写入到同一文件中，造成数据混乱，而正确的写法
应该是这样的
```bash
$ z > file.log 2>&1
$ z &> file.log
# 两种写法均可
```

### /dev/null 垃圾桶黑洞装置
假如有些命令的错误是我们预知的而不想显示出，此时该怎么做呢，我们可以让他消失
```bash
$ z 2> /dev/null                # 此时我们将看不到输出的错误信息
```

## 标准输入（stdin）
了解 stdout 和 stderr 后我们来看下怎么理解标准输入
```bash
$ cat > cat.txt
hello world
test
# 按下 ctrl + d 离开
```
这段命令可以使键盘输入内容重定向的文件中，如果我们想使用 **某个文件内容** 替代
**键盘输入** 到制定文件中呢，这时候 **<** 就派上用场了
```bash
$ cat > cat.txt < ~/.bashrc

$ ll cat.txt ~/.bashrc
-rw-r--r--  1 wxnacy  staff    42B  8 27 08:14 /Users/wxnacy/.bashrc
-rw-r--r--  1 wxnacy  staff    42B  9 11 09:50 cat.txt
```
通过 **<** 导入的文件我们回它们其实一摸一样，类似复制功能

接下来我们来探讨 **<<**，它并不同与标准输出的追加功能，我们先来看另一个例子，
当我们使用键盘输入到文件时，如果不想用 `ctrl + d` 来终止程序，而是其他方式可以
吗，我们来试一下
```bash
$ cat > cat.txt << "eof"
hello world
eof                     # 输入该关键字，我们不用输入 ctrl + d 即可终止程序
```
现在我们可以给 **<<** 下一个定义 **结束的输入字符**，当然 eof 不是不变的，我们
也可以指定其他字符串
