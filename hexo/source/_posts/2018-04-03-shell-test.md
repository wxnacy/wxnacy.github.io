---
title: Shell test 命令
tags:
  - linux
date: 2018-04-03 09:59:18
---

Shell中的 test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。

<!-- more --><!-- toc -->
test 根据表达式的求值返回 **0（真）或 1（假）**，这个地方需要注意，真和假的返回值跟绝大数的结果都不一样，如果你熟悉了其他语言的 1（真）0（假），在这里可要小心了。
## 数值
- -eq	等于则为真
- -ne	不等于则为真
- -gt	大于则为真
- -ge	大于等于则为真
- -lt	小于则为真
- -le	小于等于则为真
```bash
if test 1 -eq 1
then
    echo true
else
    echo false
fi
```
输出
```bash
true
```
也可以用 `&&, ||` 来做真假的判断
```bash
$ test 1 -eq 1 && echo true || echo false

true
```
## 字符串测试
- =	等于则为真
- !=	不相等则为真
- -z 字符串	字符串的长度为零则为真
- -n 字符串	字符串的长度不为零则为真
```bash
$ test 'wxnacy' = 'wxnacy' && echo true || echo false

true
```

## 文件测试
- -e 文件名	如果文件存在则为真
- -r 文件名	如果文件存在且可读则为真
- -w 文件名	如果文件存在且可写则为真
- -x 文件名	如果文件存在且可执行则为真
- -s 文件名	如果文件存在且至少有一个字符则为真
- -d 文件名	如果文件存在且为目录则为真
- -f 文件名	如果文件存在且为普通文件则为真
- -c 文件名	如果文件存在且为字符型特殊文件则为真
- -b 文件名	如果文件存在且为块特殊文件则为真
```bash
$ test -f test.sh && echo true || echo false

false
```

## 与或非
Shell 还提供了三个操作符
- ! 非
- -a 与
- -o 或
优先级由高到低为 `!, -a, -o`

## 返回值
我们可以通过 `$?` 来获取 `test` 的返回值
```bash
$ test 1 -gt 1; echo $?

1 # 假
```

- [Shell test 命令](http://www.runoob.com/linux/linux-shell-test.html)
- [Bash 测试和比较函数](https://www.ibm.com/developerworks/cn/linux/l-bash-test.html)
