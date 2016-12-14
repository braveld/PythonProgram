#-*- coding: utf-8 -*-
#给样本集加入用户基本信息

import pandas as pd
from dateutil.parser import parse

#源文件
zhen = u'F:/data/真容量变更数据.xls'
jia_2000 = u'F:/data/2000户容量变更数据.xls'
jia_1000 = u'F:/data/1000户容量变更数据.csv'
user_info = u'F:/data/用户全部基本信息.xls'
sanfang = u'F:/data/是否三方协议.xls'

#加载文件
# zhen = pd.read_excel(zhen)
jia_2000 = pd.read_excel(jia_2000)
# jia_1000 = pd.read_csv(jia_1000,encoding='gbk')
user_info = pd.read_excel(user_info)
sanfang = pd.read_excel(sanfang)

#新文件
zhen_user = u'F:/data/真容量变更数据+用户基本信息.xls'
jia_2000_user = u'F:/data/2000户容量变更数据+用户基本信息.xls'
jia_1000_user = u'F:/data/1000户容量变更数据+用户基本信息.csv'


#预处理用户基本信息
del user_info[u'是否销户']
user_info = user_info[user_info[u'立户时间'].notnull()]
user_info = pd.merge(user_info,sanfang,on='CONS_NO',how='left')
user_info[u'立户时间'] = user_info[u'立户时间'].map(lambda x : parse(str(x)).date().strftime('%Y%m'))
user_info = user_info.fillna(0)



sanfang = {u'是': 1, u'否': 0,0:0}
dianyadengji = {u'交流10kV': 1, u'交流35kV': 2, u'交流110kV': 3, u'交流220kV': 4, u'交流6kV': 5,
                    u'交流380V': 6, u'交流220V':7}
kehuzhongyaodengji = { u'临时性重要用户': 1, u'二级重要用户': 2, u'一级重要用户': 3, u'特级重要用户':4,0:0}
shengchanbanci = {u'三班': 3, u'二班':2, u'单班': 1}
user_info[u'电压等级'] = user_info[u'电压等级'].map(lambda x: dianyadengji[x])
user_info[u'客户重要等级'] = user_info[u'客户重要等级'].map(lambda x: kehuzhongyaodengji[x])
user_info[u'是否三方协议'] = user_info[u'是否三方协议'].map(lambda x: sanfang[x])
user_info[u'生产班次'] = user_info[u'生产班次'].map(lambda x: shengchanbanci[x])


#拼接用户基本信息

# zhen = pd.merge(zhen,user_info,on='CONS_NO',how='left')
# jia_1000 = pd.merge(jia_1000,user_info,on='CONS_NO',how='left')
jia_2000 = pd.merge(jia_2000,user_info,on='CONS_NO',how='left')


# zhen.to_excel(zhen_user)
# jia_1000.to_csv(jia_1000_user,encoding='gbk')
jia_2000.to_excel(jia_2000_user)