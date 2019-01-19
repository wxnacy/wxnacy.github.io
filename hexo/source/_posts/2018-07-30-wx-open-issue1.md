---
title: 微信第三方平台授权问题：授权入口页所在域名：空
date: 2018-07-30 19:42:54
tags: [微信]
---

在微信第三方平台[授权](https://open.weixin.qq.com/cgi-bin/showdocument?action=dir_list&t=resource/res_list&verify=1&id=open1453779503&token=&lang=zh_CN)的时候碰见一个错误。

<!-- more --><!-- toc -->
![/image/wxsq1.png](/images/wxsq1.png)

如图在**引入用户进入授权页**这一步骤中，访问授权地址时报错

```bash
https://mp.weixin.qq.com/cgi-bin/componentloginpage?component\_appid=xxxx&pre\_auth\_code=xxxxx&redirect\_uri=xxxx&auth\_type=xxx。
```

开始以为 `redirect_uri` 和第三方应用配置的授权域名不同导致的，但是查看后发现并没有不同。

并且**授权入口页所在域名：空**这叫话一时不理解是什么意思，google 后发现原来是必须从 `redirect_uri` 所在域名访问该地址才行，我从浏览器里访问自然是不行的。

或者请求加上同域名的 refer 即可
