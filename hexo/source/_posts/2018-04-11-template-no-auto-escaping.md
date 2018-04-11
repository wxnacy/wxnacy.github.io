---
title: Python Template 关闭自动转义
date: 2018-04-11 17:11:52
tags: [python]
---

在用 Python 的 Template 写页面时碰见一个自动转义的问题。
<!-- more -->

原始数据

```python
['2018-04-10']
```

在用模板展示

```html
{{ days }}
```

得到了这样的结果，很明显它将 `'` 单引号转义了，这不是我想要的

```bash
[&#39;2018-04-10&#39;]
```

Template 默认是开启转义的，需要我们手动关闭掉

```html
{% autoescape off %}
{{ days }}
{% endautoescape %}
```

显示正常

