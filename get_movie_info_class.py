#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/7

from urllib import request
from bs4 import BeautifulSoup
from pprint import pprint
class DoubanDetailSpider(object):
    def __init__(self, headurl, fpath='mvinfo.txt'):
        self.headurl = headurl
        self.handler = open(fpath, 'w', encoding='utf-8')

    def requestPage(self, url):
        # 请求数据
        if url:
            # 添加异常处理
            try:
                req = request.urlopen(url)
                if req.code == 200:
                    content = req.read().decode('utf-8')
                    obj = BeautifulSoup(content, 'html5lib')
                    return obj
            except:
                print("Error Url", url)


    def startRequest(self,url=""):
        page = self.requestPage(url)
        if not page:
            return
        self.parsePage(page)
        # 获取下一页
        nextpageurl = self.getNextPage(page)
        if nextpageurl:
            self.startRequest(nextpageurl)


    def parsePage(self, page):
        # 解析电影列表方法， 获取电影详情页，海报地址，名称地址，评分，评分人数
        lista = page.select('div.item > div > a')
        for a in lista:
            url = a.get('href')
            img = a.find('img')
            name = img.get('alt')
            # 请求详情页，解析电影信息
            self.dealDetails(url, name)


    def dealDetails(self, url, mvname):
        # 处理详情页，请求详情页，
        obj = self.requestPage(url)
        if obj:
            # 解析详情页
            self.parseDetailPage(obj, mvname)


    def parseDetailPage(self, page, mvname):
        # 提取详情页信息
        div = page.find('div', id='info')
        info = div.text
        # 使用\n 切分
        tmp = info.split('\n')
        # 列表解析忽略空元素
        items = [s.strip() for s in tmp if len(s.strip())]
        tmp = [item.split(':', 1) for item in items]
        tmp = [item for item in tmp if len(item) == 2]

        result = dict(tmp)
        result['mvname'] = mvname
        result['score'] = page.find(property='v:average').text
        result['votes'] = page.find(property='v:votes').text
        self.saveData(result)

    def saveData(self, data):
        # 保存数据

        # 定义字符顺序
        keys = ['mvname', '导演', '主演', '类型', '制片国家/地区', '语言', '上映时间', '片长', '别名', 'score', 'votes']
        info = [data.get(key, '') for key in keys]
        self.handler.write(','.join(info))

    def getNextPage(self, page):
        # 获取下一页
        if page:
            tag = page.find(rel="next")
            if tag:
                urltail = tag.get('href')
                return self.headurl + urltail

    def close(self):
        self.handler.close()


if __name__ == '__main__':
    url = 'https://movie.douban.com/top250'
    spider = DoubanDetailSpider(url)
    spider.startRequest(url)
    spider.close()