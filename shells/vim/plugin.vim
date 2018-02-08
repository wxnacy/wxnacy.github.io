"===============================
" vim-colors-solarized 配置
"===============================
colorscheme solarized

"===============================
" YouCompleterMe 配置
"===============================
"let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/cpp/ycm/.ycm_extra_conf.py'
"let g:ycm_error_symbol = '>>'
"let g:ycm_warning_symbol = '>*'
"l打开vim时不再询问是否加载ycm_extra_conf.py配置"
"let g:ycm_confirm_extra_conf=0
"let completeopt=longest,menu
"lpython解释器路径"
"let g:ycm_path_to_python_interpreter='/Users/wxnacy/.pyenv/shims/python'
"l是否开启语义补全"
"let g:ycm_seed_identifiers_with_syntax=1
"l是否在注释中也开启补全"
"let g:ycm_complete_in_comments=1
"let g:ycm_collect_identifiers_from_comments_and_strings = 0
"l开始补全的字符数"
"let g:ycm_min_num_of_chars_for_completion=2
"l补全后自动关机预览窗口"
"let g:ycm_autoclose_preview_window_after_completion=1
"l 禁止缓存匹配项,每次都重新生成匹配项"
"let g:ycm_cache_omnifunc=0
"l字符串中也开启补全"
"let g:ycm_complete_in_strings=1
"l离开插入模式后自动关闭预览窗口"
"lutocmd InsertLeave * if pumvisible() == 0|pclose|endif
"l回车即选中当前项"
" inoremap <expr> <CR>       pumvisible() ? '<C-y>' : '<CR>'
"上下左右键行为"
"inoremap <expr> <Down>     pumvisible() ? '\<C-n>' : '\<Down>'
"inoremap <expr> <Up>       pumvisible() ? '\<C-p>' : '\<Up>'
"inoremap <expr> <PageDown> pumvisible() ? '\<PageDown>\<C-p>\<C-n>' : '\<PageDown>'
"inoremap <expr> <PageUp>   pumvisible() ? '\<PageUp>\<C-p>\<C-n>' : '\<PageUp>'
nnoremap <leader>gl :YcmCompleter GoToDeclaration<CR>
nnoremap <leader>gf :YcmCompleter GoToDefinition<CR>
nnoremap <leader>gg :YcmCompleter GoToDefinitionElseDeclaration<CR>
nmap <F4> :YcmDiags<CR>

"===============================
" quickrun 配置
"===============================
let g:quickrun_config = {
\   "_" : {
\       "outputter" : "loclist",
\   },
\}
let g:quickrun_no_default_key_mappings = 1
nmap <Leader>r <Plug>(quickrun)
map <F10> :QuickRun<CR>

"===============================
" airline 配置
"===============================
if !exists('g:airline_symbols')
let g:airline_symbols = {}
endif
let g:airline_left_sep       = '▶'
let g:airline_left_alt_sep   = '❯'
let g:airline_right_sep      = '◀'
let g:airline_right_alt_sep  = '❮'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'

" 是否打开tabline
let g:airline#extensions#tabline#enabled = 1


"===============================
" EasyAlign 配置
"===============================
vmap <Leader>a <Plug>(EasyAlign)
nmap <Leader>a <Plug>(EasyAlign)
if !exists('g:easy_align_delimiters')
  let g:easy_align_delimiters = {}
endif
let g:easy_align_delimiters['#'] = { 'pattern': '#', 'ignore_groups': ['String'] }

"===============================
" NERDTree 配置
"===============================
autocmd vimenter * NERDTree     " 启动vim默认打开菜单
map tt :NERDTreeToggle<CR>       " 快速打开隐藏菜单栏
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif           " 关闭vim时，如果打开的文件除了NERDTree没有其他文件时，它自动关闭，减少多次按:q!。
let NERDTreeShowLineNumbers=1   " 是否显示菜单行号
" let NERDTreeAutoCenter=1
let NERDTreeShowHidden=1        " 是否显示隐藏文件
" let NERDTreeWinSize=31          " 设置宽度
let NERDTreeIgnore=['\.pyc','\~$','\.swp','\.git$','\.DS_Store','__pycache__','\.idea','\.cache','.python-version']  " 忽略文件显示
let NERDTreeShowBookmarks=1     " 显示书签列表
let NERDTreeHighlightCursorline = 1 " 高亮当前行
" let NERDTreeQuitOnOpen = 1      " 从菜单打开文件后关闭菜单
let NERDTreeWinPos ="left"      " 设置菜单在左侧打开，默认值

"===============================
" NERDTree-git-plugin 配置
"===============================
let g:nerdtree_tabs_open_on_console_startup=1


"===============================
" NERDTree-git-plugin 配置
"===============================
let g:NERDTreeIndicatorMapCustom = {
    \ "Modified"  : "✹",
    \ "Staged"    : "✚",
    \ "Untracked" : "✭",
    \ "Renamed"   : "➜",
    \ "Unmerged"  : "═",
    \ "Deleted"   : "✖",
    \ "Dirty"     : "✗",
    \ "Clean"     : "✔︎",
    \ 'Ignored'   : '☒',
    \ "Unknown"   : "?"
    \ }
let g:NERDTreeShowIgnoredStatus = 1


"===============================
" gundo 配置
"===============================
nnoremap <leader>H :GundoToggle<CR>


"===============================
" whitespace 配置
"===============================
map <leader><space> :FixWhitespace<cr>


"===============================
" tagbar 配置
"===============================
nmap tb :TagbarToggle<CR>
" 启动时自动focus
let g:tagbar_autofocus = 1
let g:tagbar_width=30           " 设置宽度
" for md
let g:tagbar_type_markdown = {
    \ 'ctagstype' : 'markdown',
    \ 'kinds' : [
        \ 'h:Heading_L1',
        \ 'i:Heading_L2',
        \ 'k:Heading_L3'
    \ ]
\ }
"et g:tagbar_type_markdown = {
"   \ 'ctagstype': 'markdown',
"   \ 'ctagsbin' : '~/.vim/bundle/markdown2ctags/markdown2ctags.py',
"   \ 'ctagsargs' : '-f - --sort=yes',
"   \ 'kinds' : [
"       \ 's:sections',
"       \ 'i:images'
"   \ ],
"   \ 'sro' : '|',
"   \ 'kind2scope' : {
"       \ 's' : 'section',
"   \ },
"   \ 'sort': 0,
" }
" for ruby, delete if you do not need
let g:tagbar_type_ruby = {
    \ 'kinds' : [
        \ 'm:modules',
        \ 'c:classes',
        \ 'd:describes',
        \ 'C:contexts',
        \ 'f:methods',
        \ 'F:singleton methods'
    \ ]
\ }

"===============================
" nerdcommenter 配置
"===============================
let g:NERDSpaceDelims = 1       " 注释后添加空格
" let g:NERDCompactSexyComs = 1

"===============================
" closetag 配置
"===============================
let g:closetag_html_style=1

"===============================
" emment-vim 配置
"===============================
let g:user_emmet_leader_key='<C-Z>'     " 设置快捷键

"===============================
" syntastic 配置
"===============================
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_error_symbol='>>'
let g:syntastic_warning_symbol='>'
let g:syntastic_check_on_open=0
let g:syntastic_check_on_wq=1
let g:syntastic_enable_highlighting=1
let g:syntastic_aggregate_errors = 1
let g:syntastic_stl_format = '[%E{E:%fe #%e}%B{, }%W{W:%fw #%w}]'
let g:syntastic_python_checkers=['pyflakes'] " 使用pyflakes,速度比pylint快
let g:syntastic_javascript_checkers = ['jsl', 'jshint']
let g:syntastic_html_checkers=['tidy', 'jshint']
" let g:syntastic_java_javac_classpath = '~/IdeaProjects/HelloWorld/src'
" " 修改高亮的背景色, 适应主题
highlight SyntasticErrorSign guifg=white guibg=black

" " to see error location list
let g:syntastic_always_populate_loc_list = 0
let g:syntastic_auto_loc_list = 0
let g:syntastic_loc_list_height = 5
function! ToggleErrors()
    let old_last_winnr = winnr('$')
    lclose
    if old_last_winnr == winnr('$')
        " Nothing was closed, open syntastic error location panel
        Errors
    endif
endfunction
nnoremap <Leader>e :call ToggleErrors()<cr>
nnoremap <Leader>ec :SyntasticCheck<cr>
nnoremap <Leader>en :lnext<cr>
nnoremap <Leader>ep :lprevious<cr>

"===============================
" easymotion 配置
"===============================
let g:EasyMotion_smartcase = 1
"let g:EasyMotion_startofline = 0 " keep cursor colum when JK motion
map <Leader><Leader>h <Plug>(easymotion-linebackward)
map <Leader><Leader>j <Plug>(easymotion-j)
map <Leader><Leader>k <Plug>(easymotion-k)
map <Leader><Leader>l <Plug>(easymotion-lineforward)
" 重复上一次操作, 类似repeat插件, 很强大
map <Leader><Leader>. <Plug>(easymotion-repeat)


"===============================
" ale 配置
"===============================
" let g:ale_completion_enabled = 1
" let g:ale_fix_on_save = 1
" let g:ale_sign_column_always = 1            " 保持侧边栏可见"
" let g:ale_sign_error = '>>'                 " 改变错误和警告表示服"
" let g:ale_sign_warning = '--'
" let g:ale_statusline_format = ['⨉ %d', '⚠ %d', '⬥ ok']  " 改变状态栏信息格式"
" let g:ale_echo_msg_error_str = 'E'
" let g:ale_echo_msg_warning_str = 'W'
" let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'
" let g:ale_linters = {
              " \ 'sh' : ['shellcheck'],
              " \ 'vim' : ['vint'],
              " \ 'html' : ['tidy'],
              " \ 'python' : ['flake8'],
              " \ 'markdown' : ['mdl'],
              " \ 'javascript' : ['eslint'],
              " \}
" augroup YourGroup
    " autocmd!
    " autocmd User ALELint call YourFunction()
" augroup END

" nmap <Leader>en <Plug>(ale_next)
" nmap <Leader>ep <Plug>(ale_previous)
" nnoremap <Leader>e :ALEToggle<CR>

"===============================
" deoplete 配置
"===============================
" let g:deoplete#enable_at_startup = 1        " 启动"

"===============================
" ctrlp 配置
"===============================
let g:ctrlp_map = '<leader>p'
let g:ctrlp_cmd = 'CtrlP'
map <leader>p :CtrlP<CR>
map <leader>f :CtrlPMRU<CR>
let g:ctrlp_custom_ignore = {
    \ 'dir':  '\v[\/]\.(git|hg|svn|rvm)$',
    \ 'file': '\v\.(exe|so|dll|zip|tar|tar.gz|pyc)$',
    \ }
let g:ctrlp_working_path_mode=0
let g:ctrlp_match_window_bottom=1
let g:ctrlp_max_height=15
let g:ctrlp_match_window_reversed=0
let g:ctrlp_mruf_max=500
let g:ctrlp_follow_symlinks=1

"===============================
" ctrlp-funky 配置
"===============================
nnoremap <Leader>fu :CtrlPFunky<Cr>
" narrow the list down with a word under cursor
nnoremap <Leader>fU :execute 'CtrlPFunky ' . expand('<cword>')<Cr>
let g:ctrlp_funky_syntax_highlight = 1

let g:ctrlp_extensions = ['funky']

"===============================
" vim-multiple-cursors 配置
"===============================
let g:multi_cursor_use_default_mapping=0
" Default mapping
let g:multi_cursor_next_key='<C-n>'
let g:multi_cursor_prev_key='<C-p>'
let g:multi_cursor_skip_key='<C-x>'
let g:multi_cursor_quit_key='<Esc>'
" let g:multi_cursor_start_word_key='g<C-n>'
highlight multiple_cursors_cursor term=reverse cterm=reverse gui=reverse
highlight link multiple_cursors_visual Visual

"===============================
" python-mode 配置
"===============================
" let g:pymode_python = 'python3'

"===============================
" ack 配置
"===============================
" let g:ackprg = 'ag --nogroup --nocolor --column'
nmap <Leader><Leader>a :Ack<space>-i<space>

"===============================
" Ctrlsf 配置
"===============================
nmap <Leader><Leader>c :CtrlSF<space>

"===============================
" vim-jsx 配置
"===============================
let g:jsx_ext_required = 0
let g:jsx_pragma_required = 1
