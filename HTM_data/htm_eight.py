#-*- coding: utf-8 -*-
#用电离散化、盒图
import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
from sklearn.externals import joblib
import htm_tool as ht
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
#源文件
yongdian = u'F:/data/01--30个月每月用电量、电费.csv'

#新文件

if __name__ == '__main__':


#加载文件
    yongdian = pd.read_csv(yongdian,encoding='gbk')
    del yongdian['CONS_NO']
    del yongdian[u'年月']
    yongdian = yongdian.drop_duplicates()
    yongdian = yongdian[yongdian[u'总电量'] > 0 ]
    kmodel = joblib.load(u'f:/第一次聚成6类分出用电量超高.pkl')
    tmp = pd.Series(kmodel.labels_).astype(str)
    tmp.index = range(len(tmp))
    yongdian.index = range(len(yongdian))
    yongdian[u'种类'] = tmp
    yongdian = yongdian[yongdian[u'种类'] == '0']             #5064800
    del yongdian[u'种类']

    kmodel = joblib.load(u'f:/第二次聚类聚成5类划分其余四个行为.pkl')
    tmp = pd.Series(kmodel.labels_).astype(str)
    tmp.index = range(len(tmp))
    yongdian.index = range(len(yongdian))
    yongdian[u'种类'] = tmp
    yongdian = yongdian[yongdian[u'种类'].isin(['0','2'])]        #1021520
    del yongdian[u'种类']

    kmodel = joblib.load(u'f:/第三次聚类聚成四类划分其余三个行为.pkl')
    tmp = pd.Series(kmodel.labels_).astype(str)
    tmp.index = range(len(tmp))
    yongdian.index = range(len(yongdian))
    yongdian[u'种类'] = tmp
    yongdian = yongdian[yongdian[u'种类'] == '0']         #133392
    del yongdian[u'种类']

    kmodel = joblib.load(u'f:/第四次聚类聚成六类划分其余三个行为.pkl')
    tmp = pd.Series(kmodel.labels_).astype(str)
    tmp.index = range(len(tmp))
    yongdian.index = range(len(yongdian))
    yongdian[u'种类'] = tmp
    yongdian = yongdian[yongdian[u'种类'] == '3']         #20110
    del yongdian[u'种类']


    kmodel = joblib.load(u'f:/第五次聚类聚成八类划分用电量极低.pkl')
    # tmp = pd.Series(kmodel.labels_).astype(str)
    # tmp.index = range(len(tmp))
    # yongdian.index = range(len(yongdian))
    # yongdian[u'种类'] = tmp
    # yongdian = yongdian[yongdian[u'种类'] == '5']         #3001
    # del yongdian[u'种类']
    # print yongdian.max()
    #
    # kmodel = joblib.load(u'f:/第六次聚类聚成5类划分用电量极低.pkl')
    # tmp = pd.Series(kmodel.labels_).astype(str)
    # tmp.index = range(len(tmp))
    # yongdian.index = range(len(yongdian))
    # yongdian[u'种类'] = tmp
    # yongdian = yongdian[yongdian[u'种类'] == '2']         #575
    # del yongdian[u'种类']
    # print yongdian.max()



#调用k-means算法，进行聚类分析
    # kmodel = KMeans(n_clusters = 5, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好,
    # kmodel.fit(yongdian) #训练模型
    # joblib.dump(kmodel , u'f:/第六次聚类聚成5类划分用电量极低.pkl')
    print kmodel.cluster_centers_ #查看聚类中心
    # # print kmodel.inertia_
    tmp = pd.Series(kmodel.labels_)
    tmp = pd.Series(kmodel.labels_).value_counts().sort_index()
    tmp.plot(kind = 'bar') #查看各样本对应的类别
    for i in tmp.index:
        plt.text(i-0.2,tmp.ix[i]+100,str(tmp.ix[i]),fontsize=16)
    plt.xlabel(u'聚类分类', fontsize=13)
    plt.ylabel(u'个数', fontsize=13)
    plt.show()

#[4.8644930190005107e+17, 3.3997024165080736e+17, 2.4241997905821667e+17, 1.811418831669944e+17, 1.4417405405787078e+17,
#  1.182876735392839e+17, 96706561147709936.0, 83609552476126960.0, 71743328034116848.0, 63687793207829696.0, 56160203761379568.0,
# 48908536677632240.0, 43240795961463920.0, 38537903789188336.0, 34663045744091060.0, 31317830669492940.0, 28421788700906952.0,
# 26382347210244272.0, 24375370381925156.0, 22379733706447760.0, 20718072930215116.0, 19077776226885912.0, 17761640046982370.0,
# 16406843571364108.0, 15180518731622680.0]
#最小值是24

