#-*- coding: utf-8 -*-

import pandas as pd
origin_datafile = u'F:/data/第五次处理后的容量变更记录明细数据.csv'
new = u'F:/data/全部的去除了第一次的数据.csv'
origin_data = pd.read_csv(origin_datafile,encoding='gbk')

if __name__ == '__main__':
    origin_data = origin_data[origin_data[u'距上一次暂停时长'] + origin_data[u'距上一次暂停恢复时长'] + origin_data[u'距上一次减容恢复时长'] + origin_data[u'距上一次减容时长'] != 0]
    origin_data.to_csv(new,encoding='gbk')
    # print origin_data[u'距上一次暂停时长'] + origin_data[u'距上一次暂停恢复时长'] + origin_data[u'距上一次减容恢复时长'] + origin_data[u'距上一次减容时长'] == 0
