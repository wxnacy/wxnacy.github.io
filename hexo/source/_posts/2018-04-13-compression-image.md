---
title: 压缩图片
tags:
  - 工具
  - javascript
date: 2018-04-13 21:42:27
---


今天工作需要用到压缩图片，但是一时间竟然找不到方便的工具来做这件事。你们知道我的，我一定要写个工具干这事。

<!-- more --><!-- toc -->


{% raw %}
网络图片：<input id="url" value="/images/gzjzz2.png"/>
<br/>
压缩系数：<input type="text" id="quality" value="0.7">
<br/>
<button id="comp" onClick="compression()">压缩</button>
<button id="download" onClick="download()">下载</button>
<br/>
<span id='fs'></span>
<br/>
<img id="preview" width="200"/>
<script type="text/javascript" src="/js/lrz.bundle.js"></script>
<script>
//定义一个立即执行的函数
compression()
function compression(){
    var url = document.getElementById('url').value;
    var q = document.getElementById('quality').value;
    q = parseFloat(q)
    console.log(q);
    console.log(url);
    lrz(url, {quality:q})
        .then(function (rst) {
                // 处理成功会执行
                var imgDoc = document.getElementById('preview');
                imgDoc.src = rst.base64
                var fs = rst.fileLen / Math.pow(1024, 1)
                fs = Math.floor(fs)
                document.getElementById('fs').innerHTML = '压缩后大约：' + fs + 'KB'

                })
    .catch(function (err){
            // 处理失败会执行
            console.log(res);
            })
    .always(function () {
            // 不管是成功失败，都会执行
            });
}
function download(){
    var imgDoc = document.getElementById('preview');
    var url = imgDoc.src.replace(/^data:image\/[^;]+/, 'data:image/octet-stream');
    window.open(url);
}
</script>
{% endraw %}
