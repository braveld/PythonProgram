#-*- coding: utf-8 -*-

import pandas as pd

total = u'F:/data/测试容量变更记录明细数据.csv'
user_info_file = u'F:/data/用户基本信息.xls'
user_info = pd.read_excel(user_info_file, encoding='gbk')
total_data = pd.read_csv(total,encoding='gbk')
if __name__ == '__main__':
    # user_info = user_info.fillna(0)
    #
    # sanfang = {u'是': 1, u'否': 0,0:0}
    #
    # dianyadengji = {u'交流10kV': 1, u'交流35kV': 2, u'交流110kV': 3, u'交流220kV': 4, u'交流6kV': 5,
    #                 u'交流380V': 6, u'交流220V':7}
    #
    # kehuzhongyaodengji = { u'临时性重要用户': 1, u'二级重要用户': 2, u'一级重要用户': 3, u'特级重要用户':4,0:0}
    #
    # shengchanbanci = {u'三班': 3, u'二班':2, u'单班': 1}
    #
    # user_info[u'电压等级'] = user_info[u'电压等级'].map(lambda x: dianyadengji[x])
    # user_info[u'客户重要等级'] = user_info[u'客户重要等级'].map(lambda x: kehuzhongyaodengji[x])
    # user_info[u'是否三方协议'] = user_info[u'是否三方协议'].map(lambda x: sanfang[x])
    # user_info[u'生产班次'] = user_info[u'生产班次'].map(lambda x: shengchanbanci[x])
    # user_info.to_excel(user_info_file)
    total_data = pd.merge(total_data,user_info,on='CONS_NO', how='left')
    total_data.to_csv(total,encoding='gbk')