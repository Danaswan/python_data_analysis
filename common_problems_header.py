#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/9

# 定制头信息

from urllib import request

url = 'http://httpbin.org/get'
req = request.urlopen(url)
#print(req.read().decode('utf-8'))


request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

# 设置请求头信息中 User-Agent
hds = {'User-Agent':'Test'}

# 构建Request对象
reqhd = request.Request(url = url, headers=hds)

# 发起请求
req = request.urlopen(reqhd)
#print(req.read().decode('utf-8'))


# 我们还可以通过Request 对象的add_header 添加更多信息

reqhd = request.Request(url=url,headers=hds)
# 添加信息
reqhd.add_header('Cookie', 'uid=test')
reqhd.add_header('Accept-Encoding', 'gzip,deflate,br')
# print(reqhd.headers)

