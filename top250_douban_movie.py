#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/6


from pprint import pprint

from urllib import request
import re
url = 'https://movie.douban.com/top250'

req = request.urlopen(url)

content = req.read().decode('utf-8') # get all content

# () 代表分组 .* 代表匹配前面单字符任意次 贪婪模式  .*? 是满足条件的情况只匹配一次 非贪婪模式
# 得到电影名称和海报地址的元组
list = re.findall(r'<img.*alt="(.*?)".*?src="(.*?)"', content)

# 接下来根据海报地址下载并保存文件
# for x in list:
#     imgObj = request.urlopen(x[1])
#     img = imgObj.read()
#     f = open('move.ipg', 'wb')
#     f.write(img)
#     f.close()
pprint(list)


# 查找下一页，
nextPage = re.findall(r'<link rel="next" href="(.*?)"', content)

# url 拼接再次请求
#nextUrl = url + nextPage
