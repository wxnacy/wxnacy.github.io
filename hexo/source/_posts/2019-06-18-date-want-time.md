---
title: Linux date 获取指定时间
date: 2019-06-18 11:07:25
tags: [linux]
---

最近要写一些清洗数据的脚本，需要用到各种日期格式，今天来探讨下使用 `date` 命令的 `-d/--date` 参数来获取指定时间。

<!-- more -->
<!-- toc -->

`-d/--date` 是非常强大且语法很多样复杂的参数，我了解的可能并不全面，想到哪里说到哪，提到的东西只能保证满足日常开发需求。

**本文提到的命令都是在 Linux 环境下进行的，Mac 环境需要下载 `GNU` 相应的命令。**

## 时间戳

将描述转换为 UTC 时间 1970-01-01 以后的时间

```bash
$ date -d '@12'
Thu Jan  1 00:00:12 UTC 1970
```

很明显我们可以用它来做时间戳的格式化

```bash
$ date -d '@1560825826'
Tue Jun 18 02:43:46 UTC 2019
```

然后可以使用 `+FORMAT` 将时间转为时间戳

```bash
$ date -d '2019-06-18 11:36:19' +%s
1560857779
```

## 时区

服务器一般默认使用的是 UTC 时区

```bash
$ date
Tue Jun 18 03:41:35 UTC 2019
```

返回指定时区格式

```bash
$ TZ="Asia/Shanghai" date
Tue Jun 18 11:28:42 CST 2019
```

设置指定时间的时区

```bash
$ date -d 'TZ="Asia/Shanghai" 2019-06-18 11:13:59'
Tue Jun 18 03:13:59 UTC 2019
```

世界时区名称列表 [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

## datestr

`-d/--date` 的语法为

```bash
$ date -d datestr
```

前面我们已经简单领略了他的使用方式，下面详细说说他都支持什么格式。

### 时间戳

这里注意一定要前面加上 `@` 符号

```bash
$ date -d '@12'
Thu Jan  1 00:00:12 UTC 1970
```

### 时间格式

如果不加 `@` 会怎么样呢，如果传入的数字默认返回当天的指定小时的时间，取值 [0, 23]

```bash
$ date -d '12'
Tue Jun 18 12:00:00 UTC 2019
```

更复杂的格式化按照标准格式 `YYYY-mm-dd HH:MM:SS` 来指定

```bash
$ date -d '2019-06-18 11:58:20'
Tue Jun 18 11:58:20 UTC 2019
```

```bash
$ date -d '11:20'
Tue Jun 18 11:20:00 UTC 2019
```

咦？似乎这样的设置没什么意义啊，固定的日子和时间，我为什么要多此一举的用 `date` 在获取一次。确实，它再搭配一点其他的语句就有很大的用处了。

### next 关键字

`next` 关键字可以让上面的命令更有意义

获取明天 9 点的时间

```bash
$ date -d '9 next day'
Wed Jun 19 09:00:00 UTC 2019
```

下周

```bash
$ date -d '9 next week'
Wed Jun 25 09:00:00 UTC 2019
```

下周一

```bash
$ date -d '9 next Mon'
Wed Jun 24 09:00:00 UTC 2019
```

下个月

```bash
$ date -d '9 next month'
Wed Jun 24 09:00:00 UTC 2019
```

如你所见，`next` 后面跟一个符合常理的时间或缩写就可以获取指定时间以后的某个时间，如果去掉 `9`，则返回的是当前时间以后的时间。

下一分钟

```bash
$ date -d 'next minute'
Tue Jun 18 04:13:04 UTC 2019
```

总结下 `next` 后面跟的参数

- `second[s]` `minute[s]` `hour[s]` `day[s]` `week[s]` `month[s]` `year[s]`
- 星期 `Sun[day]` `Mon[day]` `Tue[sday]` `Wed[nesday]` `Thu[rsday]` `Fri[day]` `Sat[urday]`

### ago 关键字

可以获取之后，就可以获取之前的时间，安装英语的语法应该这样的

一分钟前

```bash
$ date -d '1 minute ago'
Tue Jun 18 06:31:15 UTC 2019
```

`09:00` 的一分钟前

```bash
$ date -d '09:00 minute ago'
Tue Jun 18 08:59:00 UTC 2019
```

相信不用多举例，你也已经可以明白它的用法了，另外最前面的数字可以为负数，代表的是时间以后。下面两种方式都是获取以后以后的时间

```bash
$ date -d '-1 day ago'
Wed Jun 19 06:36:53 UTC 2019

$ date -d 'next day'
Wed Jun 19 06:37:00 UTC 2019
```

总结下 `ago` 前可以使用的参数
- `second[s]` `minute[s]` `hour[s]` `day[s]` `week[s]` `month[s]` `year[s]`

