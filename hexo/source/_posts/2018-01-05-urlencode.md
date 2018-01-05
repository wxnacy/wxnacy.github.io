---
title: UrlEncode/UrlDecode 编解码
date: 2018-01-05 15:07:08
tags: [工具, javascript]
---

昨天做 Google 搜索时需要对 url 参数进行 URLEncode 编码，发现还没有这个功能，按照惯例，赶紧写一个。
<!-- more -->
<textarea id="plain" style="width: 100%; height: 200px"></textarea>
<button onClick="doUrlencode('encode')">编码</button>
<button onClick="doUrlencode('decode')">解码</button>

js 代码很简单
```javascript
// 编码
var secret = encodeURIComponent('https://wxnacy.com/')
// https%3A%2F%2Fwxnacy.com%2F
var plain = decodeURIComponent('https%3A%2F%2Fwxnacy.com%2F')
// https://wxnacy.com/
```
