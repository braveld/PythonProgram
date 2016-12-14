#-*- coding: utf-8 -*-
#计算一级行业景气程度、二级行业景气程度
import pandas as pd

#源文件
yongdian = u'F:/data/第三次整合用电量+转化行业.csv'

#新文件
new = u'F:/data/各行业景气程度.csv'
new_2 = u'F:/data/各二级行业景气程度.csv'
#加载文件
yongdian = pd.read_csv(yongdian,encoding='gbk')
# yongdian[u'一级分类编号'] = yongdian[u'一级分类编号'].fillna(0)
yongdian[u'行业混合编号'] = yongdian[u'行业混合编号'].fillna(0)
#计算一级行业景气程度

# hangye_1 = yongdian[u'一级分类编号'].drop_duplicates().tolist()
# hangyejingqidu = pd.DataFrame()
# for i in hangye_1:
#     print i
#     tmp_yongdian = yongdian[yongdian[u'一级分类编号'] == i]
#     del tmp_yongdian[u'CONS_NO']
#     del tmp_yongdian[u'一级分类编号']
#     del tmp_yongdian[u'二级分类编号']
#     del tmp_yongdian[u'行业混合编号']
#     print len(tmp_yongdian)
#     hangyejingqidu[i] = tmp_yongdian.sum()
#
# hangyejingqidu.to_csv(new,encoding='gbk')

#计算二级行业景气程度
hangye_2 = yongdian[u'行业混合编号'].drop_duplicates().tolist()
hangye_2_jingqidu = pd.DataFrame()
for i in hangye_2:
    tmp = yongdian[yongdian[u'行业混合编号'] == i]
    del tmp[u'CONS_NO']
    del tmp[u'一级分类编号']
    del tmp[u'二级分类编号']
    del tmp[u'行业混合编号']
    hangye_2_jingqidu[i] = tmp.sum()
hangye_2_jingqidu.to_csv(new_2,encoding='gbk')