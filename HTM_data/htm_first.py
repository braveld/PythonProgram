#-*- coding: utf-8 -*-
#处理各个表格的空值，用户信息表全部转化为0
#格式转化，日期格式——容量变更
import pandas as pd
from dateutil.parser import parse
from random import shuffle

#年月减法,
# a 被减年月
# b 月份数
def minus(a,b):
    year = int(a) / 100
    month = int(a) % 100
    y = 0
    m = 0
    if month <= int(b):
        m = 12 - int(b) + month
        y = year -1
        if m < 10:
            return str(y) + '0' + str(m)
        else:
            return  str(y) + str(m)
    else:
        m = month - int(b)
        y = year
        if m < 10:
            return str(y) + '0' + str(m)
        else:
            return str(y) + str(m)


#年月相减得月份
# a 被减年月
# b 减年月
def get_month(a,b):
    year_a = int(a) / 100
    month_a = int(a) % 100
    year_b = int(b) / 100
    month_b = int(b) % 100

    if month_a < month_b:
        year = year_a - year_b -1
        month = month_a + 12 - month_b
        return year * 12 + month
    else:
        year = year_a - year_b
        month = month_a - month_b
        return year * 12 + month

#年月相加
def plus_ym(a,b):
    year_a = int(a) / 100
    month_a = int(a) % 100
    month_b = month_a + b
    if month_b > 12:
        if month_b % 12 != 0:
            year = year_a + month_b / 12
            month = month_b % 12
            if month < 10:
                return str(year) + '0' + str(month)
            else:
                return str(year) + str(month)
        else:
            year = year_a + month_b / 12 - 1
            month = 12
            return str(year) + str(month)
    else:
        if month_b < 10:
            return str(year_a) + '0' + str(month_b)
        else:
            return str(year_a) + str(month_b)

#原始文件
rongliangbiangeng = u'F:/data/2014年至2016年容量变更数据.xls'
yongdianliang_o = u'F:/data/01--30个月每月用电量、电费.csv'
user_info_o = u'F:/data/用户全部基本信息.xls'

#新文件
new_rongliangbiangeng= u'F:/data/真容量变更数据.xls'
new_rongliang_2000 = u'F:/data/2000户容量变更数据.xls'
new_rongliang_1000 = u'F:/data/1000户容量变更数据.csv'

#文件加载
rlbg = pd.read_excel(rongliangbiangeng)
yongdianliang = pd.read_csv(yongdianliang_o,encoding='gbk')
user_info_all = pd.read_excel(user_info_o)



#数据预处理
#容量变更数据转化
rlbg[u'受理申请时间'] = rlbg[u'受理申请时间'].map(lambda x: parse(str(x)).date().strftime('%Y%m%d'))
rlbg[u'申请执行月'] = rlbg[u'受理申请时间'].map(lambda x: parse(str(x)).date().strftime('%Y%m'))
deal = {u'高压增容': 1, u'减容': 2, u'减容恢复': 3, u'暂停': 4, u'暂停恢复': 5}
rlbg[u'申请业务类型'] = rlbg[u'申请业务类型'].map(lambda x : deal[x])
rlbg[u'容量变更预测'] = 1
rlbg = rlbg.dropna()
rlbg = rlbg[rlbg[u'申请执行月'] > '201405']
del rlbg[u'受理申请时间']
rlbg.to_excel(new_rongliangbiangeng)
#用户信息转化
user_info_all = user_info_all[user_info_all[u'立户时间'].notnull()]
user_info_all[u'立户时间'] = user_info_all[u'立户时间'].map(lambda x: parse(str(x)).date().strftime('%Y%m'))
user_info = user_info_all[user_info_all[u'是否销户'] == u'否']


#用户编号
user_info_consno = user_info['CONS_NO'].tolist()
rlbg_consno = pd.read_excel(rongliangbiangeng)['CONS_NO'].drop_duplicates()
yongdianliang_consno = yongdianliang['CONS_NO'].drop_duplicates()




#构建预测为假的样本
#一、从具有容量变更的样本中随机抽取2000个案例，利用真实容量变更前几个月的容量变更情况作为预测为假的样本

yd_user_list = yongdianliang['CONS_NO'].tolist()
jiequ_list = rlbg['CONS_NO'].drop_duplicates().tolist()
jiequ_list = [val for val in jiequ_list if val in yd_user_list]
rlbg = rlbg[rlbg['CONS_NO'].isin(jiequ_list)]
jiequ = rlbg[rlbg[u'申请执行月'] > '201501']
jiequ = jiequ.as_matrix()#consno，原有容量，申请业务类型，申请执行月，容量变更预测
shuffle(jiequ)

user = []
rong = []
leixing = []
yuefen = []
yuce = []
for i in range(2000):
    no = jiequ[i][0]
    yyrl = jiequ[i][1]
    yf = jiequ[i][3]
    for j in range(5):
        user.append(no)
        rong.append(yyrl)
        leixing.append(j+1)
        yuefen.append(minus(yf,j+1))
        yuce.append(0)
dict_2000 = {'CONS_NO':user,u'原有容量':rong,u'申请业务类型':leixing,u'申请执行月':yuefen,u'容量变更预测':yuce}
jia_2000 = pd.DataFrame(dict_2000)
jia_2000.to_excel(new_rongliang_2000)

#二、从从未进行过容量变更的用户中选择1000户开户日期在2015年1月到2015年12月份用户，并且不是已销户的用户
# shuffle(user_info_consno)
# user_1000 = []
# rong_1000 = []
# leixing_1000 = []
# yuefen_1000 = []
# yuce_1000 = []
# select_1000 = []
# for i in range(1000):
#     if user_info_consno[i] not in yongdianliang_consno:
#         select_1000.append(int(user_info_consno[i]))
# select = user_info[user_info['CONS_NO'].isin(select_1000)][['CONS_NO',u'立户时间',u'合同容量']]
# select_group = select.groupby(['CONS_NO'])
# select_group = dict(list(select_group))
#
# for i in select_1000:
#
#     lihu = select_group[i].as_matrix()[0][1]
#     yuanyouyongliang = select_group[i].as_matrix()[0][2]
#     if  lihu < '201401':
#         for j in range(24):
#             for p in range(5):
#                 user_1000.append(i)
#                 rong_1000.append(yuanyouyongliang)
#                 leixing_1000.append(p+1)
#                 yuefen_1000.append(plus_ym('201406', j))
#                 yuce_1000.append(0)
#
#     else:
#         for j in range(get_month('201605',lihu) - 5):
#
#             for p in range(5):
#                 user_1000.append(i)
#                 rong_1000.append(yuanyouyongliang)
#                 leixing_1000.append(p + 1)
#                 yuefen_1000.append(plus_ym(lihu, j + 5))
#                 yuce_1000.append(0)
#
#
# jia_1000 = {'CONS_NO':user_1000,u'原有容量':rong_1000,u'申请业务类型':leixing_1000,u'申请执行月':yuefen_1000,u'容量变更预测':yuce_1000}
# jia_1000 = pd.DataFrame(jia_1000)
# jia_1000.to_csv(new_rongliang_1000,encoding='gbk')












