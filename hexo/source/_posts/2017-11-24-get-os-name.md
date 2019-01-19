---
title: 如何判断 Unix 系统 OS 版本
date: 2017-11-24 10:24:37
tags: [linux, mac]
---

在编写自动化脚本时，经常会需要对系统版本进行区分，以便做自适应，这样就需要精确的获取当前操作系统的系统名，甚至发行版本，接下来我们来一步步探讨如果区分 Mac， Linux 及 Linux 中各个系统版本，本教程对 Windows 系统是废的，或者说 Windows 是废的

<!-- more -->

<!-- toc -->

## Uname
首先先来区分 Mac 和 Linux 系统，我们来使用 [Uname](https://en.wikipedia.org/wiki/Uname) 命令它可以判断系统名称，版本，内核等信息

### Linux
在 Linux 中使用规则为
```bash
$ uname [-amnprsvio]    # 默认使用 -s
```
具体参数定义
```bash
-a, --all               # 输出所有信息。其中若 -p 和 -i 的探测没有结果则被省略
-s, --kernel-name       # 输出内核名称(Linux)
-n, --nodename          # 输出网络节点上的主机名
-r, --kernel-release    # 输出内核版本
-v, --kernel-version    # 输出内核发行时间
-m, --machine           # 输出主机的硬件架构名称(和64位,32位有关)
-p, --processor         # 输出处理器类型或“unknown”
-i, --hardware-platform # 输出硬件平台或“unknown”
-o, --operating-system  # 输出操作系统名称(GNU/Linux)
    --help              # 显示此帮助信息并离开
    --version           # 显示版本信息并离开
```

### Mac
在 Mac 中使用规则基本和 Linux 一样，唯一区别在于没有 `-i, -o` 两个参数
```bash
$ uname [-amnprsv]    # 默认使用 -s
```

知道这些我们区分这两个系统已经足够，及使用 `uname -s` 命令即可

## /etc/os-release

在区分 Mac／Linux 之后我们要来谈谈怎样更好的区分 Linux 各个发行版本，毕竟现在发行版本还是很多的，每个版本的组件使用又不尽相同，我们拿最常用到的 CentOS 和 Ubuntu 最新的版本来举例说明

在 Linux 系统中有一个 os-release 文件，位置在 `/etc/os-release` 从名字我们就明白它是记录 OS 的发行版本的，它在两个系统中的内容分别如下

### CentOS
```bash
NAME="CentOS Linux"
VERSION="7 (Core)"
ID="centos"
ID_LIKE="rhel fedora"
VERSION_ID="7"
PRETTY_NAME="CentOS Linux 7 (Core)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:centos:centos:7"
HOME_URL="https://www.centos.org/"
BUG_REPORT_URL="https://bugs.centos.org/"

CENTOS_MANTISBT_PROJECT="CentOS-7"
CENTOS_MANTISBT_PROJECT_VERSION="7"
REDHAT_SUPPORT_PRODUCT="centos"
REDHAT_SUPPORT_PRODUCT_VERSION="7"
```

### Ubuntu
```bash
NAME="Ubuntu"
VERSION="16.04.2 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.2 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
```

这些信息中，我们暂时只用 ID 属性，在 Linux 中我们可以使用 `source` 命令来将文件中的 `k-v` 数据倒入到上下文中
```bash
$ source /etc/os-release
$ echo $ID      # --> ubuntu
```

## 编写脚本

知道了上边这些我们来写一个简单脚本，以达到判断系统并使用相应的安装工具安装 Git

```bash
OS=`uname -s`
if [ ${OS} == "Darwin"  ];then
    sudo brew install git
elif [ ${OS} == "Linux"  ];then
    source /etc/os-release
    case $ID in
        debian|ubuntu|devuan)
            sudo apt-get install git
            ;;
        centos|fedora|rhel)
            yumdnf="yum"
            if test "$(echo "$VERSION_ID >= 22" | bc)" -ne 0;
            then
                yumdnf="dnf"
            fi
            sudo $yumdnf install -y git
            ;;
        *)
            exit 1
            ;;
    esac
else
    echo "Other OS: ${OS}"
fi
```

## /etc/issue

`/etc/issue` 也放了发行版本信息，但是少得可怜。

```bash
$ cat /etc/issue
Ubuntu 14.04.5 LTS \n \l
```

## 其他版本
这个脚本基本可以满足简单的判断系统和版本的需求，但是在写这篇文章的时候，我发现 CentOS 6 及以前的版本是没有 `/etc/os-release` 文件的，只有 `/etc/centos-release` 也没有 `k-v` 信息，只有简单的 `CentOS release 6.8 (Final)` 信息，如何更好的区分这个版本，是我们下一步需要探讨的。
