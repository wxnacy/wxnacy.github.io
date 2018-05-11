"===============================
" Name: wxnacy's Vim setting
" Author: wxnacy <wxnacy@gmail.com>
" URL: https://wxnacy.com
" Created: 2017-08-27
" Modified: 2017-10-26
" Description:
"===============================


"==============================="
" 基本设置
"==============================="

" base
set nocompatible				"去掉对vi的兼容，让vim运行在完全模式下
syntax on    					"开启语法高亮"
set history=2003                "记录VIM历史操作的条数
set autoread					"文件在vim外修改过自动重新载入
au CursorHold,CursorHoldI * checktime   " 自动加载文件变动"
set magic                       "magic (\m)：除了 $ . * ^ 之外其他元字符都要加反斜杠。nomagic (\M)：除了 $ ^ 之外其他元字符都要加反斜杠。
set title
set nobackup                    "去掉编辑文件时的备份
set novisualbell                "关掉可视化响铃警报
set noerrorbells                "关掉错误警报
set visualbell t_vb=            "关掉警报
set tm=500
set t_Co=256
" leader
let mapleader = ';'
let g:mapleader = ';'


" filetype
filetype on                     "开启文件类型检测
filetype plugin on              "开启插件的支持
filetype indent on              "开启文件类型相应的缩进规则
set fileformat=unix    			"设置以unix的格式保存文件"

" encoding
set encoding=utf-8              "打开文件时编码格式
set fileencodings=ucs-bom,utf-8,cp936,gb18030,big5,euc-jp,euc-kr,latin1         "vim会根据该设置识别文件编码

" set fileencoding=utf-8        在保存文件时，指定编码
set termencoding=utf-8          "终端环境告诉vim使用编码
set ffs=unix,dos,mac            "在创建文件或写入时，这三种文件格式分别决定了行末要添加什么特殊字符，而在读入文件时，又分别决定了要从行末移去什么特殊字符。
set formatoptions+=m
set formatoptions+=B

" 主题
set background=dark       		"配色主题的色系,注意，这不是什么背景色！dark 是暗色系，light 是亮色系。
colorscheme desert              "配色主题的名称,:coloscheme 后键入<tab>可以自动补全 比较喜欢的desert,peachpuff,torte,elfload,slate

" show
set number						"显示行号"
set ruler						"显示当前光标行号和列
" set nowrap    					"设置不折行"
set wrap    					"设置折行"
set sidescroll=1                "默认设置set sidescroll=0之下，当光标到达屏幕边缘时，将自动扩展显示1/2屏幕的文本。通过使用set sidescroll=1设置，可以实现更加平滑的逐个字符扩展显示。
set showcmd						"在屏幕右下角显示未完成的命令
set showmode					"显示当前vim模式
set showmatch    				"显示匹配的括号"
set matchtime=1					"设置showmatch的效果时间，默认500ms，现在是100ms
set cursorline        			"突出显示当前行"
set cursorcolumn        		"突出显示当前列"
set colorcolumn=80              "设置某一列高亮"


" search
set smartcase					"搜索时，如果输入大写，则严格按照大小写搜索，如果小写，并设置了ignorecase，则忽略大小写
set ignorecase        			"搜索时忽略大小写"
set incsearch					"搜索时及时匹配搜索内容，需要回车确认
set hlsearch        			"高亮搜索项"

" tab
set expandtab                   "将<tab>符号转变为<space>空格
set smarttab					"配合shiftwidth使用，如果设置该值，在行首键入<tab>会填充shiftwidth的数值,其他地方使用tabstop的数值，不设置的话，所有地方都是用shiftwidth数值

" indent
set autoindent                  "换行自动缩进
set smartindent                 "缩进采用c语言风格
set shiftround                  "在一般模式下键入>>整个缩进shiftwidth的长度，<<反向操作,== 可以与上一行对齐，插入模式下C-T和C-D也可以左右启动
set shiftwidth=4                "缩进的空格数
set tabstop=4                   "键入<tab>的步长
set softtabstop=4                " insert mode tab and backspace use 4 spaces

" set mark column color
hi! link SignColumn   LineNr
hi! link ShowMarksHLl DiffAdd
hi! link ShowMarksHLu DiffChange

" status line
" set statusline=%<%f\ %h%m%r%=%k[%{(&fenc==\"\")?&enc:&fenc}%{(&bomb?\",BOM\":\"\")}]\ %-14.(%l,%c%V%)\ %P
set laststatus=2   " Always show the status line - use 2 lines for the status bar


" select & complete
set selection=inclusive         "选择文本事，光标所在位置也会被选中
set selectmode=mouse,key

set scrolloff=5        			"距离顶部和底部5行"
set backspace=2					"任何情况允许使用退格键删除
set mouse=a       				"启用鼠标"

" 代码折叠
set foldlevelstart=99           "默认不折叠"
set foldmethod=indent           "按照缩紧折叠"

" Mapping ================== {{{
" 快速打开 vimrc文件
nnoremap <Leader>vw :vsp ~/.vim/vimrc<CR>
nnoremap <Leader>vs :source $MYVIMRC<CR>:nohls<CR>
nnoremap <Leader>tw :vsp ~/.tmux.conf<CR>
nnoremap <Leader>mw :vsp ~/VimProjects/vim-mysql/plugin/mysql.vim<CR>
nnoremap <Leader>ms :source ~/VimProjects/vim-mysql/plugin/mysql.vim<CR>
nnoremap <Leader>vj :vsp ~/VimProjects/vim-java/plugin/vimjava.vim<CR>
nnoremap <Leader>sj :source ~/VimProjects/vim-java/plugin/vimjava.vim<CR>
nnoremap <Leader>jsw :vsp ~/.vim/syntax/javascript.vim<CR>
nnoremap <Leader>pyw :vsp ~/.vim/syntax/python.vim<CR>
nnoremap <Leader>sshw :vsp ~/.ssh/config<CR>
nnoremap <Leader>zshw :vsp ~/.zshrc<CR>
nnoremap <Leader>vsp :vsp ~/.vim/syntax/python.vim<CR>
nnoremap <Leader>vsmd :vsp ~/.vim/syntax/markdown.vim<CR>
nnoremap <Leader>vsjs :vsp ~/.vim/syntax/javascript.vim<CR>
nnoremap <Leader>vsj :vsp ~/.vim/syntax/java.vim<CR>
nnoremap <Leader>vn :vsp /usr/local/etc/openresty/nginx.conf<CR>
" nnoremap <Leader>lw :vsp ~/VimProjects/vim-linux/plugin/linux.vim<CR>
" nnoremap <Leader>ls :source ~/VimProjects/vim-linux/plugin/linux.vim<CR>
" 重新加载文件
" nnoremap <Leader>ar :e<CR>
" 选中全部
nnoremap <Leader>sa ggVG
" 删除全部
nnoremap <Leader>da ggdG
" 快速推出
nnoremap <Leader>q :q<CR>
" 快速保存
nnoremap <Leader>w :w<CR>
" 快速保存推出
nnoremap <Leader>wq :wq<CR>
" 快速返回常用模式
inoremap jk <esc>
vnoremap jk <esc>
" 修改撤销快捷键
nnoremap U u
nnoremap u <nop>
" 快速查看 messages
nnoremap <Leader>vm :messages<CR>
" 使用 <C-hjkl> 进行移动窗口，不必输入 w
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l
" 去掉高亮
nnoremap <Leader>nh :nohls<CR>
" 模拟IDE<tab>键
" 单行的缩紧退回和选中模式下的缩进退回
nnoremap <tab> V>
nnoremap <S-tab> V<
vnoremap <tab> >gv
vnoremap <S-tab> <gv
" 上下移动文本
nnoremap <Leader>k ddkP
nnoremap <Leader>j ddp
vnoremap <Leader>k dkP
vnoremap <Leader>j dp
" 文本超出屏幕时左右移动
nnoremap <Leader>l 79l
nnoremap <Leader>h 79h

" 插入模式快速移动到行首和行尾
" nnoremap <C-a> I
nnoremap <C-e> A
inoremap <C-a> <esc>I
inoremap <C-e> <esc>A
cnoremap <C-a> <Home>
cnoremap <C-e> <End>
" 插入模式快速左右移动一格
inoremap <Leader>l <esc>la
inoremap <Leader>h <esc>i
inoremap <Leader>j <esc>ja
inoremap <Leader>k <esc>ka
" 插入模式右删除一格
inoremap <C-l> <esc>lxi

" 复制和系统剪贴板交互
nnoremap <C-y> "+Y
vnoremap <C-y> "+y
" 黏贴系统剪切版的内容
nnoremap <C-p> "+p
inoremap <C-p> <esc>"+pi
" 复制黏贴
nnoremap yp yyp

" 快速选中当前行有效文字区域
nnoremap vv I<esc>lvg_

" 快速添加成对标签
" nnoremap <Leader>" eb<esc>i"<esc>ea"<esc>
" nnoremap <Leader>" viw<esc>a"<esc>bi"<esc>lel
nnoremap <Leader>" viw<esc>bi"<esc>ea"<esc>
nnoremap <Leader>' viw<esc>bi'<esc>ea'<esc>
nnoremap <Leader>` viw<esc>bi`<esc>ea`<esc>
nnoremap <Leader>[ viw<esc>bi[<esc>ea]<esc>
nnoremap <Leader>{ viw<esc>bi{<esc>ea}<esc>
nnoremap <Leader>( viw<esc>bi(<esc>ea)<esc>
vnoremap <Leader>" di""<esc>hp
vnoremap <Leader>' di''<esc>hp
vnoremap <Leader>` di``<esc>hp
vnoremap <Leader>( di()<esc>hp
vnoremap <Leader>{ di{}<esc>hp
vnoremap <Leader>[ di[]<esc>hp
nnoremap <Leader><Leader>" <s-i>"<esc><s-a>"<esc>
nnoremap <Leader><Leader>' <s-i>'<esc><s-a>'<esc>
nnoremap <Leader><Leader>` <s-i>`<esc><s-a>`<esc>
nnoremap <Leader><Leader>[ <s-i>[<esc><s-a>]<esc>
nnoremap <Leader><Leader>{ <s-i>{<esc><s-a>}<esc>
nnoremap <Leader><Leader>( <s-i>(<esc><s-a>)<esc>

" 快速在行尾巴插入分号;
nnoremap <Leader>, mzA;<esc>`z
inoremap <Leader>, <esc>mzA;<esc>`za
nnoremap <Leader><Leader><space> viw<esc>a<space><esc>bi<space><esc>
vnoremap <Leader><Leader><space> di<space><space><esc>hp

" 选中到行尾
nnoremap vig vg_

" }}}

" Operator Mapping {{{

onoremap in( :<c-u>normal! f(vi(<cr>
onoremap in[ :<c-u>normal! f[vi[<cr>
onoremap in{ :<c-u>normal! f{vi{<cr>
onoremap in" :<c-u>normal! f"vi"<cr>
onoremap in' :<c-u>normal! f'vi'<cr>

" 选中当前到结尾非空字符
onoremap ig :<c-u>normal! vg_<cr>

" }}}

" Abbreviations {{{

iabbrev eg wxnacy@gmail.com
iabbrev eq 371032668@qq.com
iabbrev hw Hello World

" }}}


" if exists('$TMUX')
  " set term=screen-256color
" endif

autocmd FileType vim setlocal foldmethod=marker
autocmd FileType html set tabstop=2 shiftwidth=2 expandtab ai
autocmd FileType javascript set tabstop=2 shiftwidth=2 expandtab ai
autocmd FileType json set tabstop=4 shiftwidth=4 expandtab ai
"
