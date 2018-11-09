#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/9

# json 数据处理
from pprint import pprint
from urllib import request
import json

url = 'http://httpbin.org/get'
hds = {'User-Agent':'Test'}
# 构建Request对象
reqhd = request.Request(url=url, headers=hds)
# 发起请求
req = request.urlopen(reqhd)
content = req.read().decode('utf-8')
pprint(content)
# 转成字典
jdata = json.loads(content)
# 输出类型及对应字段值
print(type(jdata))
pprint(jdata)
pprint(jdata.get('headers').get('Host'))
pprint(jdata.get('origin'))