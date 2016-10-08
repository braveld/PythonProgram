#-*- coding: utf-8 -*-

import pandas as pd
new_total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/处理后的用户基本信息表.xls'
oringin_total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/用户基本信息.xls'
discretization = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/离散化表.xls'
new_discretization = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/新离散化表.xls'

totaldata = pd.read_excel(new_total,encoding='gbk')

if __name__ == '__main__':
    # new = totaldata.fillna(0)
    # new.to_excel(new_total)

    discretization_data = pd.read_excel(discretization,encoding='gbk')
    oringin_data = pd.read_excel(new_total,encoding='gbk')

    xiaohu = {u'是': u'已销户', u'否': u'未销户',0:u'没有销户记录'}

    fuhezhongyaodengji = {1: u'一级重要负荷', 2: u'2级重要负荷', 3: u'3级重要负荷',0:u'没有负荷重要记录'}

    sanfang = {u'是': u'是三方协议', u'否': u'非三方协议',0:u'没有三方记录'}

    discretization_data['CONS_NO'] = oringin_data['CONS_NO']
    discretization_data[u'是否销户'] = oringin_data[u'是否销户'].map(lambda x : xiaohu[x])
    # discretization_data['行业类别'] = oringin_data['行业类别']    #行业类别数目太多，跑到崩溃
    discretization_data[u'电压等级'] = oringin_data[u'电压等级']

    discretization_data[u'负荷重要等级'] = oringin_data[u'负荷重要等级'].map(lambda x : fuhezhongyaodengji[x])

    discretization_data[u'客户重要等级'] = oringin_data[u'客户重要等级']
    discretization_data[u'客户重要等级'][discretization_data[u'客户重要等级'] == 0] = u'普通客户'

    discretization_data[u'是否三方协议'] = oringin_data[u'是否三方协议'].map(lambda x : sanfang[x])
    discretization_data[u'生产班次'] = oringin_data[u'生产班次']

    print discretization_data.columns

    discretization_data.to_excel(new_discretization)