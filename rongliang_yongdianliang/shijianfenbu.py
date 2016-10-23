#-*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt
after_change = u'F:/data/转化后的容量变更记录明细数据.xls'

data = pd.read_excel(after_change,encoding='gbk')
data = data[data[u'申请业务类型'] == 2]
d = pd.DataFrame()
grouped = data.groupby(u'申请执行月')
if __name__ == '__main__':
    s = data[u'申请执行月'].value_counts().sort_index()
    print s
    s.plot(kind = 'bar')
    for  x,y in zip(s.index,s):
        plt.text(x + 0.3, y + 0.05, '%.2f' % y, ha='center', va='bottom')

    plt.show()
    # for name,group in grouped:
    #     d[name] = group[u'申请业务类型'].value_counts()


