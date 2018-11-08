#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/7

from bs4 import BeautifulSoup
from urllib import request
url = 'https://movie.douban.com/top250'
req = request.urlopen(url)
content = req.read().decode('utf-8')

# 创建beautifulsoup 对象
# 抓取内容创建beautifulsoup对象,使用html5lib方式进行解析
# pip install html5lib

obj = BeautifulSoup(content, 'html5lib')
# BeautifulSoup将HTML文档转换成一个复杂的树形结构，每个标题都是一个节点，每个节点视为一个Tag对象
#print(obj)
print(type(obj.title))  # <class 'bs4.element.Tag'>
a = obj.a
print(a)
# 一个tag可能有很多个属性

print(a.attrs)
# {'href': 'https://www.douban.com/accounts/login?source=movie', 'class': ['nav-login'], 'rel': ['nofollow']}

print(a['rel'])
# ['nofollow']
print(a.get('href'))
# https://www.douban.com/accounts/login?source=movie
print(a.string)
print(a.text)


"""
find and findAll 的使用
"""
item = obj.find('div', class_='item')
div = item.find('div', class_='star')
score = div.find('span', class_='rating_num')
print(div)
"""
<div class="star">
    <span class="rating5-t"></span>
    <span class="rating_num" property="v:average">9.6</span>
    <span content="10.0" property="v:best"></span>
    <span>1185949人评价</span>
</div>

"""
# 如何得到评价人数
# 目的找到不带有任何属性的span节点
print(not div.attrs) # false 说明有属性
# 定义匿名函数，判断是否存在任何属性

has_attr = lambda tag: not tag.attrs
voters = div.find(has_attr)
voters.text
score.text

# 获取所有div
text = div.text
# 列表解析，字符串切分，过滤掉空白字符
info = [ s for s in text.split() if len(s.strip())]

list(div.stripped_strings)


# 我们如何获取这个页面的所有电影名称，海报地址，评分与评分人数？
# we can use findAll()
# get all <div class='items'>
items = obj.findAll('div', class_='item')
# 遍历查找结果
for item in items:
    # 获取详情页url
    detailUrl = item.a.get('href')
    # 获取电影名称
    name = item.img.get('alt')
    # 获取电影海报diz
    posterurl = item.img.get('src')
    # 获取评分与评分人数
    div = item.find('div', class_='star')
    score, voters = list(div.stripped_strings)
    #print(name, score, voters, detailUrl, posterurl)

# 查找下一页
nextlink = obj.find('link', rel='next')
# 提取下一页地址
# print(nextlink.get('href'))

"""
select() and select_one() 的使用
"""

# 查找div的节点
items = obj.select('div.item')
for item in items:
    # 查找第一个div下的第一个a节点
    a = item.select_one('> div > a')
    # 获取详情ye
    detailUrl = a.get('href')
    # 查找img节点
    img = a.select_one('img')
    # 获取名字与海报地址
    name = img.get('alt')
    posterurl = img.get('src')
    # 获取评分与评分人数
    star = item.select_one('.star')
    score, voters = list(star.stripped_strings)
    print(name, score, voters, detailUrl, posterurl)

