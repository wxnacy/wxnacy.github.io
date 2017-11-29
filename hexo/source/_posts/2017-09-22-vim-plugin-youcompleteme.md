---
title: Vim 插件 YouCompleteMe 代码自动补全
date: 2017-09-22 18:14:28
tags: [vim, python, javascript]
---

[专辑：Vim 练级手册](/vim)

> Vim 代码补全神器 [YouCompleteMe](https://github.com/Valloric/YouCompleteMe.git)

<!-- more -->

说到 ***YouCompleteMe*** 真是 Vim 开发必不可少的一个插件，功能全，速度快，
唯一的缺点就是安装起来太复杂，这也算是变相的“能量守恒”吧
废话不多说进入使用教程

## 预览
![ycm](/images/ycm.gif)

## 安装
### Pathogen
```bash
$ cd ~/.vim/bundle
$ git clone --recursive https://github.com/Valloric/YouCompleteMe
```
正常插件做到这一步就完成了，但是它还需要手动安装
```bash
$ cd ~/.vim/bundle/YouCompleteMe
$ ./install.sh --clang-completer
```
`--clang-completer` 代表支持 c-family 的补全，如果不需要可以去掉
如果想支持 Javascript 补全，需要加上参数 `--tern-completer` 详情见 [Vim 插件 tern_for_vim](/2017/09/22/vim-plugin-tern)

安装程序默认使用 py2 ，如果你使用 ***pyenv*** 可以使用 `./install.py` 进行安装，需要修改下环境变量
```bash
$ echo 'export PYTHON_CONFIGURE_OPTS="--enable-framework"' >> ~/.bash_profile
$ source ~/.bash_profile
```
随后需要重新下载新 pyenv 环境并且换到该环境进行安装
```bash
$ pyenv install 3.5.0
$ pyenv virtualenv 3.5.0 env_ycm
$ cd ~/.vim/bundle/YouCompleteMe
$ pyenv local env_ycm
$ ./install.py 
```
这样一来就静静的等待安装完成并体验了
***温馨提示：整个安装过程时间非常长，强烈建议找个网络环境好并且翻墙的环境***

### Vundle
修改 `~/.vimrc` 文件
```bash
Plugin 'Valloric/YouCompleteMe'
```
在 Vim 中运行
```bash
:PluginInstall
```
剩下的步骤就是跟上面以上执行 `./install.sh` 或 `./install.py` 了

## 配置
```bash
" 方法跳转 "
nnoremap <leader>gl :YcmCompleter GoToDeclaration<CR>
nnoremap <leader>gf :YcmCompleter GoToDefinition<CR>
nnoremap <leader>gg :YcmCompleter GoToDefinitionElseDeclaration<CR>
```
