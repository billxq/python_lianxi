#!/usr/bin/env python
# coding:utf-8
"""
从 GitHub 上选出符合这些条件的项目： 
1. 最近一周内发布的 
2. Star 数大于 200 
3. topic 是 crawler
找到后发送邮件
利用github的api接口进行查询：https://api.github.com/search/repositories?q=
"""

import time
import datetime
a = datetime.datetime.now()-datetime.timedelta(days=7)
print(a)