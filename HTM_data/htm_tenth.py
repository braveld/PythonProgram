#-*- coding: utf-8 -*-
#对五个用电行为进行程度的细分，得到五个行为的区间

import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


#源文件
yongdian = u'F:/data/01--30个月每月用电量、电费.csv'

#加载文件
yongdian = pd.read_csv(yongdian,encoding='gbk')
del yongdian['CONS_NO']
del yongdian[u'年月']
yongdian = yongdian.drop_duplicates()
yongdian = yongdian[yongdian[u'总电量'] > 0 ]


#五个行为
# jigao = yongdian[yongdian[u'总电量'] > 5064800]
# gao = yongdian[yongdian[u'总电量'] < 5064800][yongdian[u'总电量'] > 1021520]
# zhong = yongdian[yongdian[u'总电量'] < 1021520][yongdian[u'总电量'] > 133392]
# di = yongdian[yongdian[u'总电量'] < 133392][yongdian[u'总电量'] > 20110]
jidi = yongdian[yongdian[u'总电量'] < 20110]

if __name__ == '__main__':

    # 用电量低
    # kmodel = KMeans(n_clusters = 10, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(jidi) #训练模型
    # joblib.dump(kmodel , u'f:/用电量极低划分.pkl')
    kmodel = joblib.load(u'f:/用电量极低划分.pkl')  # 0:(5799,7795)  1:(13932,15930)  2：(0,1884)  3:(17988,20109)  4:(9837,11899)
    # 5:(1886,3831)  6:(11900,13928)    7:(15931,17986)     8:(3832,5796)     9:(7796,9836)
    print kmodel.cluster_centers_  # 查看聚类中心

    tmp = pd.Series(kmodel.labels_)
    tmp.index = range(len(tmp))
    jidi.index = range(len(jidi))
    jidi[u'种类'] = tmp
    jidi = jidi[jidi[u'种类'] == 9]
    print jidi.max()
    print jidi.min()

    # print kmodel.cluster_centers_  # 查看聚类中心
    # tmp = pd.Series(kmodel.labels_).value_counts().sort_index()
    # tmp.plot(kind='bar')  # 查看各样本对应的类别
    # for i in tmp.index:
    #     plt.text(i - 0.2, tmp.ix[i] + 100, str(tmp.ix[i]), fontsize=16)
    # plt.xlabel(u'聚类分类', fontsize=13)
    # plt.ylabel(u'个数', fontsize=13)
    # plt.show()




    # 用电量低
    # kmodel = KMeans(n_clusters = 8, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(di) #训练模型
    # joblib.dump(kmodel , u'f:/用电量低划分.pkl')
    # kmodel = joblib.load(u'f:/用电量低划分.pkl')  # 0、6:( 小于 45336)  1:(87208,101780)  2：(117071,133391)  3:(58921,72930)  4:(45339,58920)
    #5:(101781,117064)  7:(72931,87204)
    # print kmodel.cluster_centers_  # 查看聚类中心

    # tmp = pd.Series(kmodel.labels_)
    # tmp.index = range(len(tmp))
    # di.index = range(len(di))
    # di[u'种类'] = tmp
    # di = di[di[u'种类'].isin([0,6])]
    # del di[u'种类']

    # kmodel = KMeans(n_clusters=5, n_jobs=4)  # n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(di) #训练模型
    # joblib.dump(kmodel , u'f:/用电量低低层级划分.pkl')
    # kmodel = joblib.load(u'f:/用电量低低层级划分.pkl')  # 0:(35028,40132)    1:(20112,25050)   2:(30019,35025)
    #  3:(40136,45336)   4:(25053,30018)

    # tmp = pd.Series(kmodel.labels_)
    # tmp.index = range(len(tmp))
    # di.index = range(len(di))
    # di[u'种类'] = tmp
    # di = di[di[u'种类'] == 4]
    # print di.max()
    # print di.min()

    # print kmodel.cluster_centers_  # 查看聚类中心
    # tmp = pd.Series(kmodel.labels_).value_counts().sort_index()
    # tmp.plot(kind='bar')  # 查看各样本对应的类别
    # for i in tmp.index:
    #     plt.text(i - 0.2, tmp.ix[i] + 100, str(tmp.ix[i]), fontsize=16)
    # plt.xlabel(u'聚类分类', fontsize=13)
    # plt.ylabel(u'个数', fontsize=13)
    # plt.show()




    # 用电量中  0:(43164000,63769200)   1:(5066100,12903200)    2:(90286900,149424000)
    # 3:(63874800,90191200)   4:(25740000,43150800)   5:(166953600,269842100)   6:(12913740,25731200)
    # kmodel = KMeans(n_clusters = 6, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(zhong) #训练模型
    # joblib.dump(kmodel , u'f:/用电量中划分.pkl')
    # kmodel = joblib.load(u'f:/用电量中划分.pkl') #0、2:( < 332700)     1:(465360,624600)   3：(810760,1021317)  4:(624630,810660)   5:(332720,465300)
    # print kmodel.cluster_centers_  # 查看聚类中心

    # tmp = pd.Series(kmodel.labels_)
    # tmp.index = range(len(tmp))
    # zhong.index = range(len(zhong))
    # zhong[u'种类'] = tmp
    # zhong = zhong[zhong[u'种类'].isin([0,2])]
    # del zhong[u'种类']

    # kmodel = KMeans(n_clusters=6, n_jobs=4)  # n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(zhong) #训练模型
    # joblib.dump(kmodel , u'f:/用电量中低层级划分.pkl')
    # kmodel = joblib.load(u'f:/用电量中低层级划分.pkl') #0:(293999,332700)    1:(160457,189879)   2:(222210,257117)   3:(189888,222205)   4:(133394,160450)   5:(257142,293964)
    #
    # tmp = pd.Series(kmodel.labels_)
    # tmp.index = range(len(tmp))
    # zhong.index = range(len(zhong))
    # zhong[u'种类'] = tmp
    # zhong = zhong[zhong[u'种类'] == 5]
    # print zhong.max()
    # print zhong.min()


    # print kmodel.cluster_centers_  # 查看聚类中心
    # tmp = pd.Series(kmodel.labels_).value_counts().sort_index()
    # tmp.plot(kind='bar')  # 查看各样本对应的类别
    # for i in tmp.index:
    #     plt.text(i - 0.2, tmp.ix[i] + 100, str(tmp.ix[i]), fontsize=16)
    # plt.xlabel(u'聚类分类', fontsize=13)
    # plt.ylabel(u'个数', fontsize=13)
    # plt.show()




    #用电量极高  0:(43164000,63769200)   1:(5066100,12903200)    2:(90286900,149424000)
    # 3:(63874800,90191200)   4:(25740000,43150800)   5:(166953600,269842100)   6:(12913740,25731200)
    # kmodel = KMeans(n_clusters = 7, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(jigao) #训练模型
    # joblib.dump(kmodel , u'f:/用电量极高划分.pkl')
    # kmodel = joblib.load(u'f:/用电量极高划分.pkl')
    # print kmodel.cluster_centers_  # 查看聚类中心
    #
    # tmp = pd.Series(kmodel.labels_)
    # tmp.index = range(len(tmp))
    # jigao.index = range(len(jigao))
    # jigao[u'种类'] = tmp
    # jigao = jigao[jigao[u'种类'] == 6]
    # print len(jigao)
    # print jigao.max()
    # print jigao.min()

    # tmp = pd.Series(kmodel.labels_).value_counts().sort_index()
    # tmp.plot(kind='bar')  # 查看各样本对应的类别
    # for i in tmp.index:
    #     plt.text(i - 0.2, tmp.ix[i] + 100, str(tmp.ix[i]), fontsize=16)
    # plt.xlabel(u'聚类分类', fontsize=13)
    # plt.ylabel(u'个数', fontsize=13)
    # plt.show()


    # 用电量高
    # kmodel = KMeans(n_clusters=6, n_jobs=4)  # n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(gao)  # 训练模型
    # joblib.dump(kmodel, u'f:/用电量高划分.pkl')
    # kmodel = joblib.load(u'f:/用电量高划分.pkl') #0、5：( <2050560)     1:(3316920,4112880)     2:(2050740,2648320)     3:(4114400,5063520)     4:(2649000,3316440)


    # tmp = pd.Series(kmodel.labels_)
    # tmp.index = range(len(tmp))
    # gao.index = range(len(gao))
    # gao[u'种类'] = tmp
    # gao = gao[gao[u'种类'].isin([0,5])]
    # del gao[u'种类']

    # kmodel = KMeans(n_clusters=5, n_jobs=4)  # n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(gao)  # 训练模型
    # joblib.dump(kmodel, u'f:/用电量高低层级划分.pkl')
    # kmodel = joblib.load(u'f:/用电量高低层级划分.pkl') #0:(1021800,1195560)  1:(1590080,1812420)  2:(1195840,1384440)  3:(1812560,2050560)   4:(1384560,1589865)
    # print kmodel.cluster_centers_  # 查看聚类中心
    # tmp = pd.Series(kmodel.labels_)
    # tmp.index = range(len(tmp))
    # gao.index = range(len(gao))
    # gao[u'种类'] = tmp
    # gao = gao[gao[u'种类'] == 4]
    # print gao.max()
    # print gao.min()

    # tmp = pd.Series(kmodel.labels_)
    # tmp = pd.Series(kmodel.labels_).value_counts().sort_index()
    # tmp.plot(kind='bar')  # 查看各样本对应的类别
    # for i in tmp.index:
    #     plt.text(i - 0.2, tmp.ix[i] + 100, str(tmp.ix[i]), fontsize=16)
    # plt.xlabel(u'聚类分类', fontsize=13)
    # plt.ylabel(u'个数', fontsize=13)
    # plt.show()
