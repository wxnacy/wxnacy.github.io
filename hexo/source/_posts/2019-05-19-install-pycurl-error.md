---
title: PySpider 安装的坑：PyCurl 出错
tags:
  - python
date: 2019-05-19 08:01:36
---


问题起源在于安装 PySpider 时需要依赖 PyCurl，过程中报错

<!-- more -->
<!-- toc -->

```bash
Collecting pycurl (from pyspider)
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/e8/e4/0dbb8735407189f00b33d84122b9be52c790c7c3b25286826f4e1bdb7bde/pycurl-7.43.0.2.tar.gz
    ERROR: Complete output from command python setup.py egg_info:
    ERROR: Using curl-config (libcurl 7.54.0)
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/private/var/folders/kz/8syfctw919zdt3shr9w5j8v00000gn/T/pip-install-h_pgkvxp/pycurl/setup.py", line 913, in <module>
        ext = get_extension(sys.argv, split_extension_source=split_extension_source)
      File "/private/var/folders/kz/8syfctw919zdt3shr9w5j8v00000gn/T/pip-install-h_pgkvxp/pycurl/setup.py", line 582, in get_extension
        ext_config = ExtensionConfiguration(argv)
      File "/private/var/folders/kz/8syfctw919zdt3shr9w5j8v00000gn/T/pip-install-h_pgkvxp/pycurl/setup.py", line 99, in __init__
        self.configure()
      File "/private/var/folders/kz/8syfctw919zdt3shr9w5j8v00000gn/T/pip-install-h_pgkvxp/pycurl/setup.py", line 316, in configure_unix
        specify the SSL backend manually.''')
    __main__.ConfigurationError: Curl is configured to use SSL, but we have not been able to determine which SSL backend it is using. Please see PycURL documentation for how to specify the SSL backend manually.
    ----------------------------------------
ERROR: Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/kz/8syfctw919zdt3shr9w5j8v00000gn/T/pip-install-h_pgkvxp/pycurl/
```

出错内容 `Curl is configured to use SSL, but we have not been able to determine which SSL backend it is using. Please see PycURL documentation for how to specify the SSL backend manually.`

原因在于正确配置配置 SSL，[官方文档](http://pycurl.io/docs/latest/install.html#easy-install-pip)中给出了方式

```bash
export PYCURL_SSL_LIBRARY=[openssl|gnutls|nss]
```

openssl 是比较常用的

```bash
export PYCURL_SSL_LIBRARY=openssl
```

如果你的 `.bash_profile` 文件中没有配置 `LDFLAGS` 和 `CPPFLAGS`，那需要在当前环境中进行激活。

```bash
$ export CFLAGS="-I$(brew --prefix openssl)/include"
$ export LDFLAGS="-L$(brew --prefix openssl)/lib"
```

`$(brew --prefix openssl)` 是为了获取 openssl 的安装目录，这是在使用 HomeBrew 安装的前提下，如果不是的话可以使用 `find` 命令进行查找

```bash
$ sudo find /usr -iname ssl.h
```

- [Curl is configured to use SSL, but we have not been able to determine which SSL backend it is using](https://stackoverflow.com/questions/51019622/curl-is-configured-to-use-ssl-but-we-have-not-been-able-to-determine-which-ssl)
- [Mac下安装pycurl填坑记录](https://www.jianshu.com/p/61fd0c16aef4)
