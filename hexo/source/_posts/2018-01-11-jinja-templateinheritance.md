---
title: Jinja2 模板继承
tags:
  - python
  - jinja2
date: 2018-01-11 11:01:42
---


在 Jinja2 中非常有用的一个功能就是模板继承，它可以像任何面向对象语言一样，实现模板的多态。

<!-- more --><!-- toc -->
## 父模板
定义 `base.html` 如下
```html
<!doctype html>
<html>
	<head>
		{% block head %}
		<title>{% block title %}{% endblock %} | wxnacy 博客</title>
		{% endblock %}
	</head>
	<body>
		<div id="content">{% block content %}{% endblock %}</div>
		<div id="footer">
			{% block footer %}
			    Copyright 2018 by <a href="https://wxnacy.com">wxnacy.com</a>.
			{% endblock %}
		</div>
	</body>
</html>
```
在模板中 `{{ block }}{{ endblock }}` 定义了需要多块，它们可以在子模块中进行填充，或直接继承

## 子模块
```html
{% extends "base.html" %}
{% block title %}Jinja2 模板继承{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Jinja2 模板继承</h1>
    <p class="important">
        在 Jinja2 中非常有用的一个功能就是模板继承，它可以像任何面向对象语言一样，实现模板的多态。
    </p>
{% endblock %}
```
在子模板中使用 `super()` 标签，可以对 `block head` 进行继承并实现多态。

## 效果
渲染后页面源码为
```html
<!doctype html>
<html>
	<head>
		<title>Jinja2 模板继承 | wxnacy 博客</title>
        <style type="text/css">
            .important { color: #336699; }
        </style>
	</head>
	<body>
		<div id="content">
        <h1>Jinja2 模板继承</h1>
        <p class="important">
            在 Jinja2 中非常有用的一个功能就是模板继承，它可以像任何面向对象语言一样，实现模板的多态。
        </p>
        </div>
		<div id="footer">
            Copyright 2018 by <a href="https://wxnacy.com">wxnacy.com</a>.
		</div>
	</body>
</html>
```
