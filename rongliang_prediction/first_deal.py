#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse

origin_datafile = u'F:/data/所有的容量变更记录明细数据.xls'
after_change = u'F:/data/转化后的容量变更记录明细数据.xls'
total_data = pd.read_excel(origin_datafile,encoding='gbk')



if __name__ == '__main__':
    total_data = total_data.dropna()

    total_data[u'申请执行起日期'] = total_data[u'申请执行起日期'].map(lambda x: parse(str(x)).date().strftime('%Y%m%d'))
    total_data[u'申请执行月'] = total_data[u'申请执行起日期'].map(lambda x: parse(str(x)).date().strftime('%Y%m'))

    total_data.to_excel(after_change)

    # changed_data[changed_data[u'申请执行起日期'].isin(['201604','201605'])].to_excel(test_1)
    # changed_data[-changed_data[u'申请执行起日期'].isin(['201604', '201605'])].to_excel(train_1)


