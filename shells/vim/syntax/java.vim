setlocal omnifunc=javacomplete#Complete
iabbrev <buffer> class public class{}<esc>i<cr><esc>k$Fsli
iabbrev <buffer> main public static void main(String args[]){}<esc>i<cr>
iabbrev <buffer> classm public class{}
                 \<esc>i<cr>public static void main
                 \(String args[]){}<esc>i<cr>
                 \System.out.println("Hello World");
                 \<esc>kk$Fsli
iabbrev <buffer> print System.out.println()<esc>i""<esc>i
iabbrev <buffer> if if(){}<esc>i<cr><esc>k$hi
iabbrev <buffer> for for(int i = 0; i <; i++){}<esc>i<cr><esc>k$F;i

nnoremap <leader>r :call JavaRun()<cr>

" let g:JavaComplete_SourcesPath = '~/IdeaProjects/HelloWorld/src'
" let g:JavaComplete_LibsPath = '~/IdeaProjects/HelloWorld/src'
" let g:syntastic_java_javac_config_file_enabled = 1
" let g:syntastic_java_javac_config_file = '~/IdeaProjects/HelloWorld/syntastic_config'

function! NewJava()
    " :h expand
    let l:name = expand("%:r")
    call setline(1, "/**")
    call append(1, " * Author: wxnacy(wxnacy@gmail.com)")
    call append(2, " */")
    call append(3, "public class " . l:name . "{")
    call append(4, "    public static void main(String args[]){")
    call append(5, '        System.out.println("Hello world");')
    call append(6, "    }")
    call append(7, "}")
endfunc
" nmap <leader>jI <Plug>(JavaComplete-Imports-AddMissing)
" nmap <leader>jR <Plug>(JavaComplete-Imports-RemoveUnused)
" nmap <leader>ji <Plug>(JavaComplete-Imports-AddSmart)
" nmap <leader>jii <Plug>(JavaComplete-Imports-Add)

" imap <C-j>I <Plug>(JavaComplete-Imports-AddMissing)
" imap <C-j>R <Plug>(JavaComplete-Imports-RemoveUnused)
" imap <C-j>i <Plug>(JavaComplete-Imports-AddSmart)
" imap <C-j>ii <Plug>(JavaComplete-Imports-Add)
