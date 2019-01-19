---
title: Javascript replace() 方法
tags:
  - javascript
date: 2018-02-20 18:44:57
---


replace() 方法用于在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串。

<!-- more --><!-- toc -->
## 使用
```java
stringObject.replace(regexp/substr,newSubstr/function)

// regexp/substr 必需。规定子字符串或要替换的模式的 RegExp 对象。
// 请注意，如果该值是一个字符串，则将它作为要检索的直接量文本模式，而不是首先被转换为 RegExp 对象。

// newSubstr 必需。一个字符串值。规定了替换文本或生成替换文本的函数。

// function 一个函数，用于创建新的子字符串以用于替换给定的正则表达式或substr的匹配。
```
newSubstr 中如果有 $ 字符具有特定的含义。如下所示，它说明从模式匹配得到的字符串将用于替换
```bash
$1、$2、...、$99    # 与 regexp 中的第 1 到第 99 个子表达式相匹配的文本。
$&                  # 与 regexp 相匹配的子串。
$`                  # 位于匹配子串左侧的文本。
$'                  # 位于匹配子串右侧的文本。
$$                  # 直接量符号。'`
```

## 例子
替换第一个
```javascript
var str="Visit Microsoft!"
document.write(str.replace(/Microsoft/, "W3School"))
```
```html
Visit W3School!
```

全局替换
```javascript
var str="Welcome to Microsoft! "
str=str + "We are proud to announce that Microsoft has "
str=str + "one of the largest Web Developers sites in the world."

document.write(str.replace(/Microsoft/g, "W3School"))
```
```html
Welcome to W3School! We are proud to announce that W3School
has one of the largest Web Developers sites in the world.
```

全局替换
```javascript
var str="Welcome to Microsoft! "
str=str + "We are proud to announce that Microsoft has "
str=str + "one of the largest Web Developers sites in the world."

document.write(str.replace(/Microsoft/g, "W3School"))
```
```html
Welcome to W3School! We are proud to announce that W3School
has one of the largest Web Developers sites in the world.
```

首字母转大写
```java
name = 'aaa bbb ccc';
uw=name.replace(/\b\w+\b/g, function(word){
        return word.substring(0,1).toUpperCase()+word.substring(1);
    }
);

document.write(uw);
```
```bash
Aaa Bbb Ccc
```

- [JavaScript replace() 方法](http://www.w3school.com.cn/jsref/jsref_replace.asp)
- [String.prototype.replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
