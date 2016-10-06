#-*- coding: utf-8 -*-
'''
聚类离散化，最后的result的格式为：
      1           2           3           4
A     0    0.178698    0.257724    0.351843
An  240  356.000000  281.000000   53.000000
即(0, 0.178698]有240个，(0.178698, 0.257724]有356个，依此类推。
'''
from __future__ import print_function
import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法

datafile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/处理后的用户基本信息表.xls' #待聚类的数据文件
processedfile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/离散化表.xls' #数据处理后文件
typelabel ={u'合同容量':'A', u'运行容量':'B', u'检查周期':'C', u'立户时长':'D', u'送电时长':'E', u'计量点个数':'F', u'受电点个数':'G', u'电源点个数':'H', u'本季度暂停次数':'I', u'合同容量变更次数':'J', u'本季度减容次数':'K',
            u'全量减容恢复次数':'L', u'本季度暂停恢复次数':'M',u'全量增容次数':'N',u'全量暂停恢复次数':'O',u'全量暂停次数':'P',u'本季度增容次数':'Q',u'全量减容次数':'R',u'运行容量变更次数':'S',u'本季度减容恢复次数':'T',
            u'与电网交互情况': 'U',u'停电次数':'V',u'平均安全隐患间隔':'W',u'2016年1月至2016年6月总电量':'X',u'2015总电量':'Y',u'2014总电量':'Z'}
k = 3 #需要进行的聚类类别数

#读取数据并进行聚类分析
data = pd.read_excel(datafile) #读取数据
keys = list(typelabel.keys())
final_data = pd.DataFrame()

if __name__ == '__main__': #判断是否主窗口运行，如果是将代码保存为.py后运行，则需要这句，如果直接复制到命令窗口运行，则不需要这句。

  for i in range(len(keys)):
    #调用k-means算法，进行聚类离散化
    print(u'正在进行“%s”的聚类...' % keys[i])
    kmodel = KMeans(n_clusters = k, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好
    kmodel.fit(data[[keys[i]]].as_matrix()) #训练模型


    r3 = pd.Series(kmodel.labels_)
    # r3.name = keys[i]
    class_n = typelabel[keys[i]]
    m = {0: class_n+'1', 1: class_n+'2', 2: class_n+'3'}
    r3 = r3.map(lambda x : m[x])

    # r3 = pd.DataFrame(r3,columns = [keys[i]])

    final_data[keys[i]] = r3
  final_data.to_excel(processedfile)


