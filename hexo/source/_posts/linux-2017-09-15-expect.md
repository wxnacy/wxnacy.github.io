---
title: 使用 expect 交互免输入密码
date: 2017-09-15
tags: [linux, expect]
---
> Expect是一个免费的编程工具语言，用来实现自动和交互式任务进行通信，而无需人的
干预。

<!-- more -->

<!-- toc -->
## 简单的免输入密码

在工作经常会使用 ssh、ftp、 mysql 等命令，但每次输入密码会让事情变的很枯燥，
重复的事情就要交给脚本去做，这时候我们需要用到 **[expect](http://expect.sourceforge.net/)** ，
下面我们通过一个例子 *mysql_login* 来说明


```bash
#!/usr/bin/env expect
set password xxxxx
set name root

spawn mysql -u$name -p
expect "*assword:*"
send "$password\r"
interact
```
上边这段脚本是在登录本地 mysql 时，无需输入密码就自动登录
```bash
$ expect mysql_login
```
执行代码不能用 *sh file* 而是 *expect mysql_login* ，如果你在文件开头加上
`#!/usr/bin/env expect` 也可以用 `./mysql_login` 来执行

其他语句解释如下：

- **spawn**：spawn是expect的语句，执行命令前都要加这句
- **expect "*assword:*"**：这句意思是交互获取是否返回 password：关键字，因为在
执行 mysql 时会返回输入 password 的提示 xxxxxxxx password:
- **send**：将密码发送出去
- **interact**：代表执行完留在远程控制台，不加这句执行完后返回本地控制台

你可以仿照这段脚本写其他服务自动登录脚本，但是 ssh 无密码登录我推荐使用
[SSH 登陆远程服务器和无密码操作](/2017/08/23/linux-2017-08-23-ssh/)文章中提到的
不对称加密登录方式

## 其他用法

### 传入参数
参数传入跟 bash 一样，都是执行命令后跟参数，如：`./mysql_login p1 p2 p3 p4`
但是接收有很大不同，在 bash 中我们只需要使用 **$1 $2** 来接收第一个和第二个参数
但是在 expect 中我们需要用到 **$arg** 关键字来获取参数
```bash
puts $argv                      ==> p1 p2 p3 p4     # 输出参数数组
puts $argc                      ==> 4               # 输出参数个数
puts [lindex $argv 0]           ==> p1              # 使用 lindex 关键字获取第一个参数
puts [lrange $argv 0 2]         ==> p1 p2 p3        # 使用 lrange 关键字获取第一个到第三个参数
```

### 读取设置环境变量
不同于 bash 通过 export 和 echo 在设置和输出环境变量
expect 需要通过 **set** 和 **puts** 进行设置和输出
并且需要变量名需要用 **env()** 包起来
```bash
wxnacy@wxnacydeMacBook-Pro ~/W/w/s/mysql> expect
expect1.1> set env(NAME) "wxnacy"       # 设置环境变量，NAME 就是在 bash 中用到的环境变量
wxnacy
expect1.2> puts $env(NAME)              # 打印环境变量
wxnacy
```

### 流程控制 if
与绝大多数语言一样 expect 也可以通过 **if** 来控制程序流程，与绝大多数语言不同
的是 expect 中 **if** 的条件语句是包含在大括号中的，如：`if { name == "wxnacy" }`
```bash
if { $argc < 1 } {
    send_user 'Usage: ./mysql_login arg1'
}
```

## 参考文献
- [expect - 自动交互脚本](http://xstarcd.github.io/wiki/shell/expect.html)
- [expect使用详解](http://blog.51niux.com/?id=55)
