---
title: Sqlalchemy 快速生成 sql 语句
date: 2020-07-19 00:57:02
tags: [python, sqlalchemy]
---

Sqlalchemy 使用 `select(), insert(), update(), delete()` 方法可以快速生成 Sql 语句并执行。

<!-- more -->
<!-- toc -->

{% raw %}
<iframe id='ipynb' marginheight="0" frameborder="0" width='980px' height='4100px' src="http://notebook.wxnacy.com/modules/sqlalchemy/selectable.html" style="scrolling:no;"></iframe>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"> </script>
<script>
$(function () {
  console.log("ww");

$("#ipynb").load( function() {
    console.log("Hello World");
    console.log(this.contentWindow);
    console.log($(this).contents().find("#notebook").height());
document.getElementById('ipynb').height=$("#ipynb").contents().find("#notebook").height()+100;
})
});
</script>
{% endraw %}

