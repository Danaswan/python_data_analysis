#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/9

from urllib import parse, request

url = 'https://www.so.com/s?'
kws = {'ie':'utf-8', 'fr':'none', 'q':'区块链', 'src':'home_none'}

# 参数转url
urlkws = parse.urlencode(kws)

# url 拼接
url = url + urlkws
print(url)
req = request.urlopen(url)
print(req.read().decode('utf-8'))
