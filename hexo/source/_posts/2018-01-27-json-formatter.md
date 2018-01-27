---
title: JSON Format 工具
date: 2018-01-27 16:02:39
tags: [工具]
---

JSON 格式化工具
<!-- more -->

{% raw %}
<textarea id="plain" style="width: 100%; height: 400px">
{"name": "wxnacy", "arr": ["a", "b", 'c']}
</textarea>
<span id="err" style="color: red"></span><br/>
<button onClick="format()">格式化</button>
<script>
function format() {
    var plain = document.getElementById('plain').value
    try{
        plain = plain.replace(/'/g, "\"")
        var data = JSON.parse(plain)
        var output = JSON.stringify(data, null, 4);
        document.getElementById('plain').value = output;
    } catch(e) {
        document.getElementById('err').innerHTML = e.message;
    }
}
</script>
{% endraw %}
