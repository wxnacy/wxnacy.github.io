---
title: Yum 安装的文件去哪了
date: 2018-04-21 10:33:27
tags: [linux]
---

借助 RPM 命令可以非常方便的查找 yum 安装包的所有路径。
<!-- more -->

**查找包名**

首先确定想要查找的完整包名，以 `wget` 为例

```bash
$ rpm -qa | grep wget
wget-1.18-3.28.amzn1.x86_64
```
`wget-1.18-3.28.amzn1.x86_64` 就是完整的按照包名

**查找所有路径**

```bash
$ rpm -ql wget-1.18-3.28.amzn1.x86_64
/etc/wgetrc
/usr/bin/wget
/usr/share/doc/wget-1.18
/usr/share/doc/wget-1.18/AUTHORS
/usr/share/doc/wget-1.18/COPYING
/usr/share/doc/wget-1.18/MAILING-LIST
/usr/share/doc/wget-1.18/NEWS
/usr/share/doc/wget-1.18/README
/usr/share/doc/wget-1.18/sample.wgetrc
/usr/share/info/wget.info.gz
/usr/share/locale/be/LC_MESSAGES/wget.mo
/usr/share/locale/bg/LC_MESSAGES/wget.mo
/usr/share/locale/ca/LC_MESSAGES/wget.mo
/usr/share/locale/cs/LC_MESSAGES/wget.mo
/usr/share/locale/da/LC_MESSAGES/wget.mo
/usr/share/locale/de/LC_MESSAGES/wget.mo
/usr/share/locale/el/LC_MESSAGES/wget.mo
/usr/share/locale/en_GB/LC_MESSAGES/wget.mo
/usr/share/locale/eo/LC_MESSAGES/wget.mo
/usr/share/locale/es/LC_MESSAGES/wget.mo
/usr/share/locale/et/LC_MESSAGES/wget.mo
/usr/share/locale/eu/LC_MESSAGES/wget.mo
/usr/share/locale/fi/LC_MESSAGES/wget.mo
/usr/share/locale/fr/LC_MESSAGES/wget.mo
/usr/share/locale/ga/LC_MESSAGES/wget.mo
/usr/share/locale/gl/LC_MESSAGES/wget.mo
/usr/share/locale/he/LC_MESSAGES/wget.mo
/usr/share/locale/hr/LC_MESSAGES/wget.mo
/usr/share/locale/hu/LC_MESSAGES/wget.mo
/usr/share/locale/id/LC_MESSAGES/wget.mo
/usr/share/locale/it/LC_MESSAGES/wget.mo
/usr/share/locale/ja/LC_MESSAGES/wget.mo
/usr/share/locale/lt/LC_MESSAGES/wget.mo
/usr/share/locale/nb/LC_MESSAGES/wget.mo
/usr/share/locale/nl/LC_MESSAGES/wget.mo
/usr/share/locale/pl/LC_MESSAGES/wget.mo
/usr/share/locale/pt/LC_MESSAGES/wget.mo
/usr/share/locale/pt_BR/LC_MESSAGES/wget.mo
/usr/share/locale/ro/LC_MESSAGES/wget.mo
/usr/share/locale/ru/LC_MESSAGES/wget.mo
/usr/share/locale/sk/LC_MESSAGES/wget.mo
/usr/share/locale/sl/LC_MESSAGES/wget.mo
/usr/share/locale/sr/LC_MESSAGES/wget.mo
/usr/share/locale/sv/LC_MESSAGES/wget.mo
/usr/share/locale/tr/LC_MESSAGES/wget.mo
/usr/share/locale/uk/LC_MESSAGES/wget.mo
/usr/share/locale/vi/LC_MESSAGES/wget.mo
/usr/share/locale/zh_CN/LC_MESSAGES/wget.mo
/usr/share/locale/zh_TW/LC_MESSAGES/wget.mo
/usr/share/man/man1/wget.1.gz
```

列出的就是全部文件的路径，通常 RPM 的默认安装路径为

- `/etc`              一些设置文件放置的目录如/etc/crontab
- `/usr/bin`          一些可执行文件
- `/usr/lib`          一些程序使用的动态函数库
- `/usr/share/doc`    一些基本的软件使用手册与帮助文档
- `/usr/share/man`    一些man page文件
