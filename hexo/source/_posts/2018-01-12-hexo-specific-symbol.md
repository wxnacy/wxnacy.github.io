---
title: Hexo 特殊符号的转义问题
date: 2018-01-12 10:19:49
tags: [hexo]
---

在用 Hexo 发布博客的时候经常因为语法遇到各种问题
<!-- more -->
昨天在做 `Jinja2 模板继承` 的文章时，就碰见了问题。
```bash
Template render error: (unknown path) [Line 12, Column 23]
  Error: Unable to call `super`, which is undefined or falsey
  ...
```
```bash
Template render error: (unknown path) [Line 13, Column 52]
  expected variable end
  ...
```
```bash
Template render error: (unknown path) [Line 11, Column 22]
  unexpected token: %}
  ...
```
出现这种问题，我有个很笨的方法就是一点点排除文章中某段文字，因为我知道是某些字符跟hexo 的语法出现了冲突（强烈的不推荐你跟我学），在排查的过程中错误的信息也在不断变化，直到最后一个明明白白的是指明了 `%}` 符号的问题。

Hexo 的语法中也有 **&#123;&#123;&#125;&#125;** 相关的语法，如果你出现了跟它冲突的代码，不是在**代码块**中的，就会被 Hexo 进行编译，这时候你需要使用转义字符来代替

常见的转义如下
```java
! &#33; — 惊叹号 Exclamation mark
” &#34; &quot; 双引号 Quotation mark
# &#35; — 数字标志 Number sign
$ &#36; — 美元标志 Dollar sign
% &#37; — 百分号 Percent sign
& &#38; &amp; Ampersand
‘ &#39; — 单引号 Apostrophe
( &#40; — 小括号左边部分 Left parenthesis
) &#41; — 小括号右边部分 Right parenthesis
* &#42; — 星号 Asterisk
+ &#43; — 加号 Plus sign
< &#60; &lt; 小于号 Less than
= &#61; — 等于符号 Equals sign
- &#45; &minus; — 减号
> &#62; &gt; 大于号 Greater than
? &#63; — 问号 Question mark
@ &#64; — Commercial at
[ &#91; --- 中括号左边部分 Left square bracket
\ &#92; --- 反斜杠 Reverse solidus (backslash)
] &#93; — 中括号右边部分 Right square bracket
{ &#123; — 大括号左边部分 Left curly brace
| &#124; — 竖线Vertical bar
} &#125; — 大括号右边部分 Right curly brace
```

