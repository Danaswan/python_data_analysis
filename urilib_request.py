#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/6

from pprint import pprint
from urllib import request
url = 'http://httpbin.org/get'
req = request.urlopen(url)


pprint(req.code)
pprint(req.getheaders())
pprint(req.read())


