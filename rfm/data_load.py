#-*- coding: utf-8 -*-
#K-Means聚类算法

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import time
import datetime
from sklearn.cluster import KMeans #导入K均值聚类算法

inputfile = '/home/rh/Downloads/jilu.xls' #待聚类的数据文件

#读取数据并进行聚类分析
data = pd.read_excel(inputfile) #读取数据
data1 = data.drop_duplicates(['userid','yingshou'])[['userid','yingshou','jine']]

shijian = [201405, 201406, 201407, 201408, 201409, 201410, 201411, 201412, 201501, 201502,201503,201504]

data2 = data1[data1['yingshou'].isin(shijian)]
data3 = data[data['yingshou'].isin(shijian)]

total = data2.groupby(['userid']).sum()
total['userid']=total.index
size = data.groupby(['userid']).size()
total['F']=size
total['M']=total['jine']
s = '20150501'
a = time.strptime(s,'%Y%m%d')
a_datetime=datetime.datetime(*a[:3])

u = []
j = []
for userid,group in data3.groupby('userid'):
    k = []
    for i in group['shishouriqi']:
        b = time.strptime(str(i), '%Y%m%d')
        b_date = datetime.datetime(*b[:3])
        p = (a_datetime - b_date).days
        k.append(p)
    j.append(min(k))
    u.append(userid)
total['R'] = Series(j,index=u)
total[['R','F','M']].to_csv('/home/rh/Downloads/rfm.csv')
