#-*- coding: utf-8 -*-
#容量变更时段偏好
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
#源文件
zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的.xls'

#加载文件
zhen = pd.read_excel(zhen)

#处理方法
def qudiaonianfen(x):
   return int(x) % 100


#时段偏好
zhen_group = zhen.groupby('CONS_NO')
zhen_dict = dict(list(zhen_group))

userlist = []
for name,group in zhen_group:
    if len(group) > 8:
        userlist.append(name)

example = zhen_dict[userlist[2]]
tmp = example[example[u'申请业务类型'] == 5]
tmp = tmp[u'申请执行月'].map(lambda x : qudiaonianfen(x))
tmp_count = tmp.value_counts()
tmp_count.plot(kind = 'bar')
plt.ylim(0,3)
plt.ylabel(u'个数', fontsize=13)
plt.xlabel(u'月份', fontsize=13)
plt.show()
# nianyue = example[u'申请执行月'].map(lambda x : qudiaonianfen(x))
# nianyue = nianyue.value_counts()
# nianyue.plot(kind = 'bar')
# plt.show()

