#-*- coding: utf-8 -*-

import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
import scipy
import scipy.cluster.hierarchy as sch
from scipy.cluster.vq import vq,kmeans,whiten
import matplotlib.pyplot as plt
test = u'F:/data/去除第一次样本集.csv'
last = u'F:/data/指标增加最终样本集.csv'
new = u'F:/data/用电曲线分类.csv'
another = u'F:/data/另一个用电曲线分类.csv'
if __name__ == '__main__':
    origin_data = pd.read_csv(last,encoding='gbk')
    # origin_data = origin_data[origin_data['class'] == 0]
    list = [u'前五个月增长率',u'前四个月增长率',u'前三个月增长率',u'前二个月增长率',u'前一个月增长率']
    # l = []
    #
    # data = origin_data[list].as_matrix()
    # for i in range(len(data)):
    #     count = 0
    #     if data[i][0] == 0:
    #         count = count + 1
    #     if data[i][1] == 0:
    #         count = count + 1
    #     if data[i][2] == 0:
    #         count = count + 1
    #     if data[i][3] == 0:
    #         count = count + 1
    #     if data[i][4] == 0:
    #         count = count + 1
    #     l.append(count)
    # origin_data[u'0不交电费次数'] = pd.Series(l)
    # origin_data.to_csv(last, encoding='gbk')



    data = origin_data[list].T
    origin_data[u'平均用电增长率'] = data.mean()
    origin_data.to_csv(last, encoding='gbk')

    # data = (data - data.mean(axis=0)) / (data.std(axis=0))  # 简洁的语句实现了标准化变换，类似地可以实现任何想要的变换。
    # 调用k-means算法，进行聚类分析
    # kmodel = KMeans(n_clusters=5, n_jobs=1)  # n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(data)  # 训练模型
    #
    # print kmodel.cluster_centers_  # 查看聚类中心
    # print pd.Series(kmodel.labels_).value_counts()  # 查看各样本对应的类别





    # origin_data['class'] = kmodel.labels_
    # origin_data.to_csv(last,encoding='gbk')

    # data = pd.read_csv(new,encoding='gbk')
    # # data = data[list]
    # data = data[data['class'] == 2]
    # data = data[list].head().T
    # print data
    # data.index = ['six','five','four','three','two','one']
    # # print data
    # data.plot()
    # plt.show()

