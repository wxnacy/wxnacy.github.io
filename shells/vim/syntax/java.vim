
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
