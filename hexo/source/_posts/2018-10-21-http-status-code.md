---
title: HTTP 返回状态码
tags:
  - http
date: 2018-10-21 17:49:03
---

总结下常见的 HTTP 返回状态码

<!-- more -->
<!-- toc -->

## 2XX 成功

- `200 OK` 请求成功
- `201 Created` 资源创建成功，通常在 POST 请求返回
- `204 No Content` 请求成功，但是没有返回内容

## 4XX 客户端请求错误

- `400 Bad Request` 请求参数有误，或语义无法被服务端理解
- `401 Unauthorized` 用户验证没通过
- `403 Forbidden` 服务器已经理解请求，但是拒绝执行它。
- `404` 找不到页面
- `405 Method Not Allowed` 使用了错误的请求方式来请求资源。比如 POST 资源使用 GET 方式请求。
- `413 Request Entity Too Large` 该请求提交的实体数据大小超过了服务器愿意或者能够处理的范围。
- `414 Request-URI Too Long` 请求的 URI 长度超过了服务器能够解释的长度
- `429 Too Many Requests` 用户在给定的时间内发送了太多的请求。旨在用于网络限速。


## 5XX 服务器处理错误

- `500 Internal Server Error` 通用错误消息，服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。没有给出具体错误信息。
- `502 Bad Gateway` 作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
- `504 Gateway Timeout` 作为网关或者代理工作的服务器尝试执行请求时，未能及时从上游服务器（URI标识出的服务器，例如HTTP、FTP、LDAP）或者辅助服务器（例如DNS）收到响应。


- [HTTP 响应代码](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status)
- [HTTP 状态码](https://zh.wikipedia.org/wiki/HTTP%E7%8A%B6%E6%80%81%E7%A0%81)
