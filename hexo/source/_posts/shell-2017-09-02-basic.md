---
title: Shell 基础命令
date: 2017-09-02
tags: [linux]
---


## type
```bash
$ type [-tpa] name
选项与参数：
    ：不加任何选项与参数时，type 会显示出 name 是外部命令还是 bash 内建命令
-t  ：当加入 -t 参数时，type 会将 name 以底下这些字眼显示出他的意义：
      file    ：表示为外部命令；
      alias   ：表示该命令为命令别名所配置的名称；
      builtin ：表示该命令为 bash 内建的命令功能；
-p  ：如果后面接的 name 为外部命令时，才会显示完整文件名；
-a  ：会由 PATH 变量定义的路径中，将所有含 name 的命令都列出来，包含 alias
```

## 设置别名alias和历史记录history
```bash
$ alias h='history'     # 设置别名
$ unalias h             # 取消别名

$ history [n]
$ history [-c]
$ history [-raw] histfiles
```
