#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse

datafile = u'/home/bigdata/Downloads/data/data/测试容量变更记录明细数据.csv' #需要进行标准化的数据文件；
final_data = pd.read_csv(datafile,encoding='utf8')
if __name__ == '__main__':
    final_data[u'距上一次暂停时长'] = -final_data[u'距上一次暂停时长']
    final_data[u'距上一次暂停恢复时长'] = -final_data[u'距上一次暂停恢复时长']
    final_data[u'距上一次减容恢复时长'] = -final_data[u'距上一次减容恢复时长']
    final_data[u'距上一次减容时长'] = -final_data[u'距上一次减容时长']
    print final_data
    # final_data.to_csv(datafile,encoding='gbk')

