#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse

user_info_file = u'F:/data/用户基本信息.xls'
after_change = u'F:/data/转化后的500户容量变更记录明细数据.xls'
final = u'F:/data/测试容量变更记录明细数据.csv'
final_data = pd.read_csv(final,encoding='gbk')
if __name__ == '__main__':
    # after_change_data = pd.read_excel(after_change, encoding='gbk')
    # user_info = pd.read_excel(user_info_file, encoding='gbk')
    # grouped = after_change_data.groupby('CONS_NO')
    # group_date = after_change_data.groupby(u'申请执行月')
    # pieces = dict(list(grouped))
    # pieces_date = dict(list(group_date))
    final_data[u'是否变更'] = 0
    final_data.to_csv(final)


