---
title: 网络请求工具 cURL
date: 2017-08-16
tags: [linux, http]
---

> cRUL 是一种命令行工具，作用是发出网络请求，然后得到和提取数据，显示在 "标准输出"（stdout）上面。

<!-- more -->
## 查看网页源码
```bash
$ curl baidu.com
```
```html
<html>
<meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
</html>
```
如果要把这个网页保存下来，可以使用 `-o` 或 `--output` 参数，这就相当于使用 wget 命令了。
```bash
$ curl -o file_name baidu.com
```

## 自动跳转
有的网址是自动跳转的。使用`-L`或`--location`参数，curl就会跳转到新的网址。
```bash
$ curl -L baidu.com
```

## 显示头信息
`-i` 或 `--include` 参数可以显示 **http response** 的头信息，连同网页代码一起。
`-I` 或 `--head` 参数则是只显示 **http response** 的头信息。
```bash
$ curl -i baidu.com
```
```html
HTTP/1.1 200 OK
Date: Wed, 16 Aug 2017 08:21:49 GMT
Server: Apache
Last-Modified: Tue, 12 Jan 2010 13:48:00 GMT
ETag: "51-47cf7e6ee8400"
Accept-Ranges: bytes
Content-Length: 81
Cache-Control: max-age=86400
Expires: Thu, 17 Aug 2017 08:21:49 GMT
Connection: Keep-Alive
Content-Type: text/html

<html>
<meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
</html>

```

## 显示通信过程
`-v` 或 `--verbose` 参数可以显示一次 http 通信的整个过程，包括端口连接和
**http request** 头信息。
```bash
$ curl -v baidu.com
```
```html
* Rebuilt URL to: baidu.com/
*   Trying 220.181.57.217...
* Connected to baidu.com (220.181.57.217) port 80 (#0)
> GET / HTTP/1.1
> Host: baidu.com
> User-Agent: curl/7.43.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Wed, 16 Aug 2017 08:24:49 GMT
< Server: Apache
< Last-Modified: Tue, 12 Jan 2010 13:48:00 GMT
< ETag: "51-47cf7e6ee8400"
< Accept-Ranges: bytes
< Content-Length: 81
< Cache-Control: max-age=86400
< Expires: Thu, 17 Aug 2017 08:24:49 GMT
< Connection: Keep-Alive
< Content-Type: text/html
<
<html>
<meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
</html>
* Connection #0 to host baidu.com left intact
```
也可以通过 `--trace` 或 `--trace-ascii` 命令查看更详细通信过程，执行后通过制定
的日志地址查看
```bash
$ curl --trace ${log_path} baidu.com
$ curl --trace-ascii ${log_path} baidu.com
```
## HTTP动词
curl默认的HTTP动词是GET，使用`-X`参数可以支持其他动词。

```bash
$ curl -X POST baidu.com
```

## 增加头信息
```bash
# 使用-H 或 --header 可以起到这个作用
$ curl localhost:8002/test -H "Content-Type:application/json"
```

## 发送表单信息
```bash
# GET方法比较简单，网址后直接跟参数
$ curl localhost:8002/test?data=xxx
# POST方法通过--data或-d参数实现
$ curl -X POST localhost:8002/test --data "name=xxx" --data "password=xxx"
$ curl -X POST localhost:8002/test -H "Content-Type:application/x-www-form-urlencoded" -d "name=win"
# 使用application/json 提交json数据
$ curl -X POST localhost:8002/test -H "Content-Type:application/json" -d '{"name":"wxnacy"}'
#如果你的数据没有经过表单编码，还可以让curl为你编码，参数是`--data-urlencode`。
$ curl -X POST localhost:8002/test --data-urlencode "data=1 2"
```

## 文件上传
```bash
$ curl --form upload_field=@localfilename localhost:8002/test
$ curl --form "upload_field=@new.txt;type=text/plain" localhost:8002/test
```

## Referer字段
需要添加request头信息referer标示从哪里跳转来的
```bash
$ curl localhost:8002/test --referer ${from_url}
```
## user-agent字段
使用 `--user-agent` 或 `-A` 可以模拟发送 user-agent 字段
```bash
$ curl localhost:8002/test --user-agent "device"
```
## cookie
```bash
# 发送的cookie可以在response headers中看到
$ curl localhost:8002/test --cookie "name=ss"
# -c 可以保存服务器返回的cookies到文件中
$ curl localhost:8002/test -c ${cookie_file}
# -b 可以使用这个文件作为cookie信息，进行后续的请求。
$ curl localhost:8002/test -b ${cookie_file}
```


## HTTP认证
有些网域需要HTTP认证，这时 cURL 需要用到`--user`或 `-u`参数。
```bash
# 这时候服务器会在头信息中接收到Authorization字段，值为Basic + name:pass的base64加密数值
$ curl localhost:8002/test --user name:apss
```

## 参考资料
- [curl网站开发指南](http://www.ruanyifeng.com/blog/2011/09/curl.html)
