#-*- coding: utf-8 -*-
# 计算一级经济景气度
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
#源文件
yiji_hangye = u'F:/data/各行业景气程度.csv'
hunhe_hangye = u'F:/data/各二级行业景气程度.csv'

#新文件
hangyejingqi = u'F:/data/一级行业景气度.csv'
yiji_huafen = u'F:/data/一级行业景气度划分标准.csv'



#加载文件
yiji_hangye = pd.read_csv(yiji_hangye,encoding='gbk')
yiji_hangye.index = range(len(yiji_hangye))

def zhuanhuabiaoqian(x,l):
    if x < l[0]:
        return u'经济极其不景气'
    if l[0] <= x < l[1]:
        return u'经济不景气'
    if l[1] <= x < l[2]:
        return u'经济形势一般'
    if l[2] <= x < l[3]:
        return u'经济景气'
    if x > l[3]:
        return u'经济十分景气'

def zhuanhua(x, l):
    if x < l[0]:
        return u'1'
    if l[0] <= x < l[1]:
        return u'2'
    if l[1] <= x < l[2]:
        return u'3'
    if l[2] <= x < l[3]:
        return u'4'
    if x > l[3]:
        return u'5'

# yiji_28 = yiji_hangye['28']
# yiji_28.plot(kind = 'line')
# plt.show()

jingqi = pd.DataFrame()
for i in yiji_hangye.columns:
    d_max = yiji_hangye[i].max()
    d_min = yiji_hangye[i].min()
    dengji = []
    for j in range(1,5):
        dengji.append((d_max - d_min) * j / 5.0)
    jingqi[i] = pd.Series(dengji)
# jingqi.to_csv(yiji_huafen,encoding='gbk')

zuizhong_biaoqian = pd.DataFrame()
zuizhong = pd.DataFrame()
for j in yiji_hangye.columns:
    huafen = jingqi[j].tolist()
    length = len(yiji_hangye[j])
    zuizhong_biaoqian[j] = yiji_hangye[j].map(lambda x : zhuanhuabiaoqian(x,huafen))
    zuizhong[j] = yiji_hangye[j].map(lambda x: zhuanhua(x, huafen))
zuizhong.to_csv(u'F:/data/最终一级行业景气度.csv',encoding='gbk')
zuizhong_biaoqian.to_csv(u'F:/data/最终一级行业景气度_标签.csv',encoding='gbk')









