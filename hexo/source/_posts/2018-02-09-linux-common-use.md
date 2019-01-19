---
title: Shell 常用语法
tags:
  - shell
date: 2018-02-09 15:16:50
---


记录一些常用的 Shell 语法

<!-- more --><!-- toc -->

## 参数
文件接收参数
```bash
$ echo 'echo $1 $2' > test.sh
$ chmod +x test.sh
$ ./test.sh name age

name age
```
函数接受参数
```bash
main() {
    echo $1 $2      # --> name age
}
main name age
```

## 判断
判断字符串相等
```bash
if [ $sysOS == "Darwin"  ];then
# do something
fi
```
判断字符串为空或不存在
```bash
ENV=$1

if [ ! ${ENV} ]
then
    ENV=local
fi
```
判断是否有某个文件
```bash
if [ -f ~/.bash_profile  ]; then
    # do something
fi
```
判断是否有某个目录
```bash
if [ -d ~/.oh-my-zsh   ]; then
    # do something
else
    # else do something
fi
```
## case
```bash
case $ID in
    debian|ubuntu|devuan)
        # do something
        ;;
    centos|fedora|rhel)
        # do something
        ;;
    *)
        exit 1
        ;;
esac
```

## 其他
当前环境生效环境变量
```bash
export NODE_PATH=`pwd`/nodejs
```
执行某个文件
```bash
source ~/.bash_profile
```
