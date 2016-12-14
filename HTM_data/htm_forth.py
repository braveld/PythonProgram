#-*- coding: utf-8 -*-
#计算距离上一次容量变更的时间距离
import pandas as pd
import ny_caculate as ny
#已有文件
zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月.csv'
jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月.csv'
jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月.csv'

#新文件
new_zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离.csv'
new_jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离.csv'
new_jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离.csv'

#加载文件
zhen = pd.read_csv(zhen,encoding='gbk')
jia_1000 = pd.read_csv(jia_1000,encoding='gbk')
jia_2000 = pd.read_csv(jia_2000,encoding='gbk')

#计算假的1000户上一次容量变更时间距离

jia_1000[u'距离上一次容量变更'] = 10000
jia_1000[u'距离上一次增容'] = 10000
jia_1000[u'距离上一次减容'] = 10000
jia_1000[u'距离上一次减容恢复'] = 10000
jia_1000[u'距离上一次暂停'] = 10000
jia_1000[u'距离上一次暂停恢复'] = 10000
jia_1000.to_csv(new_jia_1000,encoding='gbk')

#计算假的2000户上一次容量变更时间距离
# zhen_group = zhen.groupby(['CONS_NO'])
# zhen_group = dict(list(zhen_group))
# s = []
# s1 = []
# s2 = []
# s3 = []
# s4 = []
# s5 = []
#
# jia_2000_userlist = zhen['CONS_NO'].tolist()
# jia_2000_nianyue = zhen[u'申请执行月'].tolist()
#
# for i in range(len(jia_2000_userlist)):
#
#     nianyue = jia_2000_nianyue[i]
#     rongliang = zhen_group[jia_2000_userlist[i]]
#     tmp = 10000
#     if len(rongliang) != 0:
#         rlnianyue = rongliang[u'申请执行月'].tolist()
#         for j in rlnianyue:
#             if nianyue > j:
#                 test = ny.get_month(nianyue,j)
#                 if test < tmp:
#                     tmp = test
#     s.append(tmp)
#
#     rongliang_1 = rongliang[rongliang[u'申请业务类型'] == 1]
#     tmp_1 = 10000
#     if len(rongliang_1) != 0:
#         rlnianyue_1 = rongliang_1[u'申请执行月'].tolist()
#         for j in rlnianyue_1:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_1:
#                     tmp_1 = test
#     s1.append(tmp_1)
#
#     rongliang_2 = rongliang[rongliang[u'申请业务类型'] == 2]
#     tmp_2 = 10000
#     if len(rongliang_2) != 0:
#         rlnianyue_2 = rongliang_2[u'申请执行月'].tolist()
#         for j in rlnianyue_2:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_2:
#                     tmp_2 = test
#     s2.append(tmp_2)
#
#     rongliang_3 = rongliang[rongliang[u'申请业务类型'] == 3]
#     tmp_3 = 10000
#     if len(rongliang_3) != 0:
#         rlnianyue_3 = rongliang_3[u'申请执行月'].tolist()
#         for j in rlnianyue_3:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_3:
#                     tmp_3 = test
#     s3.append(tmp_3)
#
#     rongliang_4 = rongliang[rongliang[u'申请业务类型'] == 4]
#     tmp_4 = 10000
#     if len(rongliang_4) != 0:
#         rlnianyue_4 = rongliang_4[u'申请执行月'].tolist()
#         for j in rlnianyue_4:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_4:
#                     tmp_4 = test
#     s4.append(tmp_4)
#
#     rongliang_5 = rongliang[rongliang[u'申请业务类型'] == 5]
#     tmp_5 = 10000
#     if len(rongliang_5) != 0:
#         rlnianyue_5 = rongliang_5[u'申请执行月'].tolist()
#         for j in rlnianyue_5:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_5:
#                     tmp_5 = test
#     s5.append(tmp_5)
#     if i%10000 == 0:
#         print i
#     if jia_2000_userlist[i] == 1171453767:
#         print '==================='
#         print nianyue
#         print tmp
#         print tmp_1
#         print tmp_2
#         print tmp_3
#         print tmp_4
#         print tmp_5
#
#
#
# jia_2000[u'距离上一次容量变更'] = pd.Series(s)
# jia_2000[u'距离上一次增容'] = pd.Series(s1)
# jia_2000[u'距离上一次减容'] = pd.Series(s2)
# jia_2000[u'距离上一次减容恢复'] = pd.Series(s3)
# jia_2000[u'距离上一次暂停'] = pd.Series(s4)
# jia_2000[u'距离上一次暂停恢复'] = pd.Series(s5)
# jia_2000.to_csv(new_jia_2000,encoding='gbk')




#计算真的上一次容量变更时间距离
# zhen_group = zhen.groupby(['CONS_NO'])
# zhen_group = dict(list(zhen_group))
# s = []
# s1 = []
# s2 = []
# s3 = []
# s4 = []
# s5 = []
#
# zhen_userlist = zhen['CONS_NO'].tolist()
# zhen_nianyue = zhen[u'申请执行月'].tolist()
#
# for i in range(len(zhen_userlist)):
#     nianyue = zhen_nianyue[i]
#     rongliang = zhen_group[zhen_userlist[i]]
#     tmp = 10000
#     if len(rongliang) != 0:
#         rlnianyue = rongliang[u'申请执行月'].tolist()
#         for j in rlnianyue:
#             if nianyue > j:
#                 test = ny.get_month(nianyue,j)
#                 if test < tmp:
#                     tmp = test
#     s.append(tmp)
#
#     rongliang_1 = rongliang[rongliang[u'申请业务类型'] == 1]
#     tmp_1 = 10000
#     if len(rongliang_1) != 0:
#         rlnianyue_1 = rongliang_1[u'申请执行月'].tolist()
#         for j in rlnianyue_1:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_1:
#                     tmp_1 = test
#     s1.append(tmp_1)
#
#     rongliang_2 = rongliang[rongliang[u'申请业务类型'] == 2]
#     tmp_2 = 10000
#     if len(rongliang_2) != 0:
#         rlnianyue_2 = rongliang_2[u'申请执行月'].tolist()
#         for j in rlnianyue_2:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_2:
#                     tmp_2 = test
#     s2.append(tmp_2)
#
#     rongliang_3 = rongliang[rongliang[u'申请业务类型'] == 3]
#     tmp_3 = 10000
#     if len(rongliang_3) != 0:
#         rlnianyue_3 = rongliang_3[u'申请执行月'].tolist()
#         for j in rlnianyue_3:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_3:
#                     tmp_3 = test
#     s3.append(tmp_3)
#
#     rongliang_4 = rongliang[rongliang[u'申请业务类型'] == 4]
#     tmp_4 = 10000
#     if len(rongliang_4) != 0:
#         rlnianyue_4 = rongliang_4[u'申请执行月'].tolist()
#         for j in rlnianyue_4:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_4:
#                     tmp_4 = test
#     s4.append(tmp_4)
#
#     rongliang_5 = rongliang[rongliang[u'申请业务类型'] == 5]
#     tmp_5 = 10000
#     if len(rongliang_5) != 0:
#         rlnianyue_5 = rongliang_5[u'申请执行月'].tolist()
#         for j in rlnianyue_5:
#             if nianyue > j:
#                 test = ny.get_month(nianyue, j)
#                 if test < tmp_5:
#                     tmp_5 = test
#     s5.append(tmp_5)
#
# zhen[u'距离上一次容量变更'] = pd.Series(s)
# zhen[u'距离上一次增容'] = pd.Series(s1)
# zhen[u'距离上一次减容'] = pd.Series(s2)
# zhen[u'距离上一次减容恢复'] = pd.Series(s3)
# zhen[u'距离上一次暂停'] = pd.Series(s4)
# zhen[u'距离上一次暂停恢复'] = pd.Series(s5)
# zhen.to_csv(new_zhen,encoding='gbk')