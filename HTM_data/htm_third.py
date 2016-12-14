#-*- coding: utf-8 -*-
#整理30个月的用电量，未达到的用-1表示没有用电或者尚未开户

import pandas as pd
import ny_caculate as ny
#源文件
yongdian_origin = u'F:/data/01--30个月每月用电量、电费.csv'
zhen = u'F:/data/真容量变更数据+用户基本信息.xls'
jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息.xls'
jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息.csv'



#新文件
new_yongdian = u'F:/data/整合用电量.csv'
zhen_6 = u'F:/data/真容量变更数据+用户基本信息+用电量.xls'
jia_2000_6 = u'F:/data/2000户容量变更数据+用户基本信息+用电量.xls'
jia_1000_6 = u'F:/data/1000户容量变更数据+用户基本信息+用电量.xls'
second_yongdian = u'F:/data/第二次整合用电量.csv'
third_yongdian = u'F:/data/第三次整合用电量.csv'
new1 = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的.xls'
new2 = u'F:/data/真容量变更数据+用户基本信息+用电量+去除没有用电记录的+前五个月.csv'
new3 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的.csv'
new4 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月.csv'
new5 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的.csv'
new6 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月.csv'
#加载文件
# yongdian_origin = pd.read_csv(yongdian_origin,encoding='gbk')
# zhen6 = pd.read_excel(new1)
#
# jia_1000 = pd.read_csv(new3,encoding='gbk')
jia_2000 = pd.read_csv(new5,encoding='gbk')
print u'加载文件'



#预处理
# userlist = yongdian_origin['CONS_NO'].drop_duplicates()
# new_user = []  # 存储用户编号
# dates = [201401, 201402, 201403, 201404, 201405, 201406, 201407, 201408, 201409, 201410, 201411, 201412, 201501,
#              201502, 201503, 201504, 201505, 201506, 201507, 201508,
#              201509, 201510, 201511, 201512,
#              201601, 201602, 201603, 201604, 201605, 201606]
# new_dates = []
# for i in userlist:
#     for j in dates:
#         new_user.append(i)
#         new_dates.append(j)
#
# data = {'CONS_NO':new_user,u'年月':new_dates}
# data = pd.DataFrame(data)
# data = pd.merge(data,yongdian_origin,on=['CONS_NO',u'年月'],how='left')
# data = data.fillna('-1')
#data.to_csv(new_yongdian,encoding='gbk')

#整合容量变更前六个月的用电量
#data_group = data.groupby(['CONS_NO'])
# data = pd.read_csv(new_yongdian,encoding='gbk')

print u'文件加载完成'
# yd = pd.DataFrame()
# yd_all_6 = pd.DataFrame()
# for i in userlist:
#     all_yd = []
#     yd_6 = []
#     d = data[data['CONS_NO'] == i]
#     d = d.as_matrix()
#     for j in range(30):
#         all_yd.append(d[j][2])
#     yd[i] = pd.Series(all_yd)

#yd = yd.T
#yd.columns = dates
#yd.to_csv(third_yongdian,encoding='gbk')

#前六个月的用电量
yd_all_6 = pd.DataFrame()
yd_user = []

yd = pd.read_csv(third_yongdian,encoding='gbk')
temp_userlist = yd['CONS_NO'].tolist()
del yd['CONS_NO']
yd = yd.T
yd.columns = temp_userlist


#去除没有用电记录的用户
# yongdian_userlist = yd['CONS_NO'].tolist()
# zhen6_userlist = zhen6['CONS_NO'].drop_duplicates().tolist()
#
# tmp = [val for val in zhen6_userlist if val in yongdian_userlist]
# zhen6 = zhen6[zhen6['CONS_NO'].isin(tmp)]
# zhen6.to_excel(new1)

# jia_1000_userlist = jia_1000['CONS_NO'].drop_duplicates().tolist()
# tmp_jia_1000 = [val for val in jia_1000_userlist if val in temp_userlist]
# jia_1000 = jia_1000[jia_1000['CONS_NO'].isin(tmp_jia_1000)]
# jia_1000.to_csv(new3,encoding='gbk')


# jia_2000_userlist = jia_2000['CONS_NO'].drop_duplicates().tolist()
# tmp_jia_2000 = [val for val in jia_2000_userlist if val in temp_userlist]
# jia_2000 = jia_2000[jia_2000['CONS_NO'].isin(tmp_jia_2000)]
# jia_2000.to_csv(new5,encoding='gbk')


#真实案例导入前六个月用电量
# zhen6_userlist = zhen6['CONS_NO'].tolist()
# zhen6_nianyue = zhen6[u'申请执行月'].tolist()
# y1 = []
# y2 = []
# y3 = []
# y4 = []
# y5 = []
# print len(zhen6_userlist)
#
# for i in range(len(zhen6_userlist)):
#     print i
#     ydlist = yd[zhen6_userlist[i]]
#     nianyue = int(ny.ny_duiying(zhen6_nianyue[i]))
#     y1.append(ydlist[nianyue - 1])
#     y2.append(ydlist[nianyue - 2])
#     y3.append(ydlist[nianyue - 3])
#     y4.append(ydlist[nianyue - 4])
#     y5.append(ydlist[nianyue - 5])
#
# zhen6[u'近一个月用电量'] = pd.Series(y1)
# zhen6[u'近二个月用电量'] = pd.Series(y2)
# zhen6[u'近三个月用电量'] = pd.Series(y3)
# zhen6[u'近四个月用电量'] = pd.Series(y4)
# zhen6[u'近五个月用电量'] = pd.Series(y5)
#
# zhen6.to_csv(new2,encoding='gbk')

#假的1000户导入前5个月的用电量
# jia_1000_userlist = jia_1000['CONS_NO'].tolist()
# jia_1000_nianyue = jia_1000[u'申请执行月'].tolist()
#
# y1 = []
# y2 = []
# y3 = []
# y4 = []
# y5 = []
# print len(jia_1000_userlist)
#
# for i in range(len(jia_1000_userlist)):
#     print i
#     yd_user.append(jia_1000_userlist[i])
#     ydlist = yd[jia_1000_userlist[i]]
#
#     nianyue = int(ny.ny_duiying(jia_1000_nianyue[i]))
#     y1.append(ydlist[nianyue - 1])
#     y2.append(ydlist[nianyue - 2])
#     y3.append(ydlist[nianyue - 3])
#     y4.append(ydlist[nianyue - 4])
#     y5.append(ydlist[nianyue - 5])
# print  len(y1)
# jia_1000[u'近一个月用电量'] = pd.Series(y1)
# jia_1000[u'近二个月用电量'] = pd.Series(y2)
# jia_1000[u'近三个月用电量'] = pd.Series(y3)
# jia_1000[u'近四个月用电量'] = pd.Series(y4)
# jia_1000[u'近五个月用电量'] = pd.Series(y5)
# print len(jia_1000)
# jia_1000.to_csv(new4,encoding='gbk')

#假的2000户导入前5个月的用电量
jia_2000_userlist = jia_2000['CONS_NO'].tolist()
jia_2000_nianyue = jia_2000[u'申请执行月'].tolist()

y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
print len(jia_2000_userlist)

for i in range(len(jia_2000_userlist)):
    print i
    yd_user.append(jia_2000_userlist[i])
    ydlist = yd[jia_2000_userlist[i]]

    nianyue = int(ny.ny_duiying(jia_2000_nianyue[i]))
    y1.append(ydlist[nianyue - 1])
    y2.append(ydlist[nianyue - 2])
    y3.append(ydlist[nianyue - 3])
    y4.append(ydlist[nianyue - 4])
    y5.append(ydlist[nianyue - 5])
print  len(y1)
jia_2000[u'近一个月用电量'] = pd.Series(y1)
jia_2000[u'近二个月用电量'] = pd.Series(y2)
jia_2000[u'近三个月用电量'] = pd.Series(y3)
jia_2000[u'近四个月用电量'] = pd.Series(y4)
jia_2000[u'近五个月用电量'] = pd.Series(y5)
print len(jia_2000)
jia_2000.to_csv(new6,encoding='gbk')







