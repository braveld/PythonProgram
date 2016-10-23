#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
model = u'F:/data/用电模式.csv'
user_info = u'F:/data/用户基本信息.xls'
user_info_1 = u'F:/data/电压等级1.xls'
user_info_2 = u'F:/data/电压等级2.xls'
user_info_3 = u'F:/data/电压等级3.xls'
user_info_4 = u'F:/data/电压等级4.xls'
user_info_5 = u'F:/data/电压等级5.xls'

user_info_data = pd.read_excel(user_info)
user_info_data = user_info_data[['CONS_NO',u'电压等级']]
kmeans_result = u'F:/data/用电模式聚类结果.csv'
model_data = pd.read_csv(model)
# model_data = model_data.as_matrix()
# k = 8
if __name__ == '__main__':
    cons_no = model_data['CONS_NO']
    model_data['total'] = 0
    for i in model_data.columns:
        model_data['total'] = model_data['total'] + model_data[i]
    print model_data.head()
    # model_data_merge = pd.merge(model_data,user_info_data,on=['CONS_NO'],how='left')

    # model_data_1 = model_data[model_data[u'电压等级'] == 1]
    # model_data_2 = model_data[model_data[u'电压等级'] == 2]
    # model_data_3 = model_data[model_data[u'电压等级'] == 3]
    # model_data_4 = model_data[model_data[u'电压等级'] == 4]
    # model_data_5 = model_data[model_data[u'电压等级'] == 5]
    # del model_data_5[u'电压等级']
    # del model_data_5[u'CONS_NO']
    # model_data_5 = model_data_5.as_matrix()


    # print model_data[u'电压等级'].value_counts()
    # kmodel = KMeans(n_clusters=k, n_jobs=5)  # n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(model_data)  # 训练模型
    #
    # print kmodel.cluster_centers_  # 查看聚类中心
    # print kmodel.labels_  # 查看各样本对应的类别
    # k = pd.Series(kmodel.labels_)
    # print k.value_counts()
    # pd.DataFrame(k,columns=[u'类别']).to_csv(kmeans_result,encoding='gbk')
    # x = [201401,201402,201403,201404,201405,201406,201407, 201408, 201409, 201410, 201411, 201412, 201501, 201502, 201503, 201504, 201505, 201506, 201507, 201508,
    #      201509, 201510, 201511, 201512,
    #      201601, 201602, 201603, 201604, 201605, 201606]

    # for i in range(len(kmodel.labels_)):
    #     if kmodel.labels_[i] == 1:
    #         plt.plot(x, model_data[i], 'r', linewidth=2)
    # for i in model_data_5:
    #     print i
    #     plt.plot(i,'r', linewidth=2)
    # plt.show()