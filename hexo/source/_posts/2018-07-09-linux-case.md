---
title: Shell 中的 Switch 语法 case
date: 2018-07-09 13:57:54
tags: [shell]
---

Shell 脚本中 case 可以进行多选择操作，每个选择匹配一中命令。

<!-- more --><!-- toc -->

语法

```bash
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2|模式3）
    command1
    command2
    ...
    commandN
    ;;
esac
```

使用

```bash
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3|4)  echo '你选择了 3 或 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
```

执行并输入 `1 - 4` 中的数字

```bash
输入 1 到 4 之间的数字:
你输入的数字为:
3
你选择了 3 或 4
```

- [Shell 流程控制](http://www.runoob.com/linux/linux-shell-process-control.html)
