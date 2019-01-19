---
title: JavaScript 上传文件时获取 File 属性
date: 2018-04-27 09:54:21
tags: [javascript]
---

总结下获取 `File` 属性以及三种上传文件的方法

<!-- more --><!-- toc -->

## 文件属性

- `File.lastModified` 只读，获取文件最后修改的时间戳
- `File.lastModifiedDate` 只读，获取文件最后的修改时间，现在已经废除，建议使用 `File.lastModified`
- `File.name` 只读，获取文件名
- `File.size` 只读，文件大小，单位 bytes
- `File.type` 只读，文件类型

## 点击上传

```javascript
<body>
<input type="file" id = 'file' multiple/><br/>
<ul id = 'output'></ul>
</body>
<script>
document.getElementById("file").addEventListener("change", handleFileSelecter, false);

function handleFileSelecter(e) {
    var content = '';
    var files = e.target.files;
    content = `<li>总数: ${files.length}</li>`
        for(var i = 0; i < files.length; i++){
            console.log(files[i]);
            var f = files[i]
                content += '<li>-------------------------</li>';
            content += `<li>name: ${f.name}</li>`;
            content += `<li>size: ${f.size}</li>`;
            content += `<li>type: ${f.type}</li>`;
            content += `<li>lastModified: ${f.lastModified}</li>`;
            content += `<li>lastModifiedDate: ${f.lastModifiedDate}</li>`;

        }
    document.getElementById("output").innerHTML = content;
}
</script>
```

[试一试](/run/?id=68719485239)

## 拖动上传

```javascript
<body>
<div id="file">将文件拖放到此处</div>
<ul id='output'></ul>
</body>
<script>
document.getElementById("file").addEventListener('dragover', handleDrop, false);
document.getElementById("file").addEventListener('drop', handleFileSelect, false);

function handleDrop(e){
    e.stopPropagation();
    e.preventDefault();
    e.dataTransfer.dropEffect = 'copy';
}

function handleFileSelect(e) {
    e.stopPropagation();
    e.preventDefault();
    var content = '';
    var files = e.dataTransfer.files;
    content = `<li>总数: ${files.length}</li>`
        for(var i = 0; i < files.length; i++){
            var f = files[i]
                content += '<li>-------------------------</li>';
            content += `<li>name: ${f.name}</li>`;
            content += `<li>size: ${f.size}</li>`;
            content += `<li>type: ${f.type}</li>`;
            content += `<li>lastModified: ${f.lastModified}</li>`;
            content += `<li>lastModifiedDate: ${f.lastModifiedDate}</li>`;

        }
    document.getElementById("output").innerHTML = content;
}
</script>
```

[试一试](/run/?id=68719485256)

## 点击或拖动

```javascript
<body>
<div id="file">点击或将文件拖放到此处</div>
<ul id='output'></ul>
</body>
<script>
document.getElementById("file").addEventListener('dragover', handleDrop, false);
document.getElementById("file").addEventListener('drop', handleFileSelect, false);
document.getElementById("file").addEventListener('click', handleClick, false);

function handleClick(){
    var text = "<input type='file' onChange='handleFileChangeSelect() />'";
    var f = document.createElement('input');
    f.type = 'file'
        f.addEventListener("change", handleFileChangeSelect, false);
    f.multiple = true
        f.click()
};

function handleDrop(e){
    e.stopPropagation();
    e.preventDefault();
    e.dataTransfer.dropEffect = 'copy';
}

function handleFileSelect(e) {
    e.stopPropagation();
    e.preventDefault();
    var files = e.dataTransfer.files;
    viewFiles(files);
}

function handleFileChangeSelect(e) {
    e.stopPropagation();
    e.preventDefault();
    var files = e.target.files;
    viewFiles(files);
}

function viewFiles(files){
    var content = '';
    content = `<li>总数: ${files.length}</li>`
        for(var i = 0; i < files.length; i++){
            var f = files[i]
                content += '<li>-------------------------</li>';
            content += `<li>name: ${f.name}</li>`;
            content += `<li>size: ${f.size}</li>`;
            content += `<li>type: ${f.type}</li>`;
            content += `<li>lastModified: ${f.lastModified}</li>`;
            content += `<li>lastModifiedDate: ${f.lastModifiedDate}</li>`;

        }
    document.getElementById("output").innerHTML = content;
}
</script>
```

[试一试](/run/?id=68719485268)

- [File](https://developer.mozilla.org/en-US/docs/Web/API/File)
- [通过 File API 使用 JavaScript 读取文件](https://www.html5rocks.com/zh/tutorials/file/dndfiles/)
