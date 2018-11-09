#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/8

# 获取 https://www.cnblogs.com/ 博客园  的 推荐博客排行

from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.cnblogs.com/aggsite/UserStats'
page = request.urlopen(url)
try:
    if page.code == 200:
        content = page.read().decode('utf-8')
        #print(content)
        obj = BeautifulSoup(content, 'html5lib')
        div = obj.find('div', id='blogger_list')
        listli = div.findAll('li')
        for li in listli:
            if '.' in li.text:
                print(li.text)
        # print(div)
except:
    print("Error url"), url