---
title: Golang 图片压缩
date: 2019-01-15 17:22:56
tags: [go]
---

Golang 图片压缩可以直接使用第三方包 [resize](https://github.com/nfnt/resize)

<!-- more --><!-- toc -->

## 安装

```bash
$ go get github.com/nfnt/resize
```

## 使用

**导入**

```go
import "github.com/nfnt/resize"
```

**语法**

`resize` 有两个方法 `Resize` `Thumbnail`

```go
resize.Resize(width, height uint, img image.Image, interp resize.InterpolationFunction) image.Image
// resize.Resize 使用插值函数interp创建具有新尺寸（宽度，高度）的缩放图像。 如果宽度或高度设置为0，则将其设置为保留宽高比值。
```

```go
resize.Thumbnail(maxWidth, maxHeight uint, img image.Image, interp resize.InterpolationFunction) image.Image
// resize.Thumbnail 缩小图像，将其纵横比保持为最大尺寸（maxWidth，maxHeight）。 如果原始尺寸小于提供的尺寸，它将返回原始图像。
```

**简单使用**

```go
package main

import (
    "fmt"
    "github.com/nfnt/resize"
    "image/png"
    "os"
    "log"
)

func main() {
    file_path := "/Users/wxnacy/Downloads/react-app1.png"

    fmt.Println("Hello World")
    file, err := os.Open(file_path)
	if err != nil {
		log.Fatal(err)
	}

	// decode jpeg into image.Image
	img, err := png.Decode(file)
	if err != nil {
		log.Fatal(err)
	}
	file.Close()

	// resize to width 1000 using Lanczos resampling
	// and preserve aspect ratio
    m := resize.Resize(800, 0, img, resize.NearestNeighbor)

	out, err := os.Create("react.NearestNeighbor.png")
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()

	// write new image to file
	png.Encode(out, m)
}
```

这里边需要关注的是参数 `resize.InterpolationFunction`，它有几个值
- NearestNeighbor: [Nearest-neighbor interpolation](https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation)
- [Bilinear: Bilinear interpolation](https://en.wikipedia.org/wiki/Bilinear_interpolation)
- Bicubic: [Bicubic interpolation](https://en.wikipedia.org/wiki/Bicubic_interpolation)
- MitchellNetravali: [Mitchell-Netravali interpolation](https://dl.acm.org/citation.cfm?id=378514)
- Lanczos2: [Lanczos resampling](https://en.wikipedia.org/wiki/Lanczos_resampling) with a=2
- Lanczos3: [Lanczos resampling](https://en.wikipedia.org/wiki/Lanczos_resampling) with a=3

这个压缩方式的展示效果可以从这里看到 https://github.com/nfnt/resize#downsizing-samples

我挨个点连接进行，发现实在不想去纠结他们的具体原理，我只想比较压缩后的文件大小

我依次按照集中格式进行了压缩，我们对比下文件大小

```bash
-rw-r--r--@  1 wxnacy  staff  64633 Jan 18 18:01 react-app1.png
-rw-r--r--@  1 wxnacy  staff  19857 Jan 19 17:13 react.NearestNeighbor.png
-rw-r--r--   1 wxnacy  staff  23336 Jan 19 17:12 react.Bilinear.png
-rw-r--r--   1 wxnacy  staff  25966 Jan 19 17:12 react.MitchellNetravali.png
-rw-r--r--@  1 wxnacy  staff  27241 Jan 19 17:12 react.Lanczos2.png
-rw-r--r--   1 wxnacy  staff  27356 Jan 19 17:12 react.Bicubic.png
-rw-r--r--@  1 wxnacy  staff  31222 Jan 19 17:09 react.Lanczos3.png
```

经过对比，`Lanczos3` 算法文件最大，图片最清晰，`NearestNeighbor` 最差

ok，这样我们就知道了，如果你追求清晰的或者文件大小该选什么类型了
