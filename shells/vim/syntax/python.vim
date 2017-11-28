" if exists("b:current_syntax")
    " finish
" endif

syntax keyword potionKeyword class self def cls
syntax keyword potionKeyword from import
syntax keyword potionKeyword __name__
syntax keyword potionFunction print join string
" syntax match potionComment "\v#.*$"
" syn keyword potionKeyword contained TODO FIXME NOTE
" syn match potionComment "\v#.*$" contains=potionKeyword
" syntax match potionOperator "\v\*"
" syntax match potionOperator "\v/"
" syntax match potionOperator "\v\+"
" syntax match potionOperator "\v-"
" syntax match potionOperator "\v\?"
" syntax match potionOperator "\v\*\="
" syntax match potionOperator "\v/\="
" syntax match potionOperator "\v\+\="
" syntax match potionOperator "\v-\="

highlight! link potionKeyword Keyword
highlight! link potionFunction Function
" highlight! link potionComment Comment
" highlight! link potionOperator Operator


" let b:current_syntax = "potion"

" Python 工作环境 ------------- {{{
set tabstop=4 shiftwidth=4 textwidth=79 expandtab ai
nnoremap <buffer> <Leader>F :call FormatPy()<cr>
inoremap <buffer> <Leader>/ """"""<esc>hhi
setlocal foldmethod=indent
setlocal foldignore=

iabbrev <buffer> main if __name__ == "__main__":<cr>
iabbrev <buffer> fh #!/usr/bin/env python<cr>
                    \# -*- coding:utf-8 -*-<cr>
                    \# Author: wxnacy
                    \(wxnacy@gmail.com)<cr>
                    \# Description:<cr>
                    \<cr>
autocmd BufNewFile *.py exec ":call NewPyFile()"
function! NewPyFile()
    if &filetype == 'python'
        call setline(1, "\#!/usr/bin/env python")
        call append(1, "\# -*- coding:utf-8 -*-")
        call append(2, "\# Author: wxnacy(wxnacy@gmail.com)")
        call append(3, "\# Description: ")
    endif

    normal G
    normal o
    normal o
endfunc

function! FormatPy()
    normal 079lF)
    let b:nc = col('.')
    if b:nc < 80
        exec "normal! i\<cr>\<esc>"
    elseif b:nc == 80
        if @@ ==# ')'
            exec "normal! i\<cr>\<esc>"
        else
            normal! F,
            exec "normal! a\<cr>\<esc>"
        endif
    endif
endfunc
" nnoremap  <Leader>F :call FormatPy()<esc>
" }}}
