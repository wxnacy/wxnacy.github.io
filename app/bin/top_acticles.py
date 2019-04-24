#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import records
from app.config import app
from app.models import VisitorLog
from app.models import Article

db = records.Database(app.config['SQLALCHEMY_DATABASE_URI'])

def print_top():
    sql = 'SELECT * from (select url, count(0) as c from visitor_log GROUP BY url) as vl order by vl.c desc;'
    rows = db.query(sql)    # or db.query_file('sqls/active-users.sql')
    print(rows)
    for r in rows[0:11]:
        #  print(r.url, r.c)
        a = Article.query_item(url = r.url)
        #  print(a.name)
        print(f'{a.name}: {r.url}')
    #  items = VisitorLog.query.all()
    #  print(len(items))
    #  res = {}
    #  for i in items:
        #  url = i.url
        #  if '?' in url:
            #  index = url.index('?')
            #  print(url)
            #  url = url[0:index]
            #  print(url)

        #  if '#' in url:
            #  index = url.index('#')
            #  print(url)
            #  url = url[0:index]
            #  print(url)

        #  if url not in res:
            #  res[url] = 0
        #  res[url] += 1

    #  print(len(res))
    #  articles = [dict(url = k, count = v) for k, v in res.items()]
    #  articles.sort(key = lambda x: x['count'], reverse=True)
    #  for a in articles[0:10]:
        #  print(a)

if __name__ == "__main__":
    print_top()
    pass

#  Python f-strings 3.6 版本新增加的字符串格式化功能: https://wxnacy.com/2018/01/16/python-f-strings/
#  Python APScheduler 定时任务: https://wxnacy.com/2018/01/23/python-apscheduler/
#  Vim 高级功能 vimgrep 全局搜索文件: https://wxnacy.com/2017/10/13/vim-grep/
#  Go 语法错误：Non-declaration statement outside function body: https://wxnacy.com/2018/08/16/go-syntax-error2/
#  办理北京工作居住证的一些细节: https://wxnacy.com/2018/02/11/beijing-xiaolvka/
#  Python 中调用 Javascript 代码: https://wxnacy.com/2018/02/02/pyexecjs/
#  JSON5 更舒服的 JSON 格式: https://wxnacy.com/2018/02/18/json5/
#  Vim 插件 tern_for_vim Javascript 自动补全: https://wxnacy.com/2017/09/22/vim-plugin-tern/
#  推荐几款获取当前 ip 的免费 api 接口: https://wxnacy.com/2017/12/22/ip-api/
#  Go 判断数组中是否包含某个 item: https://wxnacy.com/2018/11/20/go-in-array/
