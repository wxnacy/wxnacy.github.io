---
title: Go byte 和 string 的相互转换
date: 2018-08-15 15:26:58
tags: [go]
---

本章简单了解下 Go 语言中 byte 和 string 的相互转换

<!-- more --><!-- toc -->

## 普通字符串

**string to byte**

```go
b := []byte(s)
```

**byte to string**

```go
s := string(b)
```

## 十六进制字符串

需要引入包

```go
import "encoding/hex"
```

**hex string to byte**

```go
b, err := hex.DecodeString(s)
```

**byte to hex string**

```go
s := hex.EncodeToString(b)
```

另外利用 `fmt` 包的格式化也可以将字节转为十六进制字符串

```go
s := fmt.Strintf("%x", b)
```

- [hex](https://golang.org/pkg/encoding/hex/)
