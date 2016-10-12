#-*- coding: utf-8 -*-

import pandas as pd

total = u'F:/data/测试容量变更记录明细数据.csv'
train = u'F:/data/train.csv'
test = u'F:/data/test.csv'
if __name__ == '__main__':
    total_data = pd.read_csv(total, encoding='gbk')
    total_data = total_data[-total_data[u'申请业务类型'].isin([1])]
    total_data = total_data[-total_data[u'申请执行月'].isin([20130501,20130601,20130701,20130801,20130901,20131001,20131101,20131201,20140101,20140201])]

    total_data = total_data[-total_data[u'申请执行月'].isin([20160401, 20160501])]

    total_data.to_csv(train,encoding='gbk')
    total_data = total_data[total_data[u'申请执行月'].isin([20160401, 20160501])]
    total_data.to_csv(test,encoding='gbk')