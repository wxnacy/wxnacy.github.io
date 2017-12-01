
" ruby 工作环境 --------------- {{{
set tabstop=2 shiftwidth=2 expandtab ai
" autocmd BufNewFile *.rb exec ":call NewRbFile()"
function! NewRbFile()
    if &filetype == 'ruby'
        call setline(1, "\#!/usr/bin/env ruby")
        call append(1, "\# -*- coding:utf-8 -*-")
        call append(2, "\# Author: wxnacy(wxnacy@gmail.com)")
        call append(3, "\# Description: ")
    endif

    normal G
    normal o
    normal o
endfunc
" }}}
