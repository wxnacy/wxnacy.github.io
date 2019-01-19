---
title: Vim 基础命令
date: 2017-08-23
tags: [vim]
---

[专辑：Vim 练级手册](/vim)

开始之前我们先来谈谈为什么用 Vim， 网上有很多探讨 Vim 哲学的文章，在我看来 Vim 是这样的一款编辑器。它可以很简单，简单到除了你正在编辑的文字，其余什么都没有。它也可以很复杂，复杂到可以囊括所有 IDE 可以有的功能。它可以很简单，简单到只需要几个输入几个字符，就可以完成其他 IDE 几分钟的工作量。它也可以很复杂，复杂到你连退出就不会。它是一个很神奇的编辑器，它可以无所不能，也可以化繁为简。它可以变成任何你想要的样子，问题只有一个，你是不是准备好开始接受它了。上车吧，我们要出发了

<!-- more -->

<!-- toc -->
## 几种模式

### normal
以 vim 打开一个文档，默认进入的就是 normal 模式，在该模式下，我们可以 `上下左右` 移动光标，可以 `删除，黏贴，复制` 文本。

### visual
在 normal 模式下，我们可以进行的复制删除等操作仅限于打个字符或正行，如果想要对某个区域进行操作，需要通过输入 `V, v, <c-v>` 来进入 visual 模式

### insert
想要插入数据，可以通过按下 `i, I, a, A, o, O, s, S` 可以进入insert 模式，通过按下 `<es>` 退出键回到 normal 模式

### replace
replace 模式，需要在 normal 模式下按下 `r, R` 键来进入，与 insert 不同的是，该模式只能对现有文本进行替换，同样需要按下 `<esc>` 回到 normal 模式

### command
在 normal 下通过输入 `:, /, ?` 来进入 command 模式，在该模式下光标会移动到最下边一行，同时可以完成 `搜索、读取，存档，替换，离开 Vim、配置 Vim` 等操作

## 基本操作
介绍完几种模式，这部分我们来探讨下各个模式下的基本操作

### 移动光标
这部分是在 normal 模式下完成的，我通过单个或组合按键来完成光标的移动，最简单的是 `h, j, k, l` 他们分别代表了小键盘区的 `← ↓ ↑ →` 来进行左下上右的移动操作，接下来是翻页，这涉及到一个组合键 `<c-f>` ，它代表的是 `ctrl + f` 的缩写，以后这类组合键我们都会这样写
```vim
<c-f>   " 向下移动一页
<c-d>   " 向下移动半页
<c-b>   " 向上移动一页
<c-u>   " 向上移动半页
```
接下来要说到的是针对行的光标操作
```vim
n<space> / nl	    " n 表示数字，后边跟上空格或者 l ，就可以向右移动相应格数
nh                  " 跟上边一样，是向左移动
0                   " 0 可以移动到行首
$                   " 移动到行尾
g_                  " 移动到行尾最后一个非空字符

n<Enter> / nj	    " n 表示数字，向下移动相应行数
nk                  " 跟上边一样，是向上移动
nG                  " 移动到指定的行数
gg                  " 动到文档第一行，相当于1G
G                   " 移动到文档最后一行

```
还有一些不常用的行操作，不记也没关系
```vim
H	                " 移动到当前屏幕第一行的第一个字符
M	                " 移动到当前屏幕中间行的第一个字符
L	                " 移动到当前屏幕最后一行的第一个字符
+	                " 移动到非空白字符的下一行
-	                " 移动到非空白字符的上一行
```

### 查找与替换

```bash
/word   " 输入 / 会进入 command 模式，再输入先要搜索的单词并回车进行搜索
?word   " / 是向光标以后搜索，? 是向前搜索
n       " 英文字母 n，根据 / 或 ? 搜索的方向定位到下一个匹配目标
N       " 与 n 相反，定位匹配目标


:n1,n2s/word1/word2/g   " n1, n2 表示数字，替换 n1 行到 n2 行的单词
:1,$s/word1/word2/g     " 全文替换，也可以写成 :%s/word1/word2/g
:1,$s/word1/word2/gc    " 全文替换，并出现确认提示
```

### 删除、复制和黏贴

```bash
x, X        " 删除字符，x 向后删除一个字符，X 向前删除一个字符
nx, nX      " 向后或向前删除 n 个字符
dd          " 删除当前行
ndd         " 向下删除 n 行
d1G / dgg   " 删除第一行到当前行的数据
dG          " 删除当前行到最后一行的数据
d$          " 删除当前字符到行尾
d0          " 从行首删除到当前字符

yy          " 复制当前行
nyy         " 从当前行开始复制 n 行
y1G / ygg   " 从第一行复制到当前行
yG          " 从当前行复制到最后一行
y0          " 从行首复制到当前字符
y$          " 从当前字符复制到行尾

p, P        " 黏贴，p 黏贴到光标下一行，P 黏贴到光标上一行

J           " 将下一行合并到当前行，在 visual 模式下是合并选中行
ncj / nck   " 向下或向上删除 n 行，并进入 insert 模式
u           " 撤销
<c-r>       " 重做

.           " 你没看错，就是个小数点，重复上一次的动作，可以在删除黏贴等后边用
```

第二部份：一般指令模式切換到編輯模式的可用的按鈕說明

### 进入插入或替换的编辑模式

```bash
i       在光标所在处插入
I       在该行第一个非空字符处插
a       在光标后一个字符插入
A       在该行最后一个字符后插入
o, O	進入插入模式(Insert mode)：
o       在光标的下一行插入
O       在光标的上一行插入
s       " 删除当前字符，并进入 insert 模式"
S       " 删除当前行，并进入插入模式


cw      删除光标后第一个单词，并进入插入模式
cc      " 删除当前行，并进入插入模式

r, R	進入取代模式(Replace mode)：
r       只會取代游標所在的那一個字元一次；R會一直取代游標所在的文字，直到按下 ESC 為止；(常用)
<C-a>   光标放在数字上，按下该组合键可以让数字加一

# 上面這些按鍵中，在 vi 畫面的左下角處會出現『--INSERT--』或『--REPLACE--』的字樣。 由名稱就知道該動作了吧！！特別注意的是，我們上面也提過了，你想要在檔案裡面輸入字元時， 一定要在左下角處看到 INSERT 或 REPLACE 才能輸入喔！


[Esc]	退出編輯模式，回到一般指令模式中(常用)
```

第三部份：一般指令模式切換到指令列模式的可用按钮说明

### 指令列模式的保存、离开等指令

```bash
:w	                將編輯的資料寫入硬碟檔案中(常用)
:w!	                若檔案屬性為『唯讀』時，強制寫入該檔案。不過，到底能不能寫入， 還是跟你對該檔案的檔案權限有關啊！
:q	                離開 vi (常用)
:q!	                若曾修改過檔案，又不想儲存，使用 ! 為強制離開不儲存檔案。

# 注意一下啊，那個驚嘆號 (!) 在 vi 當中，常常具有『強制』的意思～

:wq	                儲存後離開           ，若為 :wq! 則為強制儲存後離開 (常用)
ZZ	                這是大寫的 Z 喔！若檔案沒有更動，則不儲存離開，若檔案已經被更動過，則儲存後離開！
:w [filename]	    將編輯的資料儲存成另一個檔案（類似另存新檔）
:r [filename]	    在編輯的資料中，讀入另一個檔案的資料。亦即將 『filename』 這個檔案內容加到游標所在列後面
:n1,n2 w [filename]	將 n1 到 n2 的內容儲存成 filename 這個檔案。
:! command	        暫時離開 vi 到指令列模式下執行 command 的顯示結果！例如『:! ls /home』即可在 vi 當中察看 /home 底下以 ls 輸出的檔案資訊！
```

### vim 环境的变更

```bash
:set nu	    顯示行號，設定之後，會在每一列的字首顯示該列的行號
:set nonu	與 set nu 相反，為取消行號！
```
## 额外功能
### vim 的保存文件、恢复与打开时的警告信息
當我們在使用 vim 編輯時， vim 會在與被編輯的檔案的目錄下，再建立一個名為 .filename.swp 的檔案。 比如說我們在上一個小節談到的編輯 /tmp/vitest/man_db.conf 這個檔案時， vim 會主動的建立 /tmp/vitest/.man_db.conf.swp 的暫存檔，你對 man_db.conf 做的動作就會被記錄到這個 .man_db.conf.swp 當中喔！如果你的系統因為某些原因斷線了， 導致你編輯的檔案還沒有儲存，這個時候 .man_db.conf.swp 就能夠發揮救援的功能了！我們來測試一下吧！ 底下的練習有些部分的指令我們尚未談到，沒關係，你先照著做，後續再回來瞭解囉！
```bash
$ cd /tmp/vitest
$ vim man_db.conf
# 此時會進入到 vim 的畫面，請在 vim 的一般指令模式下按下『 [ctrl]-z 』的組合鍵

[1]+  Stopped             vim man_db.conf  <==按下 [ctrl]-z 會告訴你這個訊息
```
當我們在 vim 的一般指令模式下按下 [ctrl]-z 的組合按鍵時，你的 vim 會被丟到背景去執行。回到命令提示字元後，接下來我們來模擬將 vim 的工作不正常的中斷吧！
```bash
$ ls -al
drwxrwxr-x.  2 dmtsai dmtsai    69 Jul  6 23:54 .
drwxrwxrwt. 17 root   root    4096 Jul  6 23:53 ..
-rw-r--r--.  1 dmtsai dmtsai  4850 Jul  6 23:47 man_db.conf
-rw-r--r--.  1 dmtsai dmtsai 16384 Jul  6 23:54 .man_db.conf.swp  <==就是他，暫存檔
-rw-rw-r--.  1 dmtsai dmtsai  5442 Jul  6 23:35 man.test.config

$ kill -9 %1 <==這裡模擬斷線停止 vim 工作
$ ls -al .man_db.conf.swp
-rw-r--r--. 1 dmtsai dmtsai 16384 Jul  6 23:54 .man_db.conf.swp  <==暫存檔還是會存在！

$ vim man_db.conf

E325: ATTENTION  <==錯誤代碼
Found a swap file by the name ".man_db.conf.swp"  <==底下數列說明有暫存檔的存在
          owned by: dmtsai   dated: Mon Jul  6 23:54:16 2015
         file name: /tmp/vitest/man_db.conf  <==這個暫存檔屬於哪個實際的檔案？
          modified: no
         user name: dmtsai   host name: study.centos.vbird
        process ID: 31851
While opening file "man_db.conf"
             dated: Mon Jul  6 23:47:21 2015

底下說明可能發生這個錯誤的兩個主要原因與解決方案！
(1) Another program may be editing the same file.  If this is the case,
    be careful not to end up with two different instances of the same
    file when making changes.  Quit, or continue with caution.
(2) An edit session for this file crashed.
    If this is the case, use ":recover" or "vim -r man_db.conf"
    to recover the changes (see ":help recovery").
    If you did this already, delete the swap file ".man_db.conf.swp"
    to avoid this message.

Swap file ".man_db.conf.swp" already exists! 底下說明你可進行的動作
[O]pen Read-Only, (E)dit anyway, (R)ecover, (D)elete it, (Q)uit, (A)bort:
```
再次打开文件时，会出现六个按钮，他们的作用依次是：

```bash
[O]pen Read-Only：打開此檔案成為唯讀檔， 可以用在你只是想要查閱該檔案內容並不想要進行編輯行為時。一般來說，在上課時，如果你是登入到同學的電腦去看他的設定檔， 結果發現其實同學他自己也在編輯時，可以使用這個模式；

(E)dit anyway：還是用正常的方式打開你要編輯的那個檔案， 並不會載入暫存檔的內容。不過很容易出現兩個使用者互相改變對方的檔案等問題！不好不好！

(R)ecover：就是載入暫存檔的內容，用在你要救回之前未儲存的工作。 不過當你救回來並且儲存離開 vim 後，還是要手動自行刪除那個暫存檔喔！

(D)elete it：你確定那個暫存檔是無用的！那麼開啟檔案前會先將這個暫存檔刪除！ 這個動作其實是比較常做的！因為你可能不確定這個暫存檔是怎麼來的，所以就刪除掉他吧！哈哈！

(Q)uit：按下 q 就離開 vim ，不會進行任何動作回到命令提示字元。

(A)bort：忽略這個編輯行為，感覺上與 quit 非常類似！ 也會送你回到命令提示字元就是囉！
```

### 多文件编辑

很多同学任务高集成的IDE比vim好用，是因为vim不能操作一些事情，比如跨文件复制，但其实vim完全可以做到，首先下载文件：http://linux.vbird.org/linux_basic/0310vi/hosts 打开后如下所示:
```bash
192.168.1.1    host1.class.net
192.168.1.2    host2.class.net
192.168.1.3    host3.class.net
192.168.1.4    host4.class.net
.....中間省略......
```

我们再建一个新文件host2,并进行跨文件复制操作
```bash
$ touch host_copy
$ vim hosts host_copy # 使用vim同时打开两个文件
```
下面我们会使用这几个命令
```bash
:n	    編輯下一個檔案
:N	    編輯上一個檔案
:files	列出目前這個 vim 的開啟的所有檔案
```

```bash
:files      # 再打开文件后一般模式下使用改名了查看有几个文件

:files
  1 %a   "hosts"                        line 1      # %a代表当前编辑的文件
  2      "host2"                        line 0

# 使用gg切换到第一行，使用4yy复制前四行
:n          # 指令该命令编辑下一个文件

# 使用p将刚才复制的内容粘贴到该文件中使用:q退出编辑并查看host2会发现刚才的内容已经复制过来了
```






```bash
v	        字元選擇，會將游標經過的地方反白選擇！
V	        列選擇，會將游標經過的列反白選擇！
[Ctrl]+v    區塊選擇，可以用長方形的方式選擇資料
y	        將反白的地方複製起來
d	        將反白的地方刪除掉
p	        將剛剛複製的區塊，在游標所在處貼上！
```

## 快替换
```bash
[Ctrl] + v 选中块
c  输入替换文字
<Esc> 完成替换
```

## 多窗口
```bash
:sp [filename]  # 垂直分割屏幕，filename 是想要打开的文件，默认当前文档
:vsp [filename] # 水平分割屏幕
[ctrl]+w+↓/j    # 按键的按法是：先按下 [ctrl] 不放， 再按下 w 后放开所有的按键，然后再按下 j (或向下箭头键)，则光标可移动到下方的窗口。
[ctrl]+w+↑/k    # 同上，不过光标移动到上面的窗口。
[ctrl]+w+q      # 其实就是 :q 结束离开啦！ 举例来说，如果我想要结束下方的窗口，那么利用 [ctrl]+w+↓ 移动到下方窗口后，按下 :q 即可离开， 也可以按下 [ctrl]+w+q 啊！

ctrl_w + r: 窗口本身, 不是鼠标指针顺时针 (向下, 向右 移动), R : 则是逆时针反方向(向上, 向左)移动.
ctrl_w+x: 左右上下对应位置的窗口 对调. 要注意窗口必须是 对应的, 如果不对应将无法对换, 比如左边一个大窗口, 右边有两个小的 子窗口, 则左右不能互换.
```


```bash
# set compatible 就是让 vim 关闭所有扩展的功能，尽量模拟 vi 的行为。
但这样就不应用 vim 的很多强大功能，所以一般没有什么特殊需要的话（比如执行很老的 vi 脚本），都要在 vim 的配置开始，写上 set nocompatible，关闭兼容模式。由于这个选项是最最基础的选项，会连带很多其它选项发生变动（称作副作用），所以它必需是第一个设定的选项。
set nocompatible
```

## Operator-Pending映射
```bash
vip         # vip很好记
viw         # 快速选中当前单词
vi(         # 选择括号内的文字
vt,         # 选择到下一个逗号
```

## 宏
vim有个非常厉害的功能叫**宏**，它可以将你的操作进行宏录制，放到vim寄存器中，并按照你想要的方式播放出来

### 操作

- 首先准备一个文件，第一行为数字1
- 光标放在1上并按下 qa（当然也可以 qb，qc，这只是录制宏的名字）开始录制，测试左下角会显示录制字样
- 输入 yyp 复制当前行到下一行，并输入 <C-a> 将数字增加1，此时第二行数字为2
- 按下 q 结束录制，并按下 @a 播放宏，此时第三行会变成3，按下 @@ 重复上次播放，第四行会变成4
- 当按下 100@@ 时，宏会重复播放100次上次的播放记录，自动生成104行数据

## 与系统剪切版交互
加上 `"+` 即可
```bash
"+yy
"+Y
v"+y
```

## 其他操作
```bash
:inoremap <esc> <nop>   # 使<esc>失效
g_  # 移动到当前行（译注：等号组成的行）的最后一个非空字符。
```

## 参考文献

- [vim 程式编辑器](http://cn.linux.vbird.org/linux_basic/0310vi.php)
