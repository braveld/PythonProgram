#-*- coding: utf-8 -*-
#计算用电增长率、平均值、方差
import pandas as pd

#源文件
zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离.csv'
jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离.csv'
jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离.csv'

#新文件
new_zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度.csv'
new_jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度.csv'
new_jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度.csv'

#加载文件
zhen = pd.read_csv(zhen,encoding='gbk')
jia_1000 = pd.read_csv(jia_1000,encoding='gbk')
jia_2000 = pd.read_csv(jia_2000,encoding='gbk')

#假的2000户
jia_2000[u'一个月前增长率'] = (jia_2000[u'近一个月用电量'] - jia_2000[u'近二个月用电量']) / jia_2000[u'近二个月用电量']
jia_2000[u'二个月前增长率'] = (jia_2000[u'近二个月用电量'] - jia_2000[u'近三个月用电量']) / jia_2000[u'近三个月用电量']
jia_2000[u'三个月前增长率'] = (jia_2000[u'近三个月用电量'] - jia_2000[u'近四个月用电量']) / jia_2000[u'近四个月用电量']
jia_2000[u'四个月前增长率'] = (jia_2000[u'近四个月用电量'] - jia_2000[u'近五个月用电量']) / jia_2000[u'近五个月用电量']

jia_2000[u'一个月前增长率'] = jia_2000[u'一个月前增长率'].fillna(0)
jia_2000[u'二个月前增长率'] = jia_2000[u'二个月前增长率'].fillna(0)
jia_2000[u'三个月前增长率'] = jia_2000[u'三个月前增长率'].fillna(0)
jia_2000[u'四个月前增长率'] = jia_2000[u'四个月前增长率'].fillna(0)

# zhen[u'平均值'] = (zhen[u'近一个月用电量'] + zhen[u'近二个月用电量'] + zhen[u'近三个月用电量'] + zhen[u'近四个月用电量'] + zhen[u'近五个月用电量']) / 5
tmp = jia_2000[[u'近一个月用电量',u'近二个月用电量',u'近三个月用电量',u'近四个月用电量',u'近五个月用电量']]
tmp_zenzhang = jia_2000[[u'一个月前增长率',u'二个月前增长率',u'三个月前增长率',u'四个月前增长率']]
jia_2000[u'平均值'] = tmp.T.mean()
jia_2000[u'方差'] = tmp.T.std()
tmp_list = tmp_zenzhang.T.std().tolist()
list = []
for i in tmp_list:
    list.append(round(i,5))
jia_2000[u'用电增长方差'] = pd.Series(list).fillna(float('Inf'))
print jia_2000[u'用电增长方差']
jia_2000.to_csv(new_jia_2000,encoding='gbk')




#假的1000户用电增长率、平均值、方差
# jia_1000[u'一个月前增长率'] = (jia_1000[u'近一个月用电量'] - jia_1000[u'近二个月用电量']) / jia_1000[u'近二个月用电量']
# jia_1000[u'二个月前增长率'] = (jia_1000[u'近二个月用电量'] - jia_1000[u'近三个月用电量']) / jia_1000[u'近三个月用电量']
# jia_1000[u'三个月前增长率'] = (jia_1000[u'近三个月用电量'] - jia_1000[u'近四个月用电量']) / jia_1000[u'近四个月用电量']
# jia_1000[u'四个月前增长率'] = (jia_1000[u'近四个月用电量'] - jia_1000[u'近五个月用电量']) / jia_1000[u'近五个月用电量']
#
# jia_1000[u'一个月前增长率'] = jia_1000[u'一个月前增长率'].fillna(0)
# jia_1000[u'二个月前增长率'] = jia_1000[u'二个月前增长率'].fillna(0)
# jia_1000[u'三个月前增长率'] = jia_1000[u'三个月前增长率'].fillna(0)
# jia_1000[u'四个月前增长率'] = jia_1000[u'四个月前增长率'].fillna(0)
#
# # zhen[u'平均值'] = (zhen[u'近一个月用电量'] + zhen[u'近二个月用电量'] + zhen[u'近三个月用电量'] + zhen[u'近四个月用电量'] + zhen[u'近五个月用电量']) / 5
# tmp = jia_1000[[u'近一个月用电量',u'近二个月用电量',u'近三个月用电量',u'近四个月用电量',u'近五个月用电量']]
# tmp_zenzhang = jia_1000[[u'一个月前增长率',u'二个月前增长率',u'三个月前增长率',u'四个月前增长率']]
# jia_1000[u'平均值'] = tmp.T.mean()
# jia_1000[u'方差'] = tmp.T.std()
# tmp_list = tmp_zenzhang.T.std().tolist()
# list = []
# for i in tmp_list:
#     list.append(round(i,5))
# jia_1000[u'用电增长方差'] = pd.Series(list).fillna(float('Inf'))
# print jia_1000[u'用电增长方差']
# jia_1000.to_csv(new_jia_1000,encoding='gbk')



#计算真的用电增长率、方差
# zhen[u'一个月前增长率'] = (zhen[u'近一个月用电量'] - zhen[u'近二个月用电量']) / zhen[u'近二个月用电量']
# zhen[u'二个月前增长率'] = (zhen[u'近二个月用电量'] - zhen[u'近三个月用电量']) / zhen[u'近三个月用电量']
# zhen[u'三个月前增长率'] = (zhen[u'近三个月用电量'] - zhen[u'近四个月用电量']) / zhen[u'近四个月用电量']
# zhen[u'四个月前增长率'] = (zhen[u'近四个月用电量'] - zhen[u'近五个月用电量']) / zhen[u'近五个月用电量']
#
# zhen[u'一个月前增长率'] = zhen[u'一个月前增长率'].fillna(0)
# zhen[u'二个月前增长率'] = zhen[u'二个月前增长率'].fillna(0)
# zhen[u'三个月前增长率'] = zhen[u'三个月前增长率'].fillna(0)
# zhen[u'四个月前增长率'] = zhen[u'四个月前增长率'].fillna(0)
#
# # zhen[u'平均值'] = (zhen[u'近一个月用电量'] + zhen[u'近二个月用电量'] + zhen[u'近三个月用电量'] + zhen[u'近四个月用电量'] + zhen[u'近五个月用电量']) / 5
# tmp = zhen[[u'近一个月用电量',u'近二个月用电量',u'近三个月用电量',u'近四个月用电量',u'近五个月用电量']]
# tmp_zenzhang = zhen[[u'一个月前增长率',u'二个月前增长率',u'三个月前增长率',u'四个月前增长率']]
# zhen[u'平均值'] = tmp.T.mean()
# zhen[u'方差'] = tmp.T.std()
# tmp_list = tmp_zenzhang.T.std().tolist()
# list = []
# for i in tmp_list:
#     list.append(round(i,5))
# zhen[u'用电增长方差'] = pd.Series(list).fillna(float('Inf'))
# print zhen[u'用电增长方差']
# zhen.to_csv(new_zhen,encoding='gbk')