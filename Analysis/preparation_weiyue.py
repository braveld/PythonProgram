#coding:utf-8
import pandas as pd
import numpy as np
from pandas import DataFrame

def count_wy_jilu():
    excel = pd.read_excel("D:/data/wy_jilu.xls")
    df = excel.drop_duplicates(['wy_type_code'])
    for i in sorted(df['wy_type_code']):
        print len(excel[excel['wy_type_code'].isin([i])])

if __name__ == '__main__':
   bi = pd.read_excel("D:/data/wy_jilu.xls")
   #df = bi.drop_duplicates(['userid'])

   print len(bi)



