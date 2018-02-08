#!/usr/bin/env bash

git submodule add --force https://github.com/tpope/vim-pathogen.git shells/vim/bundle/vim-pathogen                    # 更好的插件管理
git submodule add --force https://github.com/Valloric/YouCompleteMe shells/vim/bundle/YouCompleteMe                    # 代码补全
git submodule add --force https://github.com/altercation/vim-colors-solarized shells/vim/bundle/vim-colors-solarized   # 配色方案
git submodule add --force https://github.com/thinca/vim-quickrun shells/vim/bundle/vim-quickrun                        # 快速执行
git submodule add --force https://github.com/bling/vim-airline shells/vim/bundle/vim-airline                           # 状态栏
git submodule add --force https://github.com/junegunn/vim-easy-align shells/vim/bundle/vim-easy-align                  # 快速对齐
git submodule add --force https://github.com/scrooloose/nerdtree shells/vim/bundle/nerdtree                            # 显示文件菜单栏”
git submodule add --force https://github.com/Xuyuanp/nerdtree-git-plugin shells/vim/bundle/nerdtree-git-plugin         # 配合nerdtree，显示文件git提交信息
git submodule add --force https://github.com/jistr/vim-nerdtree-tabs shells/vim/bundle/vim-nerdtree-tabs               # 配合nerdtree，多tab显示一个nerdtree
git submodule add --force https://github.com/sjl/gundo.vim shells/vim/bundle/gundo.vim                                 # 查看文件编辑历史记录
git submodule add --force https://github.com/bronson/vim-trailing-whitespace shells/vim/bundle/vim-trailing-whitespace # 快速去掉行尾空格
git submodule add --force https://github.com/majutsushi/tagbar shells/vim/bundle/tagbar                                # 文件标签菜单
git submodule add --force https://github.com/scrooloose/nerdcommenter shells/vim/bundle/nerdcommenter                  # 快速注释
git submodule add --force https://github.com/docunext/closetag.vim shells/vim/bundle/closetag.vim                      # 编辑xml/html,自动补全闭合标签
git submodule add --force https://github.com/mattn/emmet-vim shells/vim/bundle/emmet-vim                               # 编辑html神器
git submodule add --force https://github.com/jiangmiao/auto-pairs shells/vim/bundle/auto-pairs                         # 成对标签自动补全
git submodule add --force https://github.com/kshenoy/vim-signature shells/vim/bundle/vim-signature                     # 书签展示以及快速跳转 增强vim的书签功能
git submodule add --force https://github.com/Lokaltog/vim-easymotion shells/vim/bundle/vim-easymotion                  # 快速跳转
git submodule add --force https://github.com/tpope/vim-surround shells/vim/bundle/vim-surround                         # 快速给词添加符号环绕
git submodule add --force https://github.com/tpope/vim-repeat shells/vim/bundle/vim-repeat                             # 重复一个插件的操作
git submodule add --force https://github.com/terryma/vim-expand-region shells/vim/bundle/vim-expand-region             # 区域选择
git submodule add --force https://github.com/ctrlpvim/ctrlp.vim shells/vim/bundle/ctrlp.vim                            # 文件搜索
git submodule add --force https://github.com/tacahiroy/ctrlp-funky shells/vim/bundle/ctrlp-funky                       # ctrlp插件，模糊搜索当前文件的函数
git submodule add --force https://github.com/vim-scripts/matchit.zip shells/vim/bundle/matchit.zip                     # 成对标签跳转,需要光标放在div等文字上
git submodule add --force https://github.com/terryma/vim-multiple-cursors shells/vim/bundle/vim-multiple-cursors       # 多光标操作
git submodule add --force https://github.com/scrooloose/syntastic shells/vim/bundle/syntastic                          # 语法检查
git submodule add --force https://github.com/dkprice/vim-easygrep.git shells/vim/bundle/vim-easygrep                   # 全局搜索插件
git submodule add --force https://github.com/mileszs/ack.vim.git shells/vim/bundle/ack.vim                             # 全局搜索插件
git submodule add --force https://github.com/dyng/ctrlsf.vim.git shells/vim/bundle/ctrlsf.vim                          # 搜索增强
git submodule add --force https://github.com/artur-shaik/vim-javacomplete2.git shells/vim/bundle/vim-javacomplete2     # java 代码不全
git submodule add --force https://github.com/pangloss/vim-javascript.git shells/vim/bundle/vim-javascript              # javascript 语法高亮
git submodule add --force https://github.com/mxw/vim-jsx.git shells/vim/bundle/vim-jsx                                 # react 语法高亮



# work for hexo them
git submodule add --force https://github.com/wxnacy/hexo-theme-yilia.git hexo/themes/yilia

# work for tmux
git submodule add --force https://github.com/tmux-plugins/tpm shells/tmux/plugins/tpm
