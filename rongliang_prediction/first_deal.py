#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse

origin_datafile = u'F:/data/2014年至2016年容量变更数据.xls'
after_change = u'F:/data/转化后的容量变更记录明细数据.xls'
total_data = pd.read_excel(origin_datafile,encoding='gbk')



if __name__ == '__main__':
    total_data = total_data.dropna()

    total_data[u'受理申请时间'] = total_data[u'受理申请时间'].map(lambda x: parse(str(x)).date().strftime('%Y%m%d'))
    total_data[u'申请执行月'] = total_data[u'受理申请时间'].map(lambda x: parse(str(x)).date().strftime('%Y%m'))
    deal = {u'高压增容': 1, u'减容': 2, u'减容恢复': 3, u'暂停': 4, u'暂停恢复': 5}
    total_data[u'申请业务类型'] = total_data[u'申请业务类型'].map(lambda x : deal[x])
    total_data.to_excel(after_change)

    # changed_data[changed_data[u'申请执行起日期'].isin(['201604','201605'])].to_excel(test_1)
    # changed_data[-changed_data[u'申请执行起日期'].isin(['201604', '201605'])].to_excel(train_1)


