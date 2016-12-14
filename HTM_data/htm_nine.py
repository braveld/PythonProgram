#-*- coding: utf-8 -*-
#用电量盒图，以及10个用户的用电曲线展示
import pandas as pd
import matplotlib.pyplot as plt
import htm_tool as ht
from sklearn.cluster import KMeans #导入K均值聚类算法
from sklearn.externals import joblib
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
#源文件
yongdian = u'F:/data/01--30个月每月用电量、电费.csv'
quxian = u'F:/data/第二次整合用电量.csv'
hangye = u'F:/data/第三次整合用电量+转化行业.csv'
hangye_luodi = u'F:/data/行业分类--罗迪.xls'

#加载文件
yongdian = pd.read_csv(yongdian,encoding='gbk')
yongdian.columns = ['CONS_NO',u'年月',u'月用电量']
yongdian = yongdian[yongdian[u'月用电量'] >= 0]
quxian = pd.read_csv(quxian,encoding='gbk')
# hangye = pd.read_csv(hangye,encoding='gbk')
# hangye_luodi = pd.read_excel(hangye_luodi)

#用电曲线
# quxian_select = ['1100007614','1100007627','1100007656','1100017989','1100017992','1100034722','1100034735','1100035334','1100018344','1100005706']
# r = ['1100034735','1100018344','1100007627'] #
# dates = ['201401', '201402', '201403', '201404', '201405', '201406', '201407', '201408', '201409', '201410', '201411', '201412', '201501',
#              '201502', '201503', '201504', '201505', '201506', '201507', '201508',
#              '201509', '201510', '201511', '201512',
#              '201601', '201602', '201603', '201604', '201605', '201606']
# quxian = quxian[r]
# quxian.index = dates
# print quxian.describe()
# quxian.plot(kind = 'line')
# plt.xlabel(u'月份', fontsize=13)
# plt.ylabel(u'月用电量', fontsize=13)
# plt.show()



#盒图
# yongdian_drop_duplicate = yongdian[u'月用电量'].drop_duplicates()
# print yongdian_drop_duplicate.describe()
# ax = yongdian_drop_duplicate.plot(kind = 'box')
# ax.set_yscale('log')
# plt.show()

#行业分布——罗迪
# yiji = hangye_luodi[u'一级分类编号']
# erji = hangye_luodi[u'二级分类编号']
#
# yiji_drop_duplicate = yiji.drop_duplicates()
# erji_drop_duplicate = erji.drop_duplicates()
#
# print len(yiji_drop_duplicate)
# print len(erji_drop_duplicate)
#
#
# tmp_1 = yiji.value_counts().sort_index()
# tmp_2 = erji.value_counts().sort_index()
#
# tmp_1 = tmp_1[tmp_1 > 100]
# # tmp_1.index = range(len(tmp_1))
#
#
#
# tmp_1.plot(kind = 'bar')
# # # tmp_2.plot(kind = 'bar')
# for i in tmp_1.index:
#     plt.text(i - 0.5, tmp_1.ix[i] + 10, str(tmp_1.ix[i]))
# plt.xlabel(u'行业编号', fontsize=16)
# plt.ylabel(u'数量', fontsize=16)
# plt.show()

#聚类
# if __name__ == '__main__':
#     yongdian_drop_duplicate = yongdian.drop_duplicates([u'月用电量'])
#     yongdian_drop_duplicate.index = range(len(yongdian_drop_duplicate))
#     del yongdian_drop_duplicate['CONS_NO']
#     del yongdian_drop_duplicate[u'年月']
#     # kmodel = KMeans(n_clusters=6, n_jobs=4)  # n_jobs是并行数，一般等于CPU数较好,
#     # kmodel.fit(yongdian_drop_duplicate)  # 训练模型
#     # joblib.dump(kmodel, u'f:/第一次聚成6类分出用电量超高.pkl')
#     kmodel = joblib.load(u'f:/第一次聚成6类分出用电量超高.pkl')
#     print kmodel.cluster_centers_ #查看聚类中心
#     tmp = pd.Series(kmodel.labels_)
#     #
#     # tmp.index = range(len(tmp))
#     # yongdian_drop_duplicate[u'种类'] = tmp
#     # huitu = ht.stratified_sampling(yongdian_drop_duplicate, u'种类',1)
#     #
#     # ax = huitu.plot(kind = 'scatter',x=u'种类',y=u'月用电量')
#     # plt.scatter(huitu[u'种类'],huitu[u'月用电量'])
#     # ax.set_yscale('log')
#
#
#     tmp_count = tmp.value_counts().sort_index()
#
#     tmp_count.plot(kind = 'bar') #查看各样本对应的类别
#     for i in tmp_count.index:
#         plt.text(i-0.2,tmp_count.ix[i]+100,str(tmp_count.ix[i]),fontsize=16)
#     plt.xlabel(u'聚类分类', fontsize=13)
#     plt.ylabel(u'个数', fontsize=13)
#
#     plt.show()