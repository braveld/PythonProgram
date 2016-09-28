# -*- coding: utf-8 -*-
from numpy import *
import pandas as pd

if __name__ == '__main__':
    a = matrix([['A1', 'B2', 'C3'], ['A2', 'B1', 'C2']])
    # print a
    ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数,
    b = map(ct, [['A1', 'B2', 'C3']])  # 用map方式执行
    data = pd.DataFrame(b).fillna(0)
    print data
