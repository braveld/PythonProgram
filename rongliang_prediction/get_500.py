#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse

new_500 = u'F:/data/转化后的500户容量变更记录明细数据.xls'
after_change = u'F:/data/转化后的容量变更记录明细数据.xls'
after_change_data = pd.read_excel(after_change,encoding='gbk')

if __name__ == '__main__':

    grouped = after_change_data.groupby('CONS_NO')

    # a = []
    # b = 0
    # for name, group in grouped:
    #     b = b + 1
    #     if b < 500:
    #         a.append(name)
    #     else:
    #         break
    # after_change_data[after_change_data['CONS_NO'].isin(a)].to_excel(new_500)

    a = 0
    for name, group in grouped:
        a = a + 1
    print a

