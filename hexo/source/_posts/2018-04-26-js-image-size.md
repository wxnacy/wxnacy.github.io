---
title: JavaScript 获取图片尺寸和字节大小
tags:
  - javascript
date: 2018-04-26 17:46:38
---


今天需要使用 JS 获取网络图片的尺寸大小，然后 Google 了一大圈找到的都是获取宽高的，好吧，也可能是我搜索的方式不对，还好凭着我的聪明才智最终自己琢磨出了方法，下面总结下。

<!-- more --><!-- toc -->
## 本地图片

**字节大小**

本地图片是比较简单的，使用 `File Api` 即可

```javascript
<input type="file" id = 'file' multiple/><br/>
<script>
document.getElementById("file").addEventListener("change", selectFile, false);

function selectFile(e) {
  var files = e.target.files;
  console.log(files[i].size);
}
  </script>
```

[试一试](/run/?id=68719485505)

**宽高**

需要使用 `FileReader` 来宽高 `dataurl`，然后使用 `Image` 来获取宽高。

```javascript
<input type="file" id = 'file' multiple/><br/>
<script>
document.getElementById("file").addEventListener("change", selectFile, false);

function selectFile(e) {
  var files = e.target.files;
  var f = files[0];
  var reader = new FileReader();
  reader.onload = (function(theFile) {
    return function(e) {
      var img = new Image();
      img.src = e.target.result;
      img.onload = function(){
        console.log(img.width);
        console.log(img.height);
      };
    };
  })(f);

  reader.readAsDataURL(f);
}
  </script>
```

[试一试](/run/?id=68719485516)

## 网络图片

**字节大小**

通过 `fetch` 请求获取字节大小，在这里获取头信息 `Content-Length` 为空，需要使用 `blob` 数据中的 size。

```java
<span id='output'></span><br/>
<img id="preview" width="300"/>
<script>
  fetch('/images/gzjzz2.png').then(function(res){
    return res.blob()
  }).then(function(data){
    document.getElementById("output").innerHTML =  `${data.size} bytes`

  })
document.getElementById("preview").src = '/images/gzjzz2.png'

</script>
```

[试一试](/run/?id=68719485526)

**宽高**

只需要使用 `Image` 即可
```java
<span id='output'></span><br/>
<img id="preview" width="300"/>
<script>
var img = new Image();
img.src = '/images/gzjzz2.png';
img.onload = function(){
  content = `宽：${img.width} 高：${img.height}`
  document.getElementById("output").innerHTML = content;
};
document.getElementById("preview").src = '/images/gzjzz2.png'

</script>
```

[试一试](/run/?id=68719485524)
