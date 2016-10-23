#-*- coding: utf-8 -*-

import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
from huitu.zhuzhuangtu import zhuzhuangtu
model = u'F:/data/用电模式.csv'
classified_model = u'F:/data/以总用电量分类后的用电模式.csv'
model_data = pd.read_csv(model)

if __name__ == '__main__':

    kmodel = KMeans(n_clusters=8, n_jobs=4)  # n_jobs是并行数，一般等于CPU数较好
    kmodel.fit(model_data[['total']].as_matrix())  # 训练模型
    # print kmodel.cluster_centers_  # 查看聚类中心
    # print kmodel.labels_  # 查看各样本对应的类别
    y = pd.Series(kmodel.labels_).value_counts().sort_index(ascending=True)
    y = y.tolist()
    print y
    x = [5.40694672e+06, 1.72810006e+09, 7.83635172e+08, 5.58325240e+09, 3.86620091e+08, 1.24427639e+09, 2.46295995e+09,
         1.01373041e+08]


