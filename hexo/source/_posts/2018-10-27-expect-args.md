---
title: Expect 脚本参数传递
tags:
  - expect
date: 2018-10-27 10:44:20
---


Expect 脚本同 Shell 脚本一样可以通过外部传递参数。

<!-- more --><!-- toc -->

`argc` 代表参数个数，`argv` 代表参数列表

```expect
puts $argc
puts $argv
```

```bash
$ ./test.exp wxnacy wxn
2
wxnacy wxn
```

设置变量

```expect
set name [lindex $argv 0]
puts $name
```

```bash
./test.exp wxnacy wxn
wxnacy
```
