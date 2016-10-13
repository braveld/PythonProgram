#-*- coding: utf-8 -*-

import pandas as pd

total = u'F:/data/测试容量变更记录明细数据.csv'

if __name__ == '__main__':
    total_data = pd.read_csv(total, encoding='gbk')