---
title: Python XML 转换为 JSON
date: 2018-07-07 11:39:32
tags: [python]
---

现在接口数据返回基本都用 JSON 格式，然而一些大公司依然保留 XML 格式，比如微信，我们依然想把 XML 转为 JSON 格式，因为它更流行更容易读。

<!-- more --><!-- toc -->
`xmltodict` 模块可以实现该功能。

**下载**

```bash
$ pip install xmltodict
```

**使用**

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import xmltodict

data = '<xml> <ToUserName><![CDATA[gh_96c685096fbd]]></ToUserName> <Encrypt><![CDATA[awoq2zcSPV4GAjg5u8Jr5E2G4/dUS3FbbTgeDlhYOHKxC2a7Bb+WROg6gEUUlZdgokjgUHHdPikMI/GvqGKoQ66HLxIFf54xq8FdFdXLLoZBlqHztUL3wV/T1uv25IkmlVe7zfkOG9erKemIw74gKuNzimm49Vam/OJVoYnKPYMhkWJcz9YQcP2y79ZMA6giEnGTVnAPFIc0wgpPMbpOgfih8s7H/NhE+uA+b9zdbdR5eynW3qbFtXqjRz2hxOb/LGo7djibx6OX5E6PaZ7anKxiq9psPNCo0h43h/7Gy/zT+E0BwgQg9EdjEmD/Dets8pSK7JX5WLO/oAToYVYDDtsIvFRlXK1rbn1rd9eIAj2IgrsrDFM3BGjHHybKTGOf3luSADlnxtXS4rjo8/oaZeyOe4O0JxTLvwwhlew5wd0=]]> </Encrypt> </xml>'

print(xmltodict.parse(data))
```

```bash
OrderedDict([('xml', OrderedDict([('ToUserName', 'gh_96c685096fbd'), ('Encrypt', 'awoq2zcSPV4GAjg5u8Jr5E2G4/dUS3FbbTgeDlhYOHKxC2a7Bb+WROg6gEUUlZdgokjgUHHdPikMI/GvqGKoQ66HLxIFf54xq8FdFdXLLoZBlqHztUL3wV/T1uv25IkmlVe7zfkOG9erKemIw74gKuNzimm49Vam/OJVoYnKPYMhkWJcz9YQcP2y79ZMA6giEnGTVnAPFIc0wgpPMbpOgfih8s7H/NhE+uA+b9zdbdR5eynW3qbFtXqjRz2hxOb/LGo7djibx6OX5E6PaZ7anKxiq9psPNCo0h43h/7Gy/zT+E0BwgQg9EdjEmD/Dets8pSK7JX5WLO/oAToYVYDDtsIvFRlXK1rbn1rd9eIAj2IgrsrDFM3BGjHHybKTGOf3luSADlnxtXS4rjo8/oaZeyOe4O0JxTLvwwhlew5wd0=')]))])
```

达到的结果还不是我们理想的 JSON 格式化，在手动转换一下

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

import xmltodict
import json

data = '<xml> <ToUserName><![CDATA[gh_96c685096fbd]]></ToUserName> <Encrypt><![CDATA[awoq2zcSPV4GAjg5u8Jr5E2G4/dUS3FbbTgeDlhYOHKxC2a7Bb+WROg6gEUUlZdgokjgUHHdPikMI/GvqGKoQ66HLxIFf54xq8FdFdXLLoZBlqHztUL3wV/T1uv25IkmlVe7zfkOG9erKemIw74gKuNzimm49Vam/OJVoYnKPYMhkWJcz9YQcP2y79ZMA6giEnGTVnAPFIc0wgpPMbpOgfih8s7H/NhE+uA+b9zdbdR5eynW3qbFtXqjRz2hxOb/LGo7djibx6OX5E6PaZ7anKxiq9psPNCo0h43h/7Gy/zT+E0BwgQg9EdjEmD/Dets8pSK7JX5WLO/oAToYVYDDtsIvFRlXK1rbn1rd9eIAj2IgrsrDFM3BGjHHybKTGOf3luSADlnxtXS4rjo8/oaZeyOe4O0JxTLvwwhlew5wd0=]]> </Encrypt> </xml>'

print(json.loads(json.dumps(xmltodict.parse(data))))
```

```bash
{'xml': {'ToUserName': 'gh_96c685096fbd', 'Encrypt': 'awoq2zcSPV4GAjg5u8Jr5E2G4/dUS3FbbTgeDlhYOHKxC2a7Bb+WROg6gEUUlZdgokjgUHHdPikMI/GvqGKoQ66HLxIFf54xq8FdFdXLLoZBlqHztUL3wV/T1uv25IkmlVe7zfkOG9erKemIw74gKuNzimm49Vam/OJVoYnKPYMhkWJcz9YQcP2y79ZMA6giEnGTVnAPFIc0wgpPMbpOgfih8s7H/NhE+uA+b9zdbdR5eynW3qbFtXqjRz2hxOb/LGo7djibx6OX5E6PaZ7anKxiq9psPNCo0h43h/7Gy/zT+E0BwgQg9EdjEmD/Dets8pSK7JX5WLO/oAToYVYDDtsIvFRlXK1rbn1rd9eIAj2IgrsrDFM3BGjHHybKTGOf3luSADlnxtXS4rjo8/oaZeyOe4O0JxTLvwwhlew5wd0='}}
```
