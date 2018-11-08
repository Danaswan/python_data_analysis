#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/7

# 获取电影详情页
# a 电影名称，导演，主演，编辑，类型，国家，语言
# b 上映时间，片名，别人，评分，评分人数


from bs4 import BeautifulSoup
from urllib import request

url = 'https://movie.douban.com/top250'
req = request.urlopen(url)
content = req.read().decode('utf-8')

# create BeautifulSoup
obj = BeautifulSoup(content, 'html5lib')
# get all item
items = obj.select('div.item')

# get movie's name and movie detail
detailInfo = []
for item in items:
    lists = []
    pic = item.select_one('.pic')
    name = pic.img['alt']
    detailUrl = pic.a['href']
    img = pic.img['src']


detailUrl = 'https://movie.douban.com/subject/1292052/'

infoReq = request.urlopen(detailUrl)
contentDetail = infoReq.read().decode('utf-8')
objE = BeautifulSoup(contentDetail, 'html5lib')
div = objE.find('div', id='info')
# 提取导演
direct = div.find('a', rel='v:directedBy')

info = div.text
print(info)

# 使用\n 切分
tmp = info.split('\n')
#print(tmp)
# 列表解析忽略空元素
items = [s.strip() for s in tmp if len(s.strip())]
#print(items)
# 按冒号切分
tmp = [item.split(':') for item in items]
#print(tmp)
# 换成字典
result = dict(tmp)
#print(result)

#result = dict(tmps)
#print(result)






