---
title: 二维码生成器
tags:
  - 工具
date: 2018-01-28 19:41:00
---

本章使用 [QRCode.js](https://github.com/davidshimjs/qrcodejs) 来作为生成二维码的工具
<!-- more -->
## 二维码生成器

{% raw %}
<textarea id="plain" style="width: 300px">
https://wxnacy.com
</textarea><br/>
<button onClick="markQRCode()">生成</button>
<button onClick="download()">下载</button>
<div id="qrcode"></div>
<script  type="text/javascript" src="/js/qrcode.min.js"></script>

<script type="text/javascript">
var qrcode = new QRCode(document.getElementById("qrcode"), {
        text: "https://wxnacy.com",
        width: 256,
        height: 256,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
    });
function markQRCode() {
    var plain = document.getElementById("plain").value
    qrcode.makeCode(plain);
}
function download() {
    var can =  document.getElementById("qrcode").getElementsByTagName('img')[0];
    console.log(can, can.src)
    var url = can.src.replace(/^data:image\/[^;]+/, 'data:image/octet-stream');
window.open(url);
    window.navigator.msSaveBlob(can.msToBlob(),'image.jpg');
}

</script>
{% endraw %}
## QRCode.js
基本使用
```javascript
<div id="qrcode"></div>
<script  type="text/javascript" src="qrcode.min.js"></script>
<script type="text/javascript">
new QRCode(document.getElementById("qrcode"), "https://wxnacy.com");
</script>
```
或者
```java
<script type="text/javascript">
    var qrcode = new QRCode(document.getElementById("qrcode"), {
        text: "https://wxnacy.com",
        width: 128,
        height: 128,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
    });
</script>
```
[试一试](/run.html?id=68719480053)
其他方法
```java
qrcode.clear(); // clear the code.
qrcode.makeCode("http://naver.com"); // make another code.
```
