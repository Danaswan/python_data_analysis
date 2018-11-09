#!/usr/bin/python
# coding:utf-8
# Author : Dana
# createtime:2018/11/8

import csv

# 列名称
cols = ['mvname', 'score']

# 写入数据
data = [['肖申克救赎', '9.1'], ['大话西游', '9.0']]

with open('test.csv', 'w', encoding='utf-8') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(cols)
    fcsv.writerows(data)



