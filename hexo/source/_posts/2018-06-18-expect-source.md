---
title: Expect 中 source 的用法
date: 2018-06-18 16:55:59
tags: [expect]
---

在 Expect 中 source 的用户和 Shell 很类似，可以将变量作用到当前命令中。

<!-- more -->

**用法**

```bash
source fileName                         # 加载文件
source -encoding encodingName fileName  # 使用 encoding 加载
```

新建 source 文件 `file1.exp`

```bash
set name wxnacy     # 设置变量
```

新建执行文件 `file2.exp`

```bash
#!/usr/bin/env expect
source file1.exp            # 加载文件

puts [info exists name]     # 判断是否存在变量，存在返回 1，否则返回 0
puts ${name}                # 打印变量
```

执行

```bash
$ expect file2.exp

1
wxnacy
```

- [source](https://www.tcl.tk/man/tcl/TclCmd/source.htm)
