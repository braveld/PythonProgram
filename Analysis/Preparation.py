#coding:utf-8
import pandas as pd
import numpy as np
from pandas import DataFrame

#arrange the payment data into the suitable format group by data
#userid,201406,201407,201408,......,201605
if __name__ == '__main__':
    j = ['userid','yingshou','jine']
    excel = pd.read_excel("D:/data/jilu.xls")
    df = excel[j].drop_duplicates(['userid','yingshou'])
    userid = df['userid'].drop_duplicates()
    yingshou = df['yingshou'].drop_duplicates()
    data = DataFrame()
    for i in userid:
        alist = [i]
        t = df[df['userid'].isin(alist)][['yingshou', 'jine']]
        t.columns = ['yingshou', i]
        if len(t) == 25:
            if len(data) == 0:
                data = t
            else:
                data = pd.merge(data,t,how='left')
    change = data.T
    change.to_csv("D:/change.csv")














