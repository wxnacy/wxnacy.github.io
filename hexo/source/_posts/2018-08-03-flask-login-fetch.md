---
title: FlaskLogin 解决 Fetch 不能携带登录信息的问题
date: 2018-08-03 20:35:12
tags: [flask]
---

使用 flask-login 模块时，如果在 controller 中使用 `@login_required` 检查是否登录的话，在使用 fetch 请求接口，就会报没有登录的错误。

<!-- more --><!-- toc -->
这是因为 fetch 在请求时，默认并没有携带 flask-login 所需要的登录信息，了解这一点就好说了

```javascript
fetch('/admin_content/save',{
    credentials: 'include',
}).then(function(res){
    return res.json()
}).then(function(data){
    console.log(data);
})
```

只需要在请求时加上 `credentials: 'include'` 即可

- [Flask-Login, Session Management and AJAX](https://stackoverflow.com/questions/50236564/flask-login-session-management-and-ajax)
