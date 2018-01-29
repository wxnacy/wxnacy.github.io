---
title: Javascript 如何从下载 src 为 data 数据的 img
tags:
  - javascript
date: 2018-01-29 08:44:52
---


在做[二维码生成器](/2018/01/28/qrcode-marker/)的时候，设计到下载图片的功能
<!-- more -->
在线生成图片的结果是这样的
```html
<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgICAgM...."/>
```
经过搜索，发现 stackoverflow 上的的一篇问答 https://stackoverflow.com/questions/10473932/browser-html-force-download-of-image-from-src-dataimage-jpegbase64 是可行的方法，记录如下

```javascript
var url = img.src.replace(/^data:image\/[^;]+/, 'data:application/octet-stream');
window.open(url);
```
或者
```javascript
var img = document.images[0];
img.onclick = function() {
	// atob to base64_decode the data-URI
	var image_data = atob(img.src.split(',')[1]);
	// Use typed arrays to convert the binary data to a Blob
	var arraybuffer = new ArrayBuffer(image_data.length);
	var view = new Uint8Array(arraybuffer);
	for (var i=0; i<image_data.length; i++) {
		view[i] = image_data.charCodeAt(i) & 0xff;
	}
	try {
		// This is the recommended method:
		var blob = new Blob([arraybuffer], {type: 'application/octet-stream'});
	} catch (e) {
		// The BlobBuilder API has been deprecated in favour of Blob, but older
		// browsers don't know about the Blob constructor
		// IE10 also supports BlobBuilder, but since the `Blob` constructor
		//  also works, there's no need to add `MSBlobBuilder`.
		var bb = new (window.WebKitBlobBuilder || window.MozBlobBuilder);
		bb.append(arraybuffer);
		var blob = bb.getBlob('application/octet-stream'); // <-- Here's the Blob
	}

	// Use the URL object to create a temporary URL
	var url = (window.webkitURL || window.URL).createObjectURL(blob);
	location.href = url; // <-- Download!
};
```
