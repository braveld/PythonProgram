#-*- coding: utf-8 -*-

import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
classified_model = u'F:/data/以总用电量分类后的用电模式.csv'
didianliang_file = u'F:/data/低电量的用电模式.csv'


if __name__ == '__main__':
    # model_data = model_data[model_data['leibie'] == 0]
    # del model_data['leibie']
    # model_data.to_csv(didianliang_file)
    model_data = pd.read_csv(didianliang_file)
    kmodel = KMeans(n_clusters=8, n_jobs=4)  # n_jobs是并行数，一般等于CPU数较好
    kmodel.fit(model_data[['total']].as_matrix())  # 训练模型
    print kmodel.cluster_centers_  # 查看聚类中心
    print kmodel.labels_  # 查看各样本对应的类别
    print pd.Series(kmodel.labels_).value_counts()
    model_data['leibie'] = pd.Series(kmodel.labels_)
    model_data.to_csv(classified_model)