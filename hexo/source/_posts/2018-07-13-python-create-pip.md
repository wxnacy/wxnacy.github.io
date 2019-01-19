---
title: Python 编写 pip 包并上传到 pypi
date: 2018-07-13 13:54:58
tags: [python]
---

用了这么长时间的 python，一直想写些开源的东西回馈社区，最近在封装微信的公众平台，借着机会研究了下怎样封装 pip 包，并上传到 pypi。

<!-- more --><!-- toc -->

## 创建项目

首先创建项目，目录结构如下

```bash
-- wwx
  |
  |-- wwx
  |  |
  |  |-- __init__.py
  |  |-- models.py
  |
  |-- setup.py
```

其中 `wwx/wwx` 是主代码目录，`setup.py` 是必备的打包文件

**setup.py**

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from setuptools import setup, find_packages

setup(
    name = 'wwx',
    version = '0.0.1',
    keywords='wx',
    description = 'a library for wx Developer',
    license = 'MIT License',
    url = 'https://github.com/wxnacy/wwx',
    author = 'wxnacy',
    author_email = 'wxnacy@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [
        'requests>=2.19.1',
        'pycrypto>=2.6.1',
        'xmltodict>=0.11.0'
        ],
)
```

项目代码根据你的需求编写，你可以写一个这样的例子来测试

**models.py**

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

class Message():
    @classmethod
    def test():
        print('Hello World')
```

** `__init__.py` **

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from .models import Message
```

## 安装到本地测试

接下来在 `setup.py` 所在目录下执行安装命令，安装到本地

```bash
$ pip install .
```

在项目中你就可以使用测试了

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)

from wwx import Message

Message.test()
```

## 打包

测试完成后，再上传到 pypi 之前需要先打包

```bash
$ python setup.py <params>
```

`params` 有如下取值

```bash
sdist             create a source distribution (tarball, zip file, etc.)
bdist             create a built (binary) distribution
bdist_dumb        create a "dumb" built distribution
bdist_rpm         create an RPM distribution
bdist_wininst     create an executable installer for MS Windows
bdist_egg         create an "egg" distribution
```

`sdist` 可以支持上传到 pypi

```bash
$ python setup.py sdist
```

然后根目录中会出现 `dist` 目录存放打包文件

## 上传 pypi

最后一步上传到 pypi，首先去[官网](https://pypi.org/)搜索确认项目名没有被占用，并注册用户，然后使用 `twine` 进行上传

**下载 twine**

```bash
$ pip install twine
```

**上传**

```bash
$ twine upload dist/*
```

然后根据提示输入用户名密码即可。

**设置全局账户信息**

创建 `~/.pypirc` 文件并添加如下信息

```bash
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = <username>
password = <password>
```

然后再次上传就不会提示输入用户密码了
