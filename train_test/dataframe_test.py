#-*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame,Series

if __name__ == '__main__':
    #Serices.prod(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
    # data = {'A':[0,1,1,1],'B':[1,0,1,0]}
    # dataframe = DataFrame(data)
    # print dataframe[['A','B']].prod(axis=1, numeric_only = True)



    data = {'A': [0, 1, 1, 1], 'B': [1, 0, 1, 0]}
    dataframe = DataFrame(data)
    d = dataframe[['A', 'B']].prod(axis=1, numeric_only=True)
    print d
    d_2 = DataFrame(d,index=['A---B']).T#这里会报错，Series转化为Dataframe必须是内容数超过来个的list，index必须也是list
    print d_2

    a = Series([1,0,1,0])
    b = Series([1,1,1,0])
    d_2 = DataFrame([a,b], index=['A---B','A---c']).T
    support_series_2 = 1.0 * d_2.sum() / len(d) #计算列中1的个数的占比，重点在Dataframe.sum()方法，为列元素相加
    print d_2
    print support_series_2