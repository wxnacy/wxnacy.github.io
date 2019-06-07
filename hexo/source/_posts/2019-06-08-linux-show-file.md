---
title: Linux 查看文件的几种方式
tags:
  - linux
date: 2019-06-08 05:48:00
---


Linux 中查看文件是很常见的操作，根据需求不同可以有几个不同的查看方式。

<!-- more -->
<!-- toc -->

首先点击下载一个 demo 文件: https://raw.githubusercontent.com/wxnacy/file/master/common/nums.txt

## cat

```bash
$ cat nums.txt
```

`cat` 可以将文本全部打印到屏幕中，但是只适合短小的文件，像这个 600 行的文件，翻看起来会很麻烦，如果你刚好是看最后几行的内容还好，如果想看头几行的内容那就惨了。

**其他参数**

```bash
$ cat -e nums.txt       # 每行最后添加 $ 符号
$ cat -n nums.txt       # 每行开头带有行号
```


## head

```bash
$ head nums.txt
1
2
3
4
5
6
7
8
9
10
```

`head` 可以查看前十行的内容，另外可以传参查看前 n 行的数据，或者前 n 个字节的数据。

**其他参数**

```bash
$ head -n 15 nums.txt   # 前 15 行
$ head -c 90 nums.txt   # 前 90 字节
```

## tail

```bash
$ tail nums.txt

591
592
593
594
595
596
597
598
599
600
```

`tail` 查看末尾 10 行的数据，经常查看日志的同学肯定对它很熟悉，`tail -f file` 可以等待文件追加并且到屏幕中，动态查看新增日志非常常用。

**其他参数**

```bash
tail -n 15 nums.txt     # 末尾 15 行的数据
tail -c 15 nums.txt     # 末尾 15 个字节的数据
tail -b 1 nums.txt      # 末尾 1 个 512 字节块的数据
tail -q nums.txt n.txt  # 检查多个文件时，进制打印标头
tail -f nums.txt        # 等待文件追加，并输出到标准输出中
tail -r -n 10 nums.txt  # 将最后 10 行，倒序显示
```

## less

最后是重头戏，`less` 是 Linux 的正统查看文件的方式，相似的还有 `more` 命令，虽然都说它不如 `less`，但是我觉得两者相差无几。

`less` 可以分页显示文档，翻页的方式与 `vim` 几乎一致，如果你不了解 `vim` 的翻页机制，可以看这里 [光标移动](https://vim.wxnacy.com/#docs/all-key#%E5%85%89%E6%A0%87%E7%A7%BB%E5%8A%A8)

![1](https://raw.githubusercontent.com/wxnacy/image/master/blog/less1.gif)

它还可以搜索文件，方式也与 `vim` 一样，输入 `/` 后输入匹配字符，使用 `n` 向后查找，使用 `N` 向前查找

![2](https://raw.githubusercontent.com/wxnacy/image/master/blog/less2.gif)

查看多个文件时，使用 `:e filename` 切换查看文件，或者使用 `:n` 和 `:p` 向后或向前查找

![3](https://raw.githubusercontent.com/wxnacy/image/master/blog/less3.gif)

既然它跟 `vim` 有这么多的相似点，那切换到 `vim` 模式也是很方便的，按下 `v` 即可

使用 `F` 则可以达到 `tail -f file` 的效果，等待文件的输入，`<CTRL-C>` 退出。

最后按下 `q` 即可退出 `less` 模式。

`less` 命令模式非常常见，帮助命令 `man` 就是完全依照此模式来使用的，使用 `man less` 查看更多的使用方式。

**其他参数**

```bash
$ less -N nums.txt      # 显示行号
$ less -m nums.txt      # 显示查看的百分比进度
$ less -e nums.txt      # 查看到文档末尾时，自动退出
$ less +20 nums.txt     # 从第 20 行开始查看
```

其它的命令搭配 `less` 管道输入模式可以起到很好的效果。

**分页显示当前所有进程**

```bash
$ ps aux | less
```

**分页显示历史命令**

```bash
$ history | less
```
