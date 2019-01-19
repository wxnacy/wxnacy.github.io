---
title: Shell 使用 read 创建交互模式脚本
tags:
  - shell
date: 2018-10-28 10:47:58
---


Shell 脚本中可以使用 read 来实现交互模式。

<!-- more --><!-- toc -->

## echo 和 read

```bash
#!/usr/bin/env bash

echo -n "What is your name: "
# echo -e "What is your name: \c"
read
echo "$REPLY"
```

执行该脚本，根据提示输入名字即可完成一次交互，echo 的 `-n` 参数可以使屏幕输出后不换行，键盘输入的内容默认使用变量 `REPLY`

## 直接用 read

```bash
read -p "What is your name: " name
echo "My name is $name"
```

可以实现跟上边相同的效果，`-p` 为提示信息，`name` 为传入参数变量

**不可见**

普通输入文字都是明文显示，如果想要输入密码类的内容，可以使用 `-s` 参数使内容不显示

```bash
read -p "What is your name: " -s name
```

**限制个数**

使用 `-n` 显示参数个数，再输入参数跟回车一个效果

```bash
read -n 1 -p "Are you sure delete[Y|n]: " flag
```

**读取管道数据**

```bash
while read line
do
    echo $line
done
```

```bash
$ ll | test.sh
```

**更多参数**

```bash
-a ：将内容读入到数组中
-d ：表示delimiter，即定界符，一般情况下是以IFS为参数的间隔，但是通过-d，我们可以定义一直读到出现执行的字符位置。例如read –d madfds value，读到有m的字符的时候就不在继续向后读，例如输入为 hello m，有效值为“hello”，请注意m前面的空格等会被删除。这种方式可以输入多个字符串，例如定义“.”作为结符号等等。
-e ：只用于互相交互的脚本，它将readline用于收集输入行。读到这几句话不太明白什么意思，先跳过。
-n ：用于限定最多可以有多少字符可以作为有效读入。例如echo –n 4 value1 value2，如果我们试图输入12 34，则只有前面有效的12 3，作为输入，实际上在你输入第4个字符‘3’后，就自动结束输入。这里结果是value为12，value2为3。
-p ：用于给出提示符，在前面的例子中我们使用了echo –n “…“来给出提示符，可以使用read –p ‘… my promt?’value的方式只需一个语句来表示。
-r ：在参数输入中，我们可以使用’/’表示没有输入完，换行继续输入，如果我们需要行最后的’/’作为有效的字符，可以通过-r来进行。此外在输入字符中，我们希望/n这类特殊字符生效，也应采用-r选项。
-s ：隐藏输入内容，比如密码
-t ：用于表示等待输入的时间，单位为秒，等待时间超过，将继续执行后面的脚本，注意不作为null输入，参数将保留原有的值
```

**参考**

- [shell的read命令](http://gohom.win/2015/08/20/shell-read/)
- [Shell中read的选项及用法](https://www.cnblogs.com/nwf5d/archive/2011/11/20/2255702.html)
