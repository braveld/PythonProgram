#-*- coding: utf-8 -*-
#计算最大值、导入行业、计算行业景气程度
import pandas as pd

#源文件
zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度.csv'
jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度.csv'
jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度.csv'

yongdian = u'F:/data/第三次整合用电量.csv'
hangye = u'F:/data/行业分类--罗迪.xls'

#新文件
new_zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+行业.csv'
new_zhen_1 = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业.csv'
new_jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+行业.csv'
new_jia_1000_1 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业.csv'
new_jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+行业.csv'
new_jia_2000_1 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业.csv'
new_yongdian = u'F:/data/第三次整合用电量+转化行业.csv'
#文件加载
yongdian = pd.read_csv(yongdian,encoding='gbk')
zhen = pd.read_csv(zhen,encoding='gbk')
jia_1000 = pd.read_csv(jia_1000,encoding='gbk')
jia_2000 = pd.read_csv(jia_2000,encoding='gbk')
hangye = pd.read_excel(hangye)
hangye = hangye[[u'CONS_NO',u'一级分类编号',u'二级分类编号']]
hangye = hangye.dropna()
# print hangye[u'一级分类编号'].value_counts()
# print hangye[u'二级分类编号'].value_counts()
fenlei_1 = hangye[u'一级分类编号'].tolist()
fenlei_2 = hangye[u'二级分类编号'].tolist()
tmp = []
for i in range(len(fenlei_1)):
    test = str(fenlei_1[i]) + str(fenlei_2[i])
    tmp.append(test)
hangye[u'行业混合编号'] = pd.Series(tmp)
# zhen = pd.merge(zhen,hangye,on='CONS_NO',how='left')
# zhen.to_csv(new_zhen,encoding='gbk')

# jia_1000 = pd.merge(jia_1000,hangye,on='CONS_NO',how='left')
# jia_1000.to_csv(new_jia_1000,encoding='gbk')
#
# jia_2000 = pd.merge(jia_2000,hangye,on='CONS_NO',how='left')
# jia_2000.to_csv(new_jia_2000,encoding='gbk')


fenlei_1 = hangye[u'一级分类编号'].drop_duplicates().tolist()
fenlei_2 = hangye[u'二级分类编号'].drop_duplicates().tolist()
fenlei_3 = hangye[u'行业混合编号'].drop_duplicates().tolist()



# print len(fenlei_1)  #50
# print len(fenlei_2)#277
# print len(fenlei_3)#277

deal_1 = {}
deal_2 = {}
deal_3 = {}
for j in range(len(fenlei_1)):
    deal_1[fenlei_1[j]] = j + 1

for k in range(len(fenlei_2)):
    deal_2[fenlei_2[k]] = k + 1

for l in range(len(fenlei_3)):
    deal_3[fenlei_3[l]] = l + 1

hangye[u'一级分类编号'] = hangye[u'一级分类编号'].map(lambda x : deal_1[x])
hangye[u'二级分类编号'] = hangye[u'二级分类编号'].map(lambda x : deal_2[x])
hangye[u'行业混合编号'] = hangye[u'行业混合编号'].map(lambda x : deal_3[x])

yongdian = pd.merge(yongdian,hangye,on='CONS_NO',how='left')
yongdian.to_csv(new_yongdian,encoding='gbk')

# zhen = pd.merge(zhen,hangye,on='CONS_NO',how='left')
# zhen.to_csv(new_zhen_1,encoding='gbk')

# jia_1000 = pd.merge(jia_1000,hangye,on='CONS_NO',how='left')
# jia_1000.to_csv(new_jia_1000_1,encoding='gbk')
#
# jia_2000 = pd.merge(jia_2000,hangye,on='CONS_NO',how='left')
# jia_2000.to_csv(new_jia_2000_1,encoding='gbk')
# yongdian = pd.merge(yongdian,hangye,on='CONS_NO',how='left')
