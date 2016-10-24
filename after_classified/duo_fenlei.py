#-*- coding: utf-8 -*-

import pandas as pd #导入数据分析库

quchu = u'F:/data/去除第一次样本集.csv'
zengrong = u'F:/data/1.csv'
jianrong = u'F:/data/2.csv'
jianronghuifu = u'F:/data/3.csv'
zanting = u'F:/data/4.csv'
zantinghuifu = u'F:/data/5.csv'
new = u'F:/data/1_0.csv'
data = pd.read_csv(zanting,encoding='gbk') #读取数据，数据的前三列是特征，第四列是标签

if __name__ == '__main__':
    data = data[data[u'是否容量变更'] == 0]
    data[u'申请业务类型'] = 0
    data.to_csv(new,encoding='gbk')
