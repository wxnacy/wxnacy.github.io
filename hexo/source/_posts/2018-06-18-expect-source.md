---
title: Expect 中 source 的用法
date: 2018-06-18 16:55:59
tags: [expect]
---

在 Expect 中 source 的用户和 Shell 很类似，可以将变量作用到当前命令中。
<!-- more --><!-- toc -->

**用法**

```bash
source fileName
source -encoding encodingName fileName
```

新建文件 `file1.exp`

```bash
set name wxnacy
```

新建文件 `file2.exp`

```bash
#!/usr/bin/env expect
source file1.exp

puts [info exists name]
puts ${name}
```

执行

```bash
$ expect file2.exp

1
wxnacy
```

- [source](https://www.tcl.tk/man/tcl/TclCmd/source.htm)
