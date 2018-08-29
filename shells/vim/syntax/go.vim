iabbrev <buffer> fh package main<cr><cr>import ()<esc>i<cr>
iabbrev <buffer> phw package main<cr><cr>import ()<esc>i<cr>"fmt"<esc>jo<cr>
            \ func main() {}<esc>i<cr>fmt.Println("Hello World")
iabbrev <buffer> main func main() {}<esc>i<cr>
iabbrev <buffer> fori for i := 0; i <; i++ {}<esc>i<cr><esc>k$F;i
iabbrev <buffer> forrm for k, v := range {}<esc>i<cr><esc>k$Fea
iabbrev <buffer> forra for i, d := range {}<esc>i<cr><esc>k$Fea
iabbrev <buffer> fmtp fmt.Println()<esc>i
iabbrev <buffer> fmtf fmt.Printf()<esc>i
iabbrev <buffer> fmts fmt.Sprintf()<esc>i


nnoremap <buffer> <leader>ai gg/import<cr>:nohls<cr>f(%O""<esc>i

onoremap <buffer> gp :<c-u>normal! ggwvg_<cr>
