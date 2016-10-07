# -*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd
import time #导入时间库用来计算用时


inputfile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/新离散化表.xls' #输入事务集文件
data = pd.read_excel(inputfile, header=None, encoding='gbk')


# 自定义连接函数，用于实现L_{k-1}到C_k的连接
def connect_string(x, ms):
    x = list(map(lambda i: sorted(i.split(ms)), x))
    l = len(x[0])
    r = []
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i][:l - 1] == x[j][:l - 1] and x[i][l - 1] != x[j][l - 1]:
                r.append(x[i][:l - 1] + sorted([x[j][l - 1], x[i][l - 1]]))
    return r


# 寻找关联规则的函数
def find_rule(d, support, confidence, ms=u'--'):
    result = pd.DataFrame(index=['support', 'confidence'])  # 定义输出结果

    support_series = 1.0 * d.sum() / len(d)  # 支持度序列
    column = list(support_series[support_series > support].index)  # 初步根据支持度筛选
    k = 0

    while len(column) > 1:
        k = k + 1
        print(u'\n正在进行第%s次搜索...' % k)
        column = connect_string(column, ms)
        print(column)
        print(u'数目：%s...' % len(column))
        sf = lambda i: d[i].prod(axis=1, numeric_only=True)  # 新一批支持度的计算函数
        # 创建连接数据，这一步耗时、耗内存最严重。当数据集较大时，可以考虑并行运算优化。
        d_2 = pd.DataFrame(list(map(sf, column)), index=[ms.join(i) for i in column]).T

        support_series_2 = 1.0 * d_2[[ms.join(i) for i in column]].sum() / len(d)  # 计算连接后的支持度

        column = list(support_series_2[support_series_2 > support].index)  # 新一轮支持度筛选
        support_series = support_series.append(support_series_2)
        column2 = []

        for i in column:  # 遍历可能的推理，如{A,B,C}究竟是A+B-->C还是B+C-->A还是C+A-->B？
            i = i.split(ms)
            for j in range(len(i)):
                column2.append(i[:j] + i[j + 1:] + i[j:j + 1])

        cofidence_series = pd.Series(index=[ms.join(i) for i in column2])  # 定义置信度序列

        for i in column2:  # 计算置信度序列
            cofidence_series[ms.join(i)] = support_series[ms.join(sorted(i))] / support_series[ms.join(i[:len(i) - 1])]

        for i in cofidence_series[cofidence_series > confidence].index:  # 置信度筛选
            result[i] = 0.0
            result[i]['confidence'] = cofidence_series[i]
            result[i]['support'] = support_series[ms.join(sorted(i.split(ms)))]

    result = result.T.sort(['confidence', 'support'], ascending=False)  # 结果整理，输出
    print(u'\n结果为：')
    print(result)

    return result

if __name__ == '__main__':
    start = time.clock()  # 计时开始
    print(u'\n转换原始数据至0-1矩阵...')
    ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数,

    b = map(ct, data.as_matrix())  # 用map方式执行
    print(type(b[0]))
    data = pd.DataFrame(b).fillna(0)  # 实现矩阵转换，空值用0填充

    end = time.clock()  # 计时结束
    print(u'\n转换完毕，用时：%0.2f秒' % (end - start))
    del b  # 删除中间变量b，节省内存

    support = 0.06  # 最小支持度
    confidence = 0.75  # 最小置信度
    ms = '---'  # 连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

    start = time.clock()  # 计时开始
    print(u'\n开始搜索关联规则...')
    find_rule(data, support, confidence, ms)
    end = time.clock()  # 计时结束
    print(u'\n搜索完成，用时：%0.2f秒' % (end - start))