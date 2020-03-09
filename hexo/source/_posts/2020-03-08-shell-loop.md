---
title: Shell 语言中的循环语句
date: 2020-03-08 09:30:15
tags: [shell]
---

总结几种 Shell 语言中可以用到的循环语句

<!-- more -->
<!-- toc -->

## for

### 数字循环

简单数字循环

```bash
#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

# function 1
# lists="1 2 3 4 5"
# for var in $lists

# function 2
# for var in 1 2 3 4 5

# function 3
for var in {1..5}
do
    echo $var
done
```

命令行使用方式

```bash
$ for var in {1..5};do;echo $var; done
```

**使用 seq**

```bash
#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

for var in $(seq 1 10)
do
     echo $var
done
```

使用 2 作为步长

```bash
#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

for var in $(seq 1 2 10)
do
     echo $var
done
```

**使用 c 语言的方式**

```bash
#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

for ((var=1; var<=5; var ++))
do
     echo $var
done
```

## while

```bash
#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

i=1

while(( i <= 10 ))
do
     let "i+=1"
done
```
