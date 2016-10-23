#-*- coding: utf-8 -*-

import pandas as pd
from matplotlib import pyplot as plt
after_change = u'F:/data/转化后的容量变更记录明细数据.xls'
data = pd.read_excel(after_change,encoding='gbk')

if __name__ == '__main__':
    data[u'申请业务类型'].value_counts().sort_index().plot(kind='bar')
    plt.show()