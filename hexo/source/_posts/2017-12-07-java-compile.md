---
title: Java 编译命令
date: 2017-12-07 14:36:29
tags: [java]
---

在刚学 Java 那会儿老师一再告诫要先用 Text 文本编辑程序，并能手动编译运行才行，因为只有这样才能搞清楚它的编译原理。然而实际开发中因为各种 IDE 开发工具的介入，Java 的编译不再成为我们关注的重点，在接触 Python 的一年后，我发现我“不会” Java 了，除了在 IDEA 上点击个按钮跑程序外，我不会手动编译一个多包引用的程序了。这让我很惶恐，借着想要抛弃 IDE ，拥抱 Vim 的机会，我来总结下 Java 编译命令。

<!-- more --><!-- toc -->
## Hello World
先从最简单的 `Hello World` 开始，创建 `Main.java` 文件内容如下
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
    }
}
```
通过 `javac` 进行编译
```bash
$ javac Main.java
$ java Main
```
```bash
Hello World!
```
所有学 Java 的人都是从这开始的，我不多说。如果我们的程序都是这样的单文件就好了，但是 Java 有包的概念，一个一个程序封装在包里等待其他程序调用，就像下边的文件结构一样。
## 指定 classpath
```bash
project--|--src--|--Main.java
                 |--common--|--Utils.java
```
`Utils.java` 内容如下
```java
package common;

public class Utils {
    public static String getName(){
        return "wxnacy";
    }
}
```
此时 `Main.java` 文件内容如下
```java
import common.Utils;

public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        String name = Utils.getName();
        System.out.println(name);
    }
}
```
这次我们进入 `project` 目录并执行 `javac src/Main.java`
```bash
src/Main.java:1: 错误: 程序包common不存在
import common.Utils;
             ^
src/Main.java:7: 错误: 找不到符号
String name = Utils.getName();
                    ^
符号:   变量 Utils
位置: 类 Main
2 个错误
```
报错了，找不到包，因为我们还没有编译它所需要的 `Utils.java` 程序，这时我们引入一个新的参数 `-classpath, -cp` ，我们需要先编译 `Utils.java` 并通过该参数指定 class 文件所在位置
```bash
javac src/common/Utils.java     # 编译 Utils.java
# 在 src/common 目录下生成 Utils.class
javac -cp src src/Main.java     # 指定 classpath 为 src 并编译 Main.java 
java -cp src Main               # 指定 classpath 并运行
```
```bash
Hello World!
wxnacy
```
这次我们得到了想要结果，但是运行会发现，这样的生成的 class 文件到处都是，这不是我们想要的，我们希望它能把所有的 class 生成到一个文件中，由此需要在引入一个参数 `-d` 用来指定生成目录
## 指定生成目录
```bash
mkdir target
javac -cp target -d target src/common/Utils.java
javac -cp target -d target src/Main.java
java -cp target Main
```
我们创建 `target` 目录，并指定该目录，这样生成的 class 文件都会在 target 中看到，源码与编译结果分离就是我们想要的。现在想想还差什么吗，把它放到实际开发中会怎么样呢？我扫了眼以前的项目，最少的也有几十个 java 文件，我们怎么能把那么多的文件的引用先后顺序都罗列出来呢？还好 javac 帮我解决了这个问题
```bash
javac -cp target -d target src/Main.java src/common/Utils.java
```
```bash
javac -cp target -d target @source.txt
# source.txt
# src/Main.java
# src/common/Utils.java
```
`javac` 可以接受多个文件，这时我们不用在关心他们的调用顺序，程序会自动根据需要来编译，它也可以接受一个 `source.txt` 文件跟在 `@` 后，内容是源码文件路径的列表。

现在我们来回顾一下，多包，源码分离，自动处理编译顺序，似乎都解决了。好了，我知道你要说还是不方便，那么多个源码文件，我不能每次编译都罗列一遍或者手动添加到 `source.txt` 中吧，确实，我不止一次说过，**懒是第一生产力**，我们还要处理的更方便一些，这次我们需要写一些 bash 脚本来帮忙了
## 编写编译脚本
```bash
$ touch run.sh
$ chmod +x run.sh
$ vim run.sh
```
```bash
#!/usr/bin/env bash

SOURCE_PATH=src
VIM_PROJECT_HOME=.vim
TARGET=target
CLASS_PATH=${TARGET}/classes
SOURCE_TXT=${VIM_PROJECT_HOME}/source.txt

list_file(){
    # 遍历源码目录并输出到 ${SOURCE_TXT} 中
    for file in `ls $1`
    do
        if test -f $file
        then
            echo $file >> ${SOURCE_TXT}
        else
            list_file $1/$file
        fi
    done
}
compile(){
    # 编译
    if [ ! -d "${VIM_PROJECT_HOME}"  ]; then
        mkdir ${VIM_PROJECT_HOME}
    fi
    if [ ! -d "${TARGET}"  ]; then
        mkdir ${TARGET}
    fi
    rm -rf ${CLASS_PATH}
    if [ ! -d "${CLASS_PATH}"  ]; then
        mkdir ${CLASS_PATH}
    fi
    rm -rf ${SOURCE_TXT}
    touch ${SOURCE_TXT}
    list_file ${SOURCE_PATH}
    cat ${SOURCE_TXT}
    javac -cp ${CLASS_PATH} -d ${CLASS_PATH} @${SOURCE_TXT}
}
compile
java -cp ${CLASS_PATH} Main
```
```bash
Hello World!
wxnacy
```
在项目根目录下进行这些操作，如果你看到最后的输出，说明你成功了。这个脚本的编写不在我们本次探讨的范围，你只需要知道 `list_file()` 方法就是在做我们刚才说的自动列出源码文件地址列表，整个脚本做到到了编译项目，并运行 `Main.java` 的目的。如果你还对这个脚本的编写感兴趣，请关注我其他的文章。
