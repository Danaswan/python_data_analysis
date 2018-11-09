#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/9

from urllib import request
from urllib import parse

url = 'http://httpbin.org/post'
pdata = 'test'

req = request.urlopen(url, data=pdata.encode('utf-8'))
#print(req.read().decode('utf-8'))


import json
data = {'uame':'dana', 'passwd':'test123'}
pdata = parse.urlencode(data).encode('utf-8')
req = request.urlopen(url, data=pdata)
print(req.read().decode('utf-8'))