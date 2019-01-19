---
title: jQuery 监听 element change 事件
date: 2018-08-07 10:30:00
tags: [jquery]
---

change 事件适用于文本域在值变化时触发，我们也可以在非标单元素中通过主动调用 `change()` 方法来触发 change 事件

<!-- more --><!-- toc -->
```java
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>change事件</title>
		<style>
			#container {
				min-height: 120px;
				border: 1px solid #aaa;
			}
		</style>
	</head>
	<body>
		<div id="container">

		</div>
		<button type="button" id="btn">add "aaa" for div</button>
        <button type="button" id="attr">监听属性</button>

 <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script>

			function changes(){
				alert("changes");

			}

			$("#btn").click(function() {
				$("#container").append("aaa").change();
			});
			$("#attr").click(function() {
				$("#container").attr("data-value", "test").change();
			});
			$("#container").bind("change", changes);
		</script>
	</body>
</html>
```

[试一试](/run/?id=68719513614)


