#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/8

# 关键字搜索 如在github 搜索python


from urllib import request
from urllib import parse
from bs4 import BeautifulSoup

# keyword
keywords = ['java', 'php', 'python']


urlhead = 'https://github.com/search?q='

for s in keywords:
    url = urlhead + s
    req = request.urlopen(url)
    print('search %s, code %d' %(s, req.code))


kw = '区块链'
kws = parse.urlencode({'q':kw})
print(kws)

url = 'https://github.com/search?' + kws
req = request.urlopen(url)
print('search %s, code %d' % (kw, req.code))


