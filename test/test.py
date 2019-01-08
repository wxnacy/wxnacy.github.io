#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:


#  from googletrans import Translator
#  translate = Translator()
#  result = translate.translate('America Argentina Jujuy', dest='zh-CN')
#  print(result.text)


from pytz import timezone
from datetime import datetime
tz = timezone("America/New_York")
res = datetime.now(tz).utcoffset().total_seconds()/60/60
print(res)


