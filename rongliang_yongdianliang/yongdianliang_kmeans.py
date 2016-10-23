#-*- coding: utf-8 -*-

import pandas as pd
new_yongdianlaing_datafile = u'F:/data/新的每月用电量.csv'
new = u'F:/data/用电模式.csv'
yongdian_data = pd.read_csv(new_yongdianlaing_datafile,encoding='gbk')

if __name__ == '__main__':
    grouped = yongdian_data.groupby('CONS_NO')
    d = {}
    users = []
    for name,group in grouped:
        users.append(name)
        data = group[u'总电量'].tolist()
        d[name] = data
    old = pd.DataFrame(d)
    total = pd.DataFrame(d).T

    total.columns = [201401,201402,201403,201404,201405,201406,201407, 201408, 201409, 201410, 201411, 201412, 201501, 201502, 201503, 201504, 201505, 201506, 201507, 201508,
         201509, 201510, 201511, 201512,
         201601, 201602, 201603, 201604, 201605, 201606]
    total['total'] = old.sum()
    total['mean'] = old.mean()
    total[u'方差'] = old.var()
    total[u'中位数'] = old.median()
    total.to_csv(new,encoding='gbk')