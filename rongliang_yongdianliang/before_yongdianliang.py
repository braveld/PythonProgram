#-*- coding: utf-8 -*-

import pandas as pd
origin_datafile = u'F:/data/最终样本集.csv'
third = u'F:/data/新的最终样本集.csv'
origin_data = pd.read_csv(origin_datafile,encoding='gbk')

if __name__ == '__main__':
    list = [u'前六个月',u'前五个月',u'前四个月',u'前三个月',u'前二个月',u'前一个月']
    new_data = origin_data[list]
    new = new_data.T
    origin_data['min'] = new.min()
    origin_data['max'] = new.max()
    origin_data[u'前一个月增长率'] = (origin_data[u'前一个月'] - origin_data[u'前二个月']) * 100 / (origin_data[u'前二个月'] + 0.1)
    origin_data[u'前二个月增长率'] = (origin_data[u'前二个月'] - origin_data[u'前三个月']) * 100 / (origin_data[u'前三个月'] + 0.1)
    origin_data[u'前三个月增长率'] = (origin_data[u'前三个月'] - origin_data[u'前四个月']) * 100 / (origin_data[u'前四个月'] + 0.1)
    origin_data[u'前四个月增长率'] = (origin_data[u'前四个月'] - origin_data[u'前五个月']) * 100 / (origin_data[u'前五个月'] + 0.1)
    origin_data[u'前五个月增长率'] = (origin_data[u'前五个月'] - origin_data[u'前六个月']) * 100 / (origin_data[u'前六个月'] + 0.1)
    count = []
    mean_list = origin_data['mean'].tolist()
    data_matrix = new_data.as_matrix()
    for i in range(len(data_matrix)):
        p = 0
        for j in range(6):
            if data_matrix[i][j] > mean_list[i]:
                p = p + 1
        count.append(p)
    origin_data[u'增长趋势'] = pd.Series(count)
    origin_data.to_csv(third,encoding='gbk')




