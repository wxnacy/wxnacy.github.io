#!/usr/bin/env bash
git submodule add --force https://github.com/tpope/vim-pathogen.git shells/vim/bundle/vim-pathogen
# git submodule add http://github.com/gmarik/Vundle.vim shells/vim/bundle/Vundle.vim                 # 插件管理
git submodule add --force http://github.com/Valloric/YouCompleteMe shells/vim/bundle/YouCompleteMe            # 代码补全
# git submodule add http://github.com/altercation/vim-colors-solarized shells/vim/bundle/vim-colors-solarized  # 配色方案
git submodule add --force http://github.com/thinca/vim-quickrun shells/vim/bundle/vim-quickrun               # 快速执行
git submodule add --force http://github.com/bling/vim-airline shells/vim/bundle/vim-airline                 # 状态栏
git submodule add --force http://github.com/junegunn/vim-easy-align shells/vim/bundle/vim-easy-align           # 快速对齐
git submodule add --force http://github.com/scrooloose/nerdtree shells/vim/bundle/nerdtree               # 显示文件菜单栏”
git submodule add --force http://github.com/Xuyuanp/nerdtree-git-plugin shells/vim/bundle/nerdtree-git-plugin       # 配合nerdtree，显示文件git提交信息
git submodule add --force http://github.com/jistr/vim-nerdtree-tabs shells/vim/bundle/vim-nerdtree-tabs           # 配合nerdtree，多tab显示一个nerdtree
git submodule add --force http://github.com/sjl/gundo.vim shells/vim/bundle/gundo.vim                     # 查看文件编辑历史记录
git submodule add --force http://github.com/bronson/vim-trailing-whitespace shells/vim/bundle/vim-trailing-whitespace   # 快速去掉行尾空格
git submodule add --force http://github.com/majutsushi/tagbar shells/vim/bundle/tagbar                 # 文件标签菜单
git submodule add --force http://github.com/scrooloose/nerdcommenter shells/vim/bundle/nerdcommenter          # 快速注释
git submodule add --force http://github.com/docunext/closetag.vim shells/vim/bundle/closetag.vim             # 编辑xml/html,自动补全闭合标签
git submodule add --force http://github.com/mattn/emmet-vim shells/vim/bundle/emmet-vim                   # 编辑html神器
git submodule add --force http://github.com/jiangmiao/auto-pairs shells/vim/bundle/auto-pairs              # 成对标签自动补全
git submodule add --force http://github.com/kshenoy/vim-signature shells/vim/bundle/vim-signature             # 书签展示以及快速跳转 增强vim的书签功能
git submodule add --force http://github.com/Lokaltog/vim-easymotion shells/vim/bundle/vim-easymotion           # 快速跳转
git submodule add --force http://github.com/tpope/vim-surround shells/vim/bundle/vim-surround                # 快速给词添加符号环绕
git submodule add --force http://github.com/tpope/vim-repeat shells/vim/bundle/vim-repeat                  # 重复一个插件的操作
git submodule add --force http://github.com/terryma/vim-expand-region shells/vim/bundle/vim-expand-region         # 区域选择
git submodule add --force http://github.com/ctrlpvim/ctrlp.vim shells/vim/bundle/ctrlp.vim                # 文件搜索
git submodule add --force http://github.com/tacahiroy/ctrlp-funky shells/vim/bundle/ctrlp-funky             # ctrlp插件，模糊搜索当前文件的函数
git submodule add --force http://github.com/vim-scripts/matchit.zip shells/vim/bundle/matchit.zip           # 成对标签跳转,需要光标放在div等文字上
git submodule add --force http://github.com/terryma/vim-multiple-cursors shells/vim/bundle/vim-multiple-cursors      # 多光标操作
# git submodule add --force http://github.com/klen/python-mode shells/vim/bundle/python-mode                  # python 开发集大成插件
git submodule add --force http://github.com/scrooloose/syntastic shells/vim/bundle/syntastic              # 语法检查
# git submodule add http://github.com/kevinw/pyflakes-vim shells/vim/bundle/pyflakes-vim               # 搭配语法检查的pyflakes
# git submodule add http://github.com/w0rp/ale shells/vim/bundle/ale                          # 语法检查
# git submodule add http://github.com/davidhalter/jedi-vim shells/vim/bundle/jedi-vim              # python 代码提示
# git submodule add http://github.com/Shougo/deoplete.nvim,shells/vim/bundle/deoplete.nvim { 'do': ':UpdateRemotePlugins' } #代码补全
