#-*- coding: utf-8 -*-

import pandas as pd


new_discretization = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/新离散化表.xls'
simple_discretization = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/不完整新离散化表 .xls'
origin_datafile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/用户基本信息.xls'
new_file = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/描述表.xls'
deal_datafile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/处理后的用户基本信息表.xls'
new_txt = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/完整描述表.xls'
result = pd.DataFrame()
final_result = []

if __name__ == '__main__':
    # result = []
    # discretization_data = pd.read_excel(new_discretization,encoding='gbk')
    # for i in discretization_data.columns:
    #     r = discretization_data[i].value_counts()
    #     r = pd.DataFrame(r,columns=[i]).T
    #     result.append(r)
    # for j in range(len(result)):
    #     print result[j]


    # simple_data = pd.read_excel(simple_discretization,encoding='gbk')
    # for i in simple_data.columns:
    #
    #     r1 = simple_data[i].value_counts()
    #     r1 = pd.DataFrame(r1,columns=[i])
    #
    #     r2 = pd.DataFrame(list(r1.T.columns),columns=[i+'n'])
    #     r1.index = [0, 1, 2]
    #     r = pd.concat([r2, r1], axis=1)
    #     # r[i] = pd.rolling_mean(r[i], 2)  # rolling_mean()用来计算相邻2列的均值，以此作为边界点。
    #     # r[i][1] = 0.0  # 这两句代码将原来的聚类中心改为边界点。
    #     result = result.append(r.T)
    #
    # result = result.sort_index()  # 以Index排序，即以A,B,C,D,E,F顺序排
    # print result
    # result.to_excel(new_file)

    # origin_data = pd.read_excel(origin_datafile,encoding='gbk')
    # for i in origin_data.columns:
    #     num = origin_data[i].count()
    #     print i,num

    deal_data = pd.read_excel(deal_datafile,encoding='gbk')
    d = deal_data.describe()
    d.to_excel(new_txt)