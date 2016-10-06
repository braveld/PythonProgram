#-*- coding: utf-8 -*-

import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法

if __name__ == '__main__':
    datafile = '/home/bigdata/Downloads/data/'+'哈'+'.xls'#

    datafile = unicode(datafile,"utf8")

    data = pd.read_excel(datafile,encoding='gbk')  # 读取数据

    print data.columns#