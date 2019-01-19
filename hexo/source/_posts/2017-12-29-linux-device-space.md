---
title: Linux 分析磁盘空间
tags:
  - linux
date: 2017-12-29 17:00:34
---

昨天在服务器上部署 API 时，总是失败，查看日志发现磁盘空间不足，想要查看磁盘空间各种手忙脚乱，不知如何下手，懂得简单几个命令也不能称心如意的解决问题。所以痛定思痛总结了下需要用到的几种，以便以后查阅。

<!-- more --><!-- toc -->
## df
```bash
$ df
```
```bash
Filesystem     1K-blocks    Used Available Use% Mounted on
udev              489868       0    489868   0% /dev
tmpfs             101612    2804     98808   3% /run
/dev/vda1       41151808 2200772  36837608   6% /
```
从左到右分别标示为：文件磁盘，1K空间块数，已使用，可用，已用比例，挂载点。加上 `-h` 参数可以换算为方便的阅读方式
```bash
$ df -h
```
```bash
Filesystem      Size  Used Avail Use% Mounted on
udev            479M     0  479M   0% /dev
tmpfs           100M  2.8M   97M   3% /run
/dev/vda1        40G  2.1G   36G   6% /
```
### 更多参数
```bash
-a                      # 全部文件系统列表
-h                      # 方便阅读方式显示
-H                      # 等于“-h”，但是计算式，1K=1000，而不是1K=1024
-i                      # 显示inode信息
-k                      # 区块为1024字节
-l                      # 只显示本地文件系统
-m                      # 区块为1048576字节
--no-sync               # 忽略 sync 命令
-P                      # 输出格式为POSIX
--sync                  # 在取得磁盘信息前，先执行sync命令
-T                      # 文件系统类型
--block-size=<区块大小> # 指定区块大小
-t<文件系统类型>        # 只显示选定文件系统的磁盘信息
-x<文件系统类型>        # 不显示选定文件系统的磁盘信息
--help                  # 显示帮助信息
--version               # 显示版本信息
```
## du
我们已经知道当前机器的使用空间了，如果超过了 80％ 的时候，就有必要查看下是哪些文件在占用空间了，通常会是些日志文件。
进入登陆用户根目录 `~` 执行 `du` 命令，你会得到类似这个结果
```bash
...
584  ./.oh-my-zsh/themes
8    ./.oh-my-zsh/templates
4    ./.oh-my-zsh/log
8    ./.oh-my-zsh/custom/plugins/example
12   ./.oh-my-zsh/custom/plugins
20   ./.oh-my-zsh/custom
5328 ./.oh-my-zsh
6144 .
```
`du` 会遍历当前目录和所有子目录，并把文件夹大小返回，单位 K，最后一行为当前目录总大小。
同样的使用 `-h` 参数可以方便阅读
```bash
...
584K ./.oh-my-zsh/themes
8.0K ./.oh-my-zsh/templates
4.0K ./.oh-my-zsh/log
8.0K ./.oh-my-zsh/custom/plugins/example
12K  ./.oh-my-zsh/custom/plugins
20K  ./.oh-my-zsh/custom
5.3M ./.oh-my-zsh
6.0M .
```
但是真正使用的话你会感觉到自己机器上的文件夹太多了，因为他会所有的文件夹都遍历出来，使用 `-d , --max-depth` 来限制遍历的目录层数，后面跟上层级数字。
```bash
$ du -d 1
```
```bash
8    ./.pip
8    ./.ssh
652  ./.cache
5328 ./.oh-my-zsh
6144 .
```
看，这样就简洁多了，需要注意一点，在 **CentOS 6** 版本以前，是没有缩写 `-d` 的，只能输入参数全名。
我也可以分析指定目录
```bash
$ du .oh-my-zsh .pip
```
结合上边这些参数我们已经可以来做分析了，我通常这样做
```bash
$ du -hd 1 ~
$ du -hd 1 ~/.oh-my-zsh
...
```
我从用户根目录开始查看第一级目录的文件夹大小，并一直将目录层级细化，最后找到最大的文件夹，进入后通过 `ll -h` 查看哪个文件最大，`-h` 已经不需要我告诉有什么作用了。
### 更多参数
```bash
-a或-all                # 显示目录中个别文件的大小。
-b或-bytes              # 显示目录或文件大小时，以byte为单位。
-c或--total             # 除了显示个别目录或文件的大小外，同时也显示所有目录或文件的总和。
-D或--dereference-args  # 显示指定符号连接的源文件大小。
-h或--human-readable    # 以K，M，G为单位，提高信息的可读性。
-H或--si                # 与-h参数相同，但是K，M，G是以1000为换算单位。
-k或--kilobytes         # 以1024 bytes为单位。
-l或--count-links       # 重复计算硬件连接的文件。
-L<符号连接>或--dereference<符号连接>   # 显示选项中所指定符号连接的源文件大小。
-m或--megabytes         # 以1MB为单位。
-s或--summarize         # 仅显示总计。
-S或--separate-dirs     # 显示个别目录的大小时，并不含其子目录的大小。
-x或--one-file-xystem   # 以一开始处理时的文件系统为准，若遇上其它不同的文件系统目录则略过。
-X<文件>或--exclude-from=<文件>         # 在<文件>指定目录或文件。
--exclude=<目录或文件>  # 略过指定的目录或文件。
--max-depth=<目录层数>  # 超过指定层数的目录后，予以忽略。
--help                  # 显示帮助。
--version               # 显示版本信息。
```

### 排序

当前目录下如果文件太多，挨个查看大小势必非常麻烦，我们可以对它进行排序，借助 `sort` 命令

```bash
$ du -d 1 -h | sort -nr

148K	./layer-v3.1.1
116K	./cnblogs-article-information
 71M	./AdminLTE-2.4.2
 64K	./vegobot
 59M	./ace
```

但是排序有些问题，因为它只按照文件数字显示大小，不考虑单位，所以不使用单位即可

```bash
$ du -d 1 | sort -nr
$ du -d 1 | sort -nr | head     # 显示最大的前十
$ du -d 1 | sort -nr | tail     # 显示最小的前十
```














