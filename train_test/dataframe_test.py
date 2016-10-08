#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import random

# def fanhui():
#     data = DataFrame({'key': ['a', 'b', 'c'], 'value1': [1, 2, 3]})
#     return data



if __name__ == '__main__':
    #Serices.prod(self, axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
    # data = {'A':[0,1,1,1],'B':[1,0,1,0]}
    # dataframe = DataFrame(data)
    # print dataframe[['A','B']].prod(axis=1, numeric_only = True)


    #pandas.Series与pandas.Dataframe的转化
    # data = {'A': [0, 1, 1, 1], 'B': [1, 0, 1, 0]}
    # dataframe = DataFrame(data)
    # d = dataframe[['A', 'B']].prod(axis=1, numeric_only=True)
    # print d
    # d_2 = DataFrame(d,index=['A---B']).T#这里会报错，Series转化为Dataframe必须是内容数超过来个的list，index必须也是list
    # print d_2
    #
    # a = Series([1,0,1,0])
    # b = Series([1,1,1,0])
    # d_2 = DataFrame([a,b], index=['A---B','A---c']).T
    # support_series_2 = 1.0 * d_2.sum() / len(d) #计算列中1的个数的占比，重点在Dataframe.sum()方法，为列元素相加
    # print d_2
    # print support_series_2


    #pandas.Dataframe内容筛选
    # a = Series([1, 0, 1, 0])
    # b = Series([1, 1, 1, 0])
    # d_2 = DataFrame([a, b], index=['A---B', 'A---c']).T
    # support_series_2 = 1.0 * d_2.sum() / len(d_2)  # 计算列中1的个数的占比，重点在Dataframe.sum()方法，为列元素相加
    # print d_2
    # print support_series_2
    # # 	选择占比大于0.55的index
    # print list(support_series_2[support_series_2 > 0.55].index)


    #无法直接对Dataframe的内容直接遍历，即不能使用Dataframe[i]的形式，我们直接通过获取Series的index，使用Series[index]的方式对Series进行遍历，获取每一个取值。
    # result = pd.DataFrame(index=['support', 'confidence'])  # 定义一个Dataframe
    # cofidence_series = pd.Series(index=['B---C', 'C---D'])  # 定义序列
    # for i in cofidence_series.index:  # 遍历序列的index
    #     cofidence_series[i] = random.random()  # 随机生成一个0到1的随机数
    #     result['A---B'] = 0.0  # 在Dataframe扩充一个新的列，列名为A---B
    #     result['A---B']['support'] = 0.60  # 给该列每一行赋值，用index来对应
    #     result['A---B']['confidence'] = 0.70
    #
    #     result['A---C'] = 0.0
    #     result['A---C']['support'] = 0.60
    #     result['A---C']['confidence'] = 0.70
    #
    # for i in cofidence_series.index:  # 遍历序列的index
    #     result[i] = 0.0  # 在Dataframe扩充一个新的列，列名为序列中的一个index
    #     result[i]['support'] = cofidence_series[i]
    #     result[i]['confidence'] = cofidence_series[i]
    # print result

    #合并数据集
    # data = DataFrame({'key':['a','b','c'],'value1':[1,2,3]})
    # merge_data = DataFrame({'key':['b','a'],'value2':[1,2]})
    # print pd.merge(data,merge_data,on='key',how='left')

    #返回Dataframe
    # data = fanhui()
    # print data

    #Series由数字转化为字符串
    # data = [0,1,2,3]
    # data2 = [u'是',u'否',0]
    #
    # arr = np.array(data)
    # arr = arr + 1
    # print arr
    # m = {1:'D1',2:'D2',3:'D3',4:'D4'}
    # n = {u'是':u'是三方',u'否':u'非三方','0':u'没有记录'}
    # p = {u'是': u'是', u'否': u'否', '0': u'没有记录'}
    #
    # s = pd.Series(arr)
    # zifu = s.map(lambda x: str(x))
    # print zifu
    # s = s.map(lambda x : m[x])
    # print s
    #
    # r = pd.Series(np.array(data2))
    # # r = r.map(lambda x : unicode(x))
    # r = r.map(lambda x : n[x])
    #
    # print r
    #
    # t = pd.Series(np.array(data2))
    # t = t.map(lambda x: p[x])
    # print t
    #
    # q = pd.Series(np.array(data2))
    # q[q=='0'] = '没有记录'
    # print q

    data = {'A':[1,2,3],'B':[1,2,5]}
    data1 = {'A':[1,2,3],'B':[1,2,5]}
    data = pd.DataFrame(data)
    data1 = pd.DataFrame(data1)
    print data.append(data1)