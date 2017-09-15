# 使用 expect 交互免输入密码

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
执行代码不能用 *sh file* 而是 *expect mysql_login* ，如果你在文件开头加上 *#!/usr/bin/env expect* 也可以用 *./mysql_login* 来执行

其他语句解释如下：

- **spawn**：spawn是expect的语句，执行命令前都要加这句
- **expect "*assword:*"**：这句意思是交互获取是否返回 password：关键字，因为在执行 mysql 时会返回输入 password 的提示 xxxxxxxx password:
- **send**：将密码发送出去
- **interact**：代表执行完留在远程控制台，不加这句执行完后返回本地控制台

你可以仿照这段脚本写其他服务自动登录脚本，但是 ssh 无密码登录我推荐使用[SSH 登陆远程服务器和无密码操作](/linux/2017/08/23/ssh)文章中提到的不对称加密登录方式
