---
title: JavaScript 操作 Select DOM
tags:
  - javascript
date: 2018-05-03 09:35:53
---


Javascript 操作 Select DOM 的一些方法。

<!-- more --><!-- toc -->

```html
<select id="defaultSelect">
    <option value="GET">GET</option>
    <option value="POST" selected>POST</option>
    <option value="PUT">PUT</option>
</select>
```

**获取 Select DOM**
```javascript
var objSelect = document.getElementById('defaultSelect');
```

## 属性操作

```javascript
objSelect.value = 'GET'                         // 设置值
objSelect.value                                 // 获取值
objSelect.selectedIndex                         // 获取索引
objSelect.options[selectedIndex].text           // 获取选中text
objSelect.options.length = 0;                   // 清空
```

## 判断是否有某个值

```javascript
function isExitItem(objSelect, objItemValue) {
    var isExit = false;
    for (var i = 0; i < objSelect.options.length; i++) {
        if (objSelect.options[i].value == objItemValue) {
            isExit = true;
            break;
        }
    }
    return isExit;
}
```

## 添加 Option

```javascript
function addItemToSelect(objSelect, objItemText, objItemValue) {
    if (isExitItem(objSelect, objItemValue)) {
        alert("该 Item 的 Value 值已经存在");
    } else {
        var varItem = new Option(objItemText, objItemValue);
        objSelect.options.add(varItem);
        alert("成功加入");
    }
}
```

## 修改 text 值

```javascript
function updateItemTextForSelect(objSelect, objItemText, objItemValue) {
    //判断是否存在
    if (isExitItem(objSelect, objItemValue)) {
        for (var i = 0; i < objSelect.options.length; i++) {
            if (objSelect.options[i].value == objItemValue) {
                objSelect.options[i].text = objItemText;
                break;
            }
        }
        alert("成功修改");
    } else {
        alert("该select中 不存在该项");
    }
}
```

## 删除 Option

```javascript
function removeItemFromSelect(objSelect, objItemValue) {
    //判断是否存在
    if (isExitItem(objSelect, objItemValue)) {
        for (var i = 0; i < objSelect.options.length; i++) {
            if (objSelect.options[i].value == objItemValue) {
                objSelect.options.remove(i);
                break;
            }
        }
        alert("成功删除");
    } else {
        alert("该select中 不存在该项");
    }
}
```

## 根据 Text 选中 item

```javascript
function selectItemByText(objSelect, objItemText) {
    //判断是否存在
    var isExit = false;
    for (var i = 0; i < objSelect.options.length; i++) {
        if (objSelect.options[i].text == objItemText) {
            objSelect.options[i].selected = true;
            isExit = true;
            break;
        }
    }
    //Show出结果
    if (isExit) {
        alert("成功选中");
    } else {
        alert("该select中 不存在该项");
    }
}
```

[试一试](/run/?id=68719487623)

