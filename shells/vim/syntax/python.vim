" if exists("b:current_syntax")
    " finish
" endif
" if exists('syntax_on')
  " syntax reset
" endif

function! s:Enabled(name)
  return exists(a:name) && {a:name}
endfunction
syntax match   pythonRun		"\%^#!.*$"
syntax match   pythonCoding	"\%^.*\%(\n.*\)\?#.*coding[:=]\s*[0-9A-Za-z-_.]\+.*$"
syntax keyword potionKeyword class self def cls
" syntax keyword potionKeyword from import
syntax keyword potionKeyword __name__ __file__
syntax keyword potionFunction print join string
syntax keyword pythonMagic __abs__ __add__ __aenter__ __aexit__ __aiter__ __and__ __anext__
  \ __await__ __bytes__ __call__ __complex__ __contains__ __del__ __delattr__ __delete__
  \ __delitem__ __dir__ __divmod__ __enter__ __eq__ __exit__ __float__ __floordiv__
  \ __format__ __ge__ __get__ __getattr__ __getattribute__ __getitem__ __gt__ __hash__
  \ __iadd__ __iand__ __ifloordiv__ __ilshift__ __imod__ __imul__ __index__ __init__
  \ __int__ __invert__ __ior__ __ipow__ __irshift__ __isub__ __iter__ __itruediv__ __ixor__
  \ __le__ __len__ __lshift__ __lt__ __mod__ __mul__ __ne__ __neg__ __new__ __next__ __or__
  \ __pos__ __pow__ __radd__ __rand__ __rdivmod__ __repr__ __reversed__ __rfloordiv__
  \ __rlshift__ __rmod__ __rmul__ __ror__ __rpow__ __rrshift__ __rshift__ __rsub__
  \ __rtruediv__ __rxor__ __set__ __setattr__ __setitem__ __str__ __sub__ __truediv__ __xor__
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

highlight! link pythonCoding  Comment
highlight! link pythonRun     Special
highlight! link potionKeyword Keyword
highlight! link pythonMagic Keyword
highlight! link potionFunction Function
highlight! pythonMagic    guibg=NONE guifg=#8e44ad gui=NONE
" highlight! link potionComment Comment
" highlight! link potionOperator Operator



" Python 工作环境 ------------- {{{
set tabstop=4 shiftwidth=4 textwidth=79 expandtab ai
nnoremap <buffer> <Leader>F :call FormatPy()<cr>
inoremap <buffer> <Leader>/ """"""<esc>hhi
setlocal foldmethod=indent
setlocal foldignore=

iabbrev <buffer> main if __name__ == "__main__":<cr>
iabbrev <buffer> init def __init__(self, *args, **kwargs):<cr>
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
" let b:current_syntax = "python"
