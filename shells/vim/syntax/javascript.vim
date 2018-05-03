iabbrev <buffer> print console.log("");<esc>hhi
iabbrev <buffer> if if(){}<esc>i<cr><esc>k$hi
iabbrev <buffer> for for(var i = 0; i <; i++){}<esc>i<cr><esc>k$F;i
iabbrev <buffer> fh /**<cr> * Author: wxnacy(wxnacy@gmail.com)<cr>
            \ * Description:<cr> */<cr>

iabbrev <buffer> func function(){};<esc>hi<cr><esc>kf(i
iabbrev <buffer> main if( require.main === module ){}<esc>i<cr>

iabbrev <buffer> debi document.getElementById("");<esc>hhi
iabbrev <buffer> dce document.createElement("");<esc>hhi
iabbrev <buffer> ael addEventListener("");<esc>hhi

"===============================
" vim-javascript 配置
"===============================
" setlocal foldmethod=syntax
" let g:javascript_plugin_jsdoc = 1
" let g:javascript_plugin_ngdoc = 1
" let g:javascript_plugin_flow = 1

" let g:javascript_conceal_function             = "ƒ"
" let g:javascript_conceal_null                 = "ø"
" let g:javascript_conceal_this                 = "@"
" let g:javascript_conceal_return               = "⇚"
" let g:javascript_conceal_undefined            = "¿"
" let g:javascript_conceal_NaN                  = "ℕ"
" let g:javascript_conceal_prototype            = "¶"
" let g:javascript_conceal_static               = "•"
" let g:javascript_conceal_super                = "Ω"
" let g:javascript_conceal_arrow_function       = "⇒"
" let g:javascript_conceal_noarg_arrow_function = "🞅"
" let g:javascript_conceal_underscore_arrow_function = "🞅"
" set conceallevel=1
