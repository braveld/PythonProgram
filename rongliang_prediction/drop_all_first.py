#-*- coding: utf-8 -*-

import pandas as pd
total_f = u'F:/data/测试容量变更记录明细数据.csv'
total_t = u'F:/data/测试真的容量变更记录明细数据.csv'
total = u'F:/data/时间规律数据集.csv'
total_f_data = pd.read_csv(total_f)
total_t_data = pd.read_csv(total_t)

# if __name__ == '__main__':
