#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse
first_change_datafile = u'F:/data/第五次处理后的容量变更记录明细数据.csv'
new = u'F:/data/这次没有问题了.csv'
user_info_datafile = u'F:/data/用户基本信息.xls'
# first_change_data = pd.read_csv(first_change_datafile,encoding='gbk')
user_info = pd.read_excel(user_info_datafile)
def change(x):
    return int(str(x) + '01')

if __name__ == '__main__':
    # first_change_data = pd.merge(first_change_data,user_info,on='CONS_NO',how='left')
    # first_change_data.to_csv(first_change_datafile,encoding='gbk')
    # first_change_data.to_csv(new,encoding='gbk')
    first_change_data = pd.read_csv(new, encoding='gbk')
    new_data = first_change_data[first_change_data[u'是否容量变更'] == 0]
    new_data = new_data.drop_duplicates([u'CONS_NO',u'申请执行月'])
    new_data[u'申请业务类型'] = 0
    new_data.to_csv(new,encoding='gbk')