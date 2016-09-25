#coding:utf-8
import pandas as pd
import numpy as np
from pandas import DataFrame


if __name__ == '__main__':
   bi = pd.read_excel("D:/data/train_set.xls")
   df = bi.drop_duplicates(['userid'])

   print len(df)
