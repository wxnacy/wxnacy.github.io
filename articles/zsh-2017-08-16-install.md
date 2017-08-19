# zsh 安装

## linux安装
```bash
$ yum install zsh
$ chsh -s /bin/zsh # 将默认shell改为zsh
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