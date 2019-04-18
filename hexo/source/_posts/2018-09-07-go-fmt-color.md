---
title: Go 如何给屏幕打印信息加上颜色
tags:
  - go
date: 2018-09-07 11:13:45
---

Go 语言可以很简单的给屏幕打印信息加上颜色。

<!-- more -->

![color1](https://raw.githubusercontent.com/wxnacy/image/master/blog/output-color.png)

```go
conf := 0   // 配置、终端默认设置
bg   := 0   // 背景色、终端默认设置
text := 31  // 前景色、红色
fmt.Printf("\n %c[%d;%d;%dm%s%c[0m\n\n", 0x1B, conf, bg, text, "testPrintColor", 0x1B)
```

颜色和配置的取值范围

```bash
// 前景 背景 颜色
// ---------------------------------------
// 30  40  黑色
// 31  41  红色
// 32  42  绿色
// 33  43  黄色
// 34  44  蓝色
// 35  45  紫红色
// 36  46  青蓝色
// 37  47  白色
//
// 代码 意义
// -------------------------
//  0  终端默认设置
//  1  高亮显示
//  4  使用下划线
//  5  闪烁
//  7  反白显示
//  8  不可见
```

[Go语言在Linux环境下输出彩色字符](https://www.cnblogs.com/journeyonmyway/p/4317108.html) 这篇文章遍历打印了每种颜色的组合。

我们可以将该方法封装了起来供程序使用

```go
func SetColor(msg string, conf, bg, text int) string {
    return fmt.Sprintf("%c[%d;%d;%dm%s%c[0m", 0x1B, conf, bg, text, msg, 0x1B)
}
```

将颜色定义为常量，比如

```go
const (
	TextBlack = iota + 30
	TextRed
	TextGreen
	TextYellow
	TextBlue
	TextMagenta
	TextCyan
	TextWhite
)
```

完整代码见 [demo](https://github.com/wxnacy/study/blob/master/goland/src/color/main.go)
