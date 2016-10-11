#-*- coding: utf-8 -*-

import pandas as pd
import os
from datetime import datetime
from dateutil.parser import parse

origin_datafile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/明细数据/所有的容量变更记录明细数据.xls'

new_datafile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/明细数据/去除0所有的容量变更记录明细数据.xls'

new = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/明细数据/test.xls'



if __name__ == '__main__':
    origin_data = pd.read_excel(new_datafile,encoding='gbk')
    origin_data[u'申请执行起日期'] = origin_data[u'申请执行起日期'].map(lambda x: parse(str(x)).date().strftime('%Y%m%d'))
    grouped = origin_data.groupby('CONS_NO')
    for name,group in grouped:
        print name







