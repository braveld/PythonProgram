#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse


last = u'F:/data/新的最终样本集.csv'

if __name__ == '__main__':
    origin_data = pd.read_csv(last,encoding='gbk')