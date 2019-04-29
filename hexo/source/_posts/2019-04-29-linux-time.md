---
title: Linux time 命令统计脚本耗时
tags:
  - linux
date: 2019-04-29 12:10:22
---


在 Linux 中 time 命令可以统计执行脚本的耗时。

<!-- more -->
<!-- toc -->

我们以 [wc](https://wxnacy.com/2019/02/01/linux-wc/) 命令为例子，统计下计算文件行数时的耗时情况

```bash
$ wc -l tmd-error.log
655572 tmd-error.log
```

只需要在命令前加上 `time` 即可

**bash环境下**

```bash
bash-3.2$ time wc -l tmd-error.log
  655572 tmd-error.log

real    0m0.047s
user    0m0.036s
sys     0m0.011s
```

得到的结果有三个时间，`real` 为真实耗时，而 `user` 和 `sys` 为用户环境和系统的各自耗时。

**zsh环境下**

```bash
> $ time wc -l tmd-error.log
  655572 tmd-error.log
wc -l tmd-error.log  0.04s user 0.01s system 97% cpu 0.047 total
```

`zsh` 环境的输出结果不太易读，只需要看最后的 `total` 值即可

**fish环境下**

```bash
wxnacy@wxnacydeMacBook-Pro ~/P/t/log> time wc -l tmd-error.log
  655572 tmd-error.log
        0.04 real         0.03 user         0.01 sys
```

说实话还是 `fish` 环境的看着最舒服，要不是它不兼容 `bash` 脚本，我感觉它早就制霸 shell 届了，哼。
