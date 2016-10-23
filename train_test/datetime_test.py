#-*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime
from dateutil.parser import parse
from datetime import datetime,timedelta
total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/01--30个月每月用电量、电费.csv'

new = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/明细数据/聚合的去除0所有的容量变更记录明细数据.xls'
tmp_datafile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/明细数据/data.xls'
new_datafile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/明细数据/去除0所有的容量变更记录明细数据.xls'
# total_data = pd.read_csv(total,encoding='gbk')
final = u'F:/data/测试容量变更记录明细数据.csv'
if __name__ == '__main__':
    # date1 = parse('01/04/2014 15:44:16',dayfirst = True)
    # date2 = parse('20140401')
    # print date1
    # print date2
    # print date1.date().__eq__(date2)
    # print date2.strftime('%Y%m%d')
    # print date1.date().strftime('%Y%m%d')
    # print date1.date().strftime('%Y%m')

    # origin_data = pd.read_excel(new_datafile, encoding='gbk')

    # date1 = parse('20091203')
    # date2 = parse('20160101')
    #
    # print (date2 - date1).days

    # final_data = pd.read_csv(final)
    # data = {'date':[20160101,20160201],'userno':[1,2]}
    # data = pd.DataFrame(data)
    # data['date'] = pd.to_datetime(data['date'],format='%Y%m%d')


    #时间差
    date1 = parse('20170731')
    date2 = date1 - timedelta(183)
    print date2