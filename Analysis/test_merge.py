#coding:utf-8
import pandas as pd
import numpy as np
from pandas import DataFrame

if __name__ == '__main__':
    j = ['userid', 'yingshou', 'jine']
    excel = pd.read_excel("D:/jilu.xls")
    df = excel[j].drop_duplicates(['userid', 'yingshou'])
    userid = df['userid'].drop_duplicates()
    yingshou = df['yingshou'].drop_duplicates()
    data = DataFrame()
    print len(userid)