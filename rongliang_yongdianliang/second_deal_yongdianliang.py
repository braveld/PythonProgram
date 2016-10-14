#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse
from datetime import datetime,timedelta
new_yongdianlaing_datafile = u'F:/data/新的每月用电量.csv'
first_change_datafile = u'F:/data/第一次处理后的容量变更记录明细数据.xls'

yongdianliang_data = pd.read_csv(new_yongdianlaing_datafile,encoding='gbk')
first_change_data = pd.read_excel(first_change_datafile)

if __name__ == '__main__':
    date_list = first_change_data[u'申请执行起日期'].tolist()
    user_list = first_change_data[u'CONS_NO'].tolist()
    y_user_list = yongdianliang_data[u'CONS_NO'].tolist()
    user_list = [val for val in user_list if val in y_user_list]
    first_change_data = first_change_data[first_change_data['CONS_NO'].isin(user_list)]
    grouped = yongdianliang_data.groupby('CONS_NO')
    pieces = dict(list(grouped))
    row = []
    columns = []
    for i in range(len(user_list)):
        start = parse(str(date_list[i])) - timedelta(180)
        start = int(start.strftime('%Y%m'))
        d = pieces[user_list[i]]
        row = d[start <= d[u'年月']][d[u'年月'] <= date_list[i]][u'总电量'].tolist()
        # print len(row)
        columns.append(row)
    print columns
    # first_change_data[u'前六个月'] = pd.Series(columns[:,1])
    # first_change_data[u'前五个月'] = pd.Series(columns[:, 2])
    # first_change_data[u'前四个月'] = pd.Series(columns[:, 3])
    # first_change_data[u'前三个月'] = pd.Series(columns[:, 4])
    # first_change_data[u'前二个月'] = pd.Series(columns[:, 5])
    # first_change_data[u'前一个月'] = pd.Series(columns[:, 6])
    # print first_change_data
