#-*- coding: utf-8 -*-
# 导入一级经济景气度
import pandas as pd
import ny_caculate as nc

#源文件
jingqidu = u'F:/data/最终一级行业景气度.csv'
zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签.csv'
jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签.csv'
jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签.csv'

#加载文件
jingqidu = pd.read_csv(jingqidu,encoding='gbk')
zhen = pd.read_csv(zhen,encoding='gbk')
jia_1000 = pd.read_csv(jia_1000,encoding='gbk')
jia_2000 = pd.read_csv(jia_2000,encoding='gbk').dropna()

#新文件
new_zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签+行业景气度.csv'
new_jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签+行业景气度.csv'
new_jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签+行业景气度.csv'


dates = [201401, 201402, 201403, 201404, 201405, 201406, 201407, 201408, 201409, 201410, 201411, 201412, 201501,
             201502, 201503, 201504, 201505, 201506, 201507, 201508,
             201509, 201510, 201511, 201512,
             201601, 201602, 201603, 201604, 201605, 201606]

jingqidu[u'前一个月月份'] = pd.Series(dates)


zhen[u'前一个月月份'] = zhen[u'申请执行月'].map(lambda x : nc.minus(x,1))
jia_1000[u'前一个月月份'] = jia_1000[u'申请执行月'].map(lambda x : nc.minus(x,1))
jia_2000[u'前一个月月份'] = jia_2000[u'申请执行月'].map(lambda x : nc.minus(x,1))



jia_2000_hangye = jia_2000[u'一级分类编号_y'].tolist()
nianyue = jia_2000[u'前一个月月份'].map(lambda x : nc.ny_duiying(x)).tolist()
kong = []
for i in range(len(jia_2000_hangye)):
    h = int(jia_2000_hangye[i])
    h = str(h)
    list = jingqidu[h]
    list = list.tolist()
    # print list
    n = nianyue[i]
    # print n
    tmp = list[n]
    kong.append(tmp)

jia_2000[u'一级行业经济景气度'] = pd.Series(kong)
jia_2000.to_csv(new_jia_2000,encoding='gbk')


# jia_1000_hangye = jia_1000[u'一级分类编号_y'].dropna().tolist()
# nianyue = jia_1000[u'前一个月月份'].map(lambda x : nc.ny_duiying(x)).tolist()
# kong = []
# for i in range(len(jia_1000_hangye)):
#     h = int(jia_1000_hangye[i])
#     h = str(h)
#     list = jingqidu[h]
#     list = list.tolist()
#     # print list
#     n = nianyue[i]
#     # print n
#     tmp = list[n]
#     kong.append(tmp)
#
# jia_1000[u'一级行业经济景气度'] = pd.Series(kong)
# jia_1000.to_csv(new_jia_1000,encoding='gbk')


# zhen_hangye = zhen[u'一级分类编号_y'].tolist()
# nianyue = zhen[u'前一个月月份'].map(lambda x : nc.ny_duiying(x)).tolist()
# kong = []
# for i in range(len(zhen_hangye)):
#     # print i
#     h = str(zhen_hangye[i])
#     # print h
#     list = jingqidu[h].tolist()
#     # print list
#     n = nianyue[i]
#     # print n
#     tmp = list[n]
#     kong.append(tmp)
#
# zhen[u'一级行业经济景气度'] = pd.Series(kong)
# zhen.to_csv(new_zhen,encoding='gbk')


