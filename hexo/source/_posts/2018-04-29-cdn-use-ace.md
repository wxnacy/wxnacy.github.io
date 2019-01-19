---
title: 使用 CDN 加载的方式运行 Ace
date: 2018-04-29 16:54:11
tags: [html, javascript]
---

一个使用 cdn 加载的方式运行 ace 组件。

<!-- more --><!-- toc -->

## 使用

**预览**

![ace](https://wxnacy-img.oss-cn-beijing.aliyuncs.com/upload/1524992481.924261-ace.png)

**Demo**
```html
<body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.2.9/ace.js"></script>
    <textarea name="my-xml-editor" data-editor="html" data-gutter="1" rows="20">
<html>
    <body>
        Hello World
    </body>
</html>
    </textarea>

<script>

    $(function() {
        $('textarea[data-editor]').each(function() {
            var textarea = $(this);
            var mode = textarea.data('editor');
            var editDiv = $('<div>', {
                position: 'absolute',
                width: textarea.width(),
                height: textarea.height(),
                'class': textarea.attr('class')
            }).insertBefore(textarea);
            textarea.css('display', 'none');
            var editor = ace.edit(editDiv[0]);
            editor.renderer.setShowGutter(textarea.data('gutter'));
            editor.getSession().setValue(textarea.val());
            editor.getSession().setMode("ace/mode/" + mode);
            editor.setTheme("ace/theme/idle_fingers");

            // copy back to textarea on form submit...
            textarea.closest('form').submit(function() {
                textarea.val(editor.getSession().getValue());
            })
        });
    });
</script>
</body>
```

[试一试](/run/?id=68719486928)

## 美化代码

需要下载 [beautify.js](https://raw.githubusercontent.com/ajaxorg/ace/master/lib/ace/ext/beautify.js) 扩展

```javascript
var beautify = ace.require("ace/ext/beautify"); // get reference to extension
var editor = ace.edit("editor"); // get reference to editor
beautify.beautify(editor.session);
```

- [api](https://ace.c9.io/#nav=api&api=ace)
- [github](https://github.com/ajaxorg/ace)
