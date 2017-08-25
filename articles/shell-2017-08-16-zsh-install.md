# zsh与oh-my-zsh 安装

## zsh
### linux安装
```bash
$ yum install zsh
$ chsh -s /bin/zsh # 将默认shell改为zsh
$ echo $SHELL # 查看是否生效
```
### mac
```bash
$ brew install zsh

$ which zsh
/usr/local/bin/zsh  # 执行which命令发现brew将zsh安装到了/usr/local/bin/zsh

# 所以首先需要将zsh执行脚本所在位置写入到/etc/shells 中，在进行chsh操作
$ sudo vim /etc/shells

# List of acceptable shells for chpass(1). 
  2 # Ftpd will not allow users to connect who are not using 
  3 # one of these shells. 
  4          
  5 /bin/bash 
  6 /bin/csh 
  7 /bin/ksh 
  8 /bin/sh  
  9 /bin/tcsh 
-10 /bin/zsh   
+10 /usr/local/bin/zsh


# 保存退出后在更换shell
$ chsh -s /usr/local/bin/zsh
$ echo $SHELL # 查看是否生效

```

## 安装oh-my-zsh
curl
```bash
$ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```
wget
```bash
$ sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```