---
title: iTerm2 使用 expect 无密码登录服务器
tags:
  - iterm
  - expect
date: 2018-02-26 11:43:05
---


之前介绍过[使用 expect 交互免输入密码](/2017/09/15/linux-2017-09-15-expect/)，你也可以跟 iTerm 配合在进行无密码登录服务器
<!-- more -->
首先编辑登录脚本 `/data/test_ssh.sh`
```bash
#!/usr/bin/env expect
set user root
set host your_host
set password your_password
set timeout -1

spawn ssh $user@$host
expect "*assword:*"
send "$password\r"
interact
expect eof
```

然后在 iTerm 界面通过快捷键 `command + ,` 进入设置界面，并使用下图进行配置
![/images/iterm2.png](/images/iterm2.png)

最后如下图所示右键选择配置完成的标签，即可打开新窗口并自动登录到服务器
![/images/iterm3.png](/images/iterm3.png)

