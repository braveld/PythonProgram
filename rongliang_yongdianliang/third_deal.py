#-*- coding: utf-8 -*-

import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
second_change_datafile = u'F:/data/第二次处理后的容量变更记录明细数据.csv'
model = u'F:/data/用电模式.csv'
classified_model = u'F:/data/分类后的用电模式.csv'
model_data = pd.read_csv(model)

if __name__ == '__main__':

    kmodel = KMeans(n_clusters=5, n_jobs=4)  # n_jobs是并行数，一般等于CPU数较好
    kmodel.fit(model_data[['mean']].as_matrix())  # 训练模型
    print kmodel.cluster_centers_  # 查看聚类中心
    print kmodel.labels_  # 查看各样本对应的类别
    print pd.Series(kmodel.labels_).value_counts()
    model_data['leibie'] = pd.Series(kmodel.labels_)
    model_data.to_csv(classified_model)