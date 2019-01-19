---
title: Go 判断文件是否存在
date: 2018-08-30 11:19:48
tags: [go]
---

Go 判断文件是否存在

<!-- more --><!-- toc -->

```go
// 判断路径是否存在
func IsExists(path string) (os.FileInfo, bool) {
	f, err := os.Stat(path)
    return f, err == nil || os.IsExist(err)
}
```

如果当前用户没有访问该文件的权限时，err 也有值，所以需要使用 `os.IsExist()` 方法加一层判断。

**判断是否文件夹**

```go
// 判断所给路径是否为文件夹
func IsDir(path string) (os.FileInfo, bool) {
    f, flag := IsExists(path)
    return f, flag && f.IsDir()
}
```

**判断是否文件**

```go
// 判断所给路径是否为文件
func IsFile(path string) (os.FileInfo, bool) {
    f, flag := IsExists(path)
    return f, flag && !f.IsDir()
}
```
