---
title: Python 操作 ini 配置文件
tags:
  - python
date: 2019-04-11 11:25:49
---


Python 中使用 `configparser` 模块来操作 ini 文件。

<!-- more --><!-- toc -->

假如想要生成 `example.ini` 文件，内容如下：

```bash
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no
```

**写入操作**

`configparser.ConfigParser()` 方法生成实例，配置和读取内容都可以按照 `dict` 的方式进行。

```python
>>> import configparser
>>> config = configparser.ConfigParser()
>>> config['DEFAULT'] = {'ServerAliveInterval': '45',
...                      'Compression': 'yes',
...                      'CompressionLevel': '9'}
>>> config['bitbucket.org'] = {}
>>> config['bitbucket.org']['User'] = 'hg'
>>> config['topsecret.server.com'] = {}
>>> topsecret = config['topsecret.server.com']
>>> topsecret['Port'] = '50022'     # mutates the parser
>>> topsecret['ForwardX11'] = 'no'  # same here
>>> config['DEFAULT']['ForwardX11'] = 'yes'
>>> with open('example.ini', 'w') as configfile:
...   config.write(configfile)
...
```

**读取操作**

```python
>>> config = configparser.ConfigParser()
>>> config.sections()
[]
>>> config.read('example.ini')
['example.ini']
>>> config.sections()
['bitbucket.org', 'topsecret.server.com']
>>> 'bitbucket.org' in config
True
>>> 'bytebong.com' in config
False
>>> config['bitbucket.org']['User']
'hg'
>>> config['DEFAULT']['Compression']
'yes'
>>> topsecret = config['topsecret.server.com']
>>> topsecret['ForwardX11']
'no'
>>> topsecret['Port']
'50022'
>>> for key in config['bitbucket.org']:
...     print(key)
user
compressionlevel
serveraliveinterval
compression
forwardx11
>>> config['bitbucket.org']['ForwardX11']
'yes'
```

**修改操作**

因为此处配置的写入是覆盖模式，所以如果想要修改文件，需要判断下文件是否存在，存在的话，先加载文件内容。

```python
def config(filepath, section, **data):
    '''
    filepath: 配置文件地址
    '''
    conf = configparser.ConfigParser()
    if os.path.exists(filepath):
        conf.read(filepath)

    conf[section] = data

    with open(filepath, 'w') as f:
        conf.write(f)
        f.close()
```

- [configparser](https://docs.python.org/3/library/configparser.html)
