---
title: Python 命令行参数模块 argparse
date: 2019-07-08 21:32:29
tags: [python]
---

Python 有很多处理命令行参数的外部模块，[click](https://github.com/pallets/click) 是其中的佼佼者，如果你是要完成一个稍微复杂点的项目，我也推荐使用它。但是如果编写一个独立的脚本，我认为方便简洁才是最重要的，也就是能用内置模块就用内置模块。此时了解相应功能的实现方式就尤为重要，何况 [argparse](https://docs.python.org/3/howto/argparse.html) 也真的没有想象中的那么难用。

<!-- more -->
<!-- toc -->

直接进入正题，基础用法如下

## 初始化

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# filename: demo.py

import argparse
parser = argparse.ArgumentParser(description='This is a argparse demo')
args = parser.parse_args()
```

```bash
$ python demo.py -h
usage: demo.py [-h]

This is a argparse demo

optional arguments:
  -h, --help  show this help message and exit
```

三行代码即可初始化一个命令行参数模块，默认有一个 `-h, --help` 参数显示帮助信息。

`ArgumentParser` 函数有如下参数:
- `prog` 程序的名字，默认是argv[0]。若设置，则在帮助信息中，可以使用%(prog)s来作为格式化的引用（修改一处全局受用）。
- `usage` 帮助信息的usage字段，描述程序的各种用法，默认情况下会依据add_argument()来自动生成。
- `description` 一个简单描述程序主要干啥以及怎么用的字符段，默认为空。
- `epilog` optional arguments字符段之后的字符段，默认为空。
- `parents` 继承的父parser，为了避免一些公共的内容重复定义，父parser在初始化时会设置add_help=False，这是为了防止出现父与子parser的-h冲突而抛出异常。
- `formatter_class` 对于help输出进行格式化，除了输出的样式外，如果设置为ArgumentDefaultsHelpFormatter，则会自动在help输出中添加已定义的default值。
- `prefix_chars` options前的字符，默认为'-'，可以添加其他字符，如'-+'，但是如果没有包括'-'，那么对应的option如'-h'就无法解析。
- `fromfile_prefix_chars` 有时会使用文件给parse_args()传入参数，为了能够识别文件字符串，如"demo.txt"，需要设置此值，如"@"，那么所有以此字符为开头的字符串都被当作是文件，所以传给parse_args()的参数应该是@demo.txt。在该文件中，一行只能有一个参数。如文件中的'-f\nbar'会被解析成['-f','bar']。
- `argument_default` 一般情况下，默认值使用add_argument()来添加，或者使用set_defaults()设置一些键值对来添加。剩下一种情况就是设置此项（此处没看明白是咋回事）。
- `conflict_handler` 解决在add_argument()阶段有冲突的option的依据策略，默认为error即抛出异常。一般情况下遇到冲突是抛出异常即可，但是如果设置了parents，那么需要重写父parser中的规则的时候，就需要将此项设置为resolve，但是重写是精确匹配的，如老规则定义了-h/--help，重写了-h，那么--help还是老规则。
- `add_help` 是否添加-h/--helpoption，默认为True。为False时，是要做parent（其实可以设置子Parser重写）。默认是-h/--help，若prefix_chars中没有包含'-'，那么就以其中第一个字符作为代替。

## 解析参数

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# filename: demo.py

import argparse
parser = argparse.ArgumentParser(description='This is a argparse demo')
parser.add_argument('file', help='List file or dir')
parser.add_argument('-u', '--user', help='Config user name')
args = parser.parse_args()
print(args.file)
print(args.user)
```

```bash
$ python demo.py bashrc -u wxnacy
bashrc
wxnacy
```

`add_argument` 函数有如下参数：
- `name or flags` 是位置参数，则需要传入名字；要是可选参数，则需要进行定义，如'-f'，'--foo'。

- `action` 定义传入的参数如何处理。
```
action='store'，默认取值，保存传入参数。
action='store_const'，需要添加const，意味着该argument的值不从命令行输入，而是取const的值。
action='store_true' or action='store_false'，'store_const'的特殊情形，意味着const的值为True或False。
action='append'，表示传入的值会作为一个列表的一项，意味着option可以在命令行中多次出现。
action='append_const'，传入列表的项由const定义，通常用在需要多个argument将值传入一个列表中的场景。
action='count'，输出argument出现的次数。
action='help'，已默认添加。
action='version'，需要定义version，使用时输出版本信息并退出。
自定义，通过定义一个argparse.Action子类来实现。实际上，上面的这些可选项都是通过这种形式定义的。    
```

- `nargs` ArgumentParser对象通常将一个动作与一个命令行参数关联。nargs关键字参数将一个动作与不同数目的命令行参数关联在一起：

```
nargs=N，一个选项后可以跟多个参数（action='append'时，依然是一个选项后跟一个参数，只不过选项可以多次出现），参数的个数必须为N的值，这些参数会生成一个列表，当nargs=1时，会生成一个长度为1的列表。
nargs=?，如果没有在命令行中出现对应的项，则给对应的项赋值为default。特殊的是，对于可选项，如果命令行中出现了此可选项，但是之后没有跟随赋值参数，则此时给此可选项并不是赋值default的值，而是赋值const的值。
nargs=* 位置参数 0 到多个
nargs=+ 位置参数 1 到多个
nargs=argparse.REMAINDER，所有剩余的参数，均转化为一个列表赋值给此项，通常用此方法来将剩余的参数传入另一个parser进行解析。如果nargs没有定义，则可传入参数的数量由action决定，通常情况下为一个，并且不会生成长度为一的列表。
```
- `const` 一种是定义action='store_const'或action='append_const'时使用。一种是定义nargs='?'时，可选项出现在命令行中，但之后并没有跟随赋值的参数，作为默认值传给此可选项。
- `default` 默认值。
    如果是一个字符串，那么Parser解析的时候会将它作为命令行传入值，使用type的值来进行转换类型，但是如果不是的话，就会使用定义的值而不进行类型转换。如果设置了nargs='?'或nargs=`*`，那么当没有参数赋值给该项时，会使用default定义的值。
而default=argparse.SUPPRESS时，则表示命令行中未出现某一项时，不会对它进行默认赋值。
- `type` 用于类型检查和类型转换。
    使用FileType可简化对文件的操作。还可以自定义函数，输入是一个字符串，输出是转换后的字符串。当设置choices的时，类型检查会变得容易，因为只需要在一个范围内比较即可。
- `choices` 给定了取值范围，超出会报错。
    当type也有定义时，会先使用type进行类型检查，所以choices中的取值必须符合type的定义，否则在parse_args()时会报错。任何支持in操作符的均可作为choices的赋值，所以字典，列表，集合，等等其他容器均都支持。
- `required` 默认情况下，可选项（前面有'-'）被认为并不一定需要出现在命令行参数中，但是如果设置了required=True的话，则必须出现。此类设置违背人的常识，应避免使用。
- `help` 帮助信息。
    之前提到的%(prog)s可用于此处程序名的格式化，此外，还有%(default)s格式化default的值，%(type)s格式化type的值。
设置为argparse.SUPPRESS可不显示帮助信息。
- `metavar` 在Parser生成帮助信息时，需要有字符代表需要传入的值。（这一段和dest相同，使用的就是dest的值）如果是位置参数，则用它本身代替；如果是可选参数，则使用它的大写来代替。使用metavar可替换默认的字符。
- `dest` 大部分的选项都需要通过命令行来给其赋值，这些值的名字通过dest来定义，默认的规则如同metavar中所述。

## 实际命令的例子

```python
# ls ~/Downloads ~/Documents
# 位置参数 0 或多个
parser.add_argument('files', nargs='*')
```

```python
# wget https://wxnacy.com
# 位置参数为必传
parser.add_argument('url', nargs=1)
```

```python
# wget https://wxnacy.com
# 位置参数为必传
parser.add_argument('url', nargs=1)
```

```python
# curl -X POST <url> -H 'Content-Type: application/json' -H 'Postman-Token: 0871758a-2782-4600-9d1f-e3da3270fd95'
# 可选参数可以叠加
parser.add_argument('-H', '--headers', action='append')
```

```python
# ls -a
# 可选参数为 bool 类型
parser.add_argument('-a', action='store_true')
```
