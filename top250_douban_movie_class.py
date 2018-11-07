#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/6

from urllib import request
import re, os
class PostSpider(object):
    def __init__(self, url, path='./'):
        self.path = path
        self.url = url

    def start(self, url):
        # 入口函数
        page = (self.reqPage(url)).decode('utf-8')
        mvInfo = self.getMvInfo(page)

        for mvname, mvurl in mvInfo:
            self.save2Img(mvname, mvurl)
        nexturl = self.getNextPage(page)
        if nexturl:
            self.start(nexturl)

    def reqPage(self, url):
        # 请求数据
        if url:
            req = request.urlopen(url)
            if req.code == 200:
                return req.read()

    def getMvInfo(self, page):
        # 提取信息， 返回电影名称与海报
        if page:
            listinfo = re.findall(r'<img.*alt="(.*?)".*?src="(.*?)"', page)
            return listinfo
        return []

    def getNextPage(self, page):
        # 获取下一页
        if page:
            nexturl = re.findall(r'<link rel="next" href="(.*?)"', page)
            print(nexturl)
            if nexturl :
                return self.url + nexturl[0]

    def save2Img(self, fname, url):
        # 保存图片
        img = self.reqPage(url)
        # 文件名与后缀
        fname = fname + '.' + url.rsplit('.', 1)[-1]
        # 文件路径
        fpath = os.path.join(self.path, fname)
        # 保存图片
        with open(fpath, 'wb') as f:
            f.write(img)



if __name__ == '__main__':
    url = 'https://movie.douban.com/top250'
    spider = PostSpider(url,'img')
    spider.start(url)