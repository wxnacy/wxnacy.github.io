---
title: 利用 Google 搜索你的网站
date: 2018-01-04 17:47:51
tags: [工具, javascript]
---

Google 大法好啊
<!-- more -->
个人建站动不动就自己写搜索引擎的时代已经一去不复返了，现在各种搜索服务应接不暇，收费的免费的，一抓一大把，而如果巧用 Google 的搜索功能，你连 API 都不用接入，就可以做搜索。

把 `site:https://wxnacy.com python` 复制到 Google 搜索框，或者直接点击下面的连接

https://www.google.co.jp/search?q=site:https://wxnacy.com+python&gws_rd=cr&dcr=0&ei=nf1NWqbiFISx0ATokYaQBA

你会发现在 Google 中搜索出来的内容，全都是我博客中关于 Python 的内容，这是咋回事？

其实很多人并不会用 Google，除了翻墙的限制，也是因为平常的简单搜索足以了，它有一个非常棒的特性 `site`
```bash
site:<website> <key worlds>
```
按照这样的格式进行搜索，你就可以只搜索某一个网站的内容了。
```javascript
<input id='search' onkeydown="search()"/>
<script>
function search() {
    var e = window.event
    if( e.key == 'Enter' ){
        var value = document.getElementById('search').value
        value = 'site:https://wxnacy.com ' + value
        value = encodeURIComponent(value)   // urlencode 编码
        var url = 'https://www.google.com/search?q=' + value
        window.open(url,'_blank');      // 打开新标签
    }
}
</script>
```
利用这段代码，你就可以轻松的给你的网站添加 Google 搜索了，唯一的缺点就是需要翻墙，但是我不担心这点，反正能搜索到我网站的也都是从 Google 搜索过来的，它不想某度花钱才能被搜到。

利用这一点，你也可以搜索还没有添加搜索功能的博客网站了。

Google 还有很多其他的高级搜索，有时间我在整理一下。
