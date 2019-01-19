---
title: Python 实时翻译模块 googletrans
date: 2018-09-27 16:44:00
tags: [python]
---

Google 为 Python 提供了可以实时翻译的模块 googletrans，使用非常简单。

<!-- more --><!-- toc -->
## 下载

```bash
$ pip install googletrans
```

## 使用

**翻译英文**

```python
from googletrans import Translator

translate = Translator()
result = translate.translate('中国')
print(result.text)
# China
```

默认翻译为英文，也可以指定想要的语言

**翻译中文**

```bash
from googletrans import Translator

translate = Translator()
result = translate.translate('China', dest='zh-CN')
print(result.text)
# 中国
```

## 灵活使用

模块虽好，但也有不完善的地方，比如当有连字符的时候就有可能翻译不出来，比如

```bash
America/Argentina/Jujuy
```

这时候只能原样返回，但是用 Google 的翻译工具是可以出结果的，那只能想想办法，比
如把练习替换为空格

```python
result = translate.translate('America/Argentina/Jujuy'.replace("/", " "), dest='zh-CN')
# 美国阿根廷胡胡伊
```

这样就能得到想要的结果了

有一个问题，它是实时请求的 Google API，所以速度上不是很快，更适合一次性写入库的翻译操作。

可选的翻译种类有
```bash
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'ar': 'arabic',
    'be': 'belarusian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'zh-CN': 'chinese_simplified',
    'zh-TW': 'chinese_traditional',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'gl': 'galician',
    'de': 'german',
    'el': 'greek',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hu': 'hungarian',
    'is': 'icelandic',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'ko': 'korean',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'mk': 'macedonian',
    'ms': 'malay',
    'mt': 'maltese',
    'no': 'norwegian',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'ro': 'romanian',
    'ru': 'russian',
    'sr': 'serbian',
    'sk': 'slovak',
    'sl': 'slovenian',
    'es': 'spanish',
    'sw': 'swahili',
    'sv': 'swedish',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'yi': 'yiddish',
  }
```

- [Python 免费翻译API](https://blog.csdn.net/u010856630/article/details/75357991)
