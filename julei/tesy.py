#coding:utf-8
import pandas as pd
import numpy as np
from pandas import DataFrame


if __name__ == '__main__':
   bi = pd.read_excel("D:/data/TS_TAG.xlsx")
   df = bi.drop_duplicates(['userid'])
   j = ['rank','rongliang','importance','source','dianfei1','dianfei2','dianliang1','dianliang2','sanfang','current','protensial','timing']
   print df[j]
