#-*- coding: utf-8 -*-
#用电增长率离散化
import pandas as pd

#源文件
zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签+行业景气度.csv'
jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签+行业景气度.csv'
jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签+行业景气度.csv'

#加载文件
zhen = pd.read_csv(zhen,encoding='gbk')
jia_1000 = pd.read_csv(jia_1000,encoding='gbk')
jia_2000 = pd.read_csv(jia_2000,encoding='gbk').dropna()

#新文件
new_zhen = u'F:/data/准备阶段_真容量变更.csv'
new_jia_1000 = u'F:/data/准备阶段_1000户假容量变更.csv'
new_jia_2000 = u'F:/data/准备阶段_2000户假容量变更.csv'

def chuli0(x):
    if x == 0:
        return 0.1
    else:
        return x

list = [u'近一个月用电量',u'近二个月用电量',u'近三个月用电量',u'近四个月用电量',u'近五个月用电量']


for i in list:
    jia_2000[i] = jia_2000[i].map(lambda x : chuli0(x))

jia_2000[u'一个月前增长率'] = (jia_2000[u'近一个月用电量'] - jia_2000[u'近二个月用电量']) / jia_2000[u'近二个月用电量']
jia_2000[u'二个月前增长率'] = (jia_2000[u'近二个月用电量'] - jia_2000[u'近三个月用电量']) / jia_2000[u'近三个月用电量']
jia_2000[u'三个月前增长率'] = (jia_2000[u'近三个月用电量'] - jia_2000[u'近四个月用电量']) / jia_2000[u'近四个月用电量']
jia_2000[u'四个月前增长率'] = (jia_2000[u'近四个月用电量'] - jia_2000[u'近五个月用电量']) / jia_2000[u'近五个月用电量']

list_zeng = [u'一个月前增长率',u'二个月前增长率',u'三个月前增长率',u'四个月前增长率']
jia_2000.to_csv(new_jia_2000,encoding='gbk')



# for i in list:
#     jia_1000[i] = jia_1000[i].map(lambda x : chuli0(x))
#
# jia_1000[u'一个月前增长率'] = (jia_1000[u'近一个月用电量'] - jia_1000[u'近二个月用电量']) / jia_1000[u'近二个月用电量']
# jia_1000[u'二个月前增长率'] = (jia_1000[u'近二个月用电量'] - jia_1000[u'近三个月用电量']) / jia_1000[u'近三个月用电量']
# jia_1000[u'三个月前增长率'] = (jia_1000[u'近三个月用电量'] - jia_1000[u'近四个月用电量']) / jia_1000[u'近四个月用电量']
# jia_1000[u'四个月前增长率'] = (jia_1000[u'近四个月用电量'] - jia_1000[u'近五个月用电量']) / jia_1000[u'近五个月用电量']
#
# list_zeng = [u'一个月前增长率',u'二个月前增长率',u'三个月前增长率',u'四个月前增长率']
# jia_1000.to_csv(new_jia_1000,encoding='gbk')

# for i in list:
#     zhen[i] = zhen[i].map(lambda x : chuli0(x))
#
# zhen[u'一个月前增长率'] = (zhen[u'近一个月用电量'] - zhen[u'近二个月用电量']) / zhen[u'近二个月用电量']
# zhen[u'二个月前增长率'] = (zhen[u'近二个月用电量'] - zhen[u'近三个月用电量']) / zhen[u'近三个月用电量']
# zhen[u'三个月前增长率'] = (zhen[u'近三个月用电量'] - zhen[u'近四个月用电量']) / zhen[u'近四个月用电量']
# zhen[u'四个月前增长率'] = (zhen[u'近四个月用电量'] - zhen[u'近五个月用电量']) / zhen[u'近五个月用电量']
#
# list_zeng = [u'一个月前增长率',u'二个月前增长率',u'三个月前增长率',u'四个月前增长率']
# zhen.to_csv(new_zhen,encoding='gbk')