#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse

origin_datafile = u'F:/data/01--30个月每月用电量、电费.csv'
all_rongliang_datafile = u'F:/data/2014年至2016年容量变更数据.xls'
first_change_datafile = u'F:/data/第一次处理后的容量变更记录明细数据.xls'
rl_count_datafile = u'F:/data/容量变更次数.xls'
new_yongdianlaing_datafile = u'F:/data/新的每月用电量.csv'

dates = [201407, 201408, 201409, 201410, 201411, 201412, 201501, 201502, 201503, 201504, 201505, 201506, 201507, 201508,
         201509, 201510, 201511, 201512,
         201601, 201602, 201603, 201604, 201605, 201606]
origin_data = pd.read_csv(origin_datafile,encoding='gbk')
del origin_data[u'总电费']
origin_data = origin_data[origin_data[u'总电量'] != 0]
all_rongliang_data = pd.read_excel(all_rongliang_datafile,encoding='gbk')

if __name__ == '__main__':
    all_rongliang_data = all_rongliang_data.dropna()#去除空值

    #进行日期转换
    all_rongliang_data[u'申请执行起日期'] = all_rongliang_data[u'受理申请时间'].map(lambda x: parse(str(x)).date().strftime('%Y%m%d'))
    all_rongliang_data[u'申请执行月'] = all_rongliang_data[u'受理申请时间'].map(lambda x: parse(str(x)).date().strftime('%Y%m'))
    all_rongliang_data = all_rongliang_data[all_rongliang_data[u'申请执行月'] > 201407]#选择2014年7月之后的数据
    deal = {u'高压增容':1,u'减容':2,u'减容恢复':3,u'暂停':4,u'暂停恢复':5}
    all_rongliang_data[u'申请业务类型'] = all_rongliang_data[u'申请业务类型'].map(lambda x : deal[x])
    del all_rongliang_data[u'受理申请时间']


    grouped = origin_data.groupby('CONS_NO')

    rongliang_count = []
    users = []
    for name,group in grouped:
        g_size = group['CONS_NO'].size
        if g_size > 20:
            users.append(name)
            rongliang_count.append(g_size)
    rongliang_biangeng_cishu = {'CONS_NO':users,'count':rongliang_count}
    rongliang_biangeng_cishu = pd.DataFrame(rongliang_biangeng_cishu)
    rongliang_biangeng_cishu.to_excel(rl_count_datafile)
    print len(users)
    new_user = []#存储用户编号
    new_dates = [201401,201402,201403,201404,201405,201406,201407, 201408, 201409, 201410, 201411, 201412, 201501, 201502, 201503, 201504, 201505, 201506, 201507, 201508,
         201509, 201510, 201511, 201512,
         201601, 201602, 201603, 201604, 201605, 201606]
    store_date = []
    for j in users:
        for k in new_dates:
            new_user.append(j)
            store_date.append(k)

    change_data = {'CONS_NO':new_user,u'年月':store_date}
    change_data = pd.DataFrame(change_data)
    change_data = pd.merge(change_data,origin_data,on=[u'CONS_NO',u'年月'],how='left')
    change_data = change_data.fillna(0)
    # change_data = change_data[change_data['CONS_NO'].isin(users)]
    change_data.to_csv(new_yongdianlaing_datafile,encoding='gbk')
    all_rongliang_data.to_excel(first_change_datafile)

