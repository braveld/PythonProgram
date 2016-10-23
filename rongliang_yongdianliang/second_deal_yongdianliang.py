#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse

new_yongdianlaing_datafile = u'F:/data/新的每月用电量.csv'
# first_change_datafile = u'F:/data/第一次处理后的容量变更记录明细数据.xls'
first_change_datafile = u'F:/data/最终样本集.csv'
second_change_datafile = u'F:/data/最终样本集用电量.csv'
yongdianliang_data = pd.read_csv(new_yongdianlaing_datafile,encoding='gbk')
# l = yongdianliang_data['CONS_NO'].tolist()
first_change_data = pd.read_csv(first_change_datafile,encoding='gbk')
# first_change_data = first_change_data[first_change_data['CONS_NO'].isin(l)]

# first_change_data.to_csv(first_change_datafile,encoding='gbk')
if __name__ == '__main__':
    date_list = first_change_data[u'受理申请时间'].tolist()
    user_list = first_change_data[u'CONS_NO'].tolist()
    grouped = yongdianliang_data.groupby('CONS_NO')
    pieces = dict(list(grouped))
    row = []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    dates = []
    for i in range(len(user_list)):
        print i
        print date_list[i]
        end = int(parse(str(int(date_list[i]))).strftime('%Y%m'))
        end_m = int(parse(str(int(date_list[i]))).strftime('%m'))
        end_y = int(parse(str(int(date_list[i]))).strftime('%Y'))
        start = end - 6
        if end_m <= 6:
            start = (end_y - 1) * 100 + 12 + end_m - 6
        d = pieces[user_list[i]]
        dates.append(date_list[i])
        row = d[start <= d[u'年月']][d[u'年月'] < end][u'总电量'].tolist()#很有可能会出现不止6个月的现象
        row1.append(row[0])
        row2.append(row[1])
        row3.append(row[2])
        row4.append(row[3])
        row5.append(row[4])
        row6.append(row[5])
    # columns = {u'前六个月':row1,u'前五个月':row2,u'前四个月':row3,u'前三个月':row4,u'前二个月':row5,u'前一个月':row6,u'受理申请时间':date_list,u'CONS_NO':user_list}
    # data = pd.DataFrame(columns)
    # first_change_data = pd.merge(first_change_data,data,on=[u'CONS_NO',u'受理申请时间'],how='left')
    first_change_data[u'前六个月'] = pd.Series(row1)
    first_change_data[u'前五个月'] = pd.Series(row2)
    first_change_data[u'前四个月'] = pd.Series(row3)
    first_change_data[u'前三个月'] = pd.Series(row4)
    first_change_data[u'前二个月'] = pd.Series(row5)
    first_change_data[u'前一个月'] = pd.Series(row6)
    first_change_data.to_csv(second_change_datafile,encoding='gbk')
