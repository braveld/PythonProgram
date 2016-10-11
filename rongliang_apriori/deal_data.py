#-*- coding: utf-8 -*-

import pandas as pd
new_total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/处理后的用户基本信息表.xls'
oringin_total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/用户基本信息.xls'
discretization = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/离散化表.xls'
new_discretization = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/新去除0离散化表.xls'
new = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/新完整去除0离散化表.xls'
new_test = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/新完整去除0可挖掘离散化表.xls'
# totaldata = pd.read_excel(new_total,encoding='gbk')
oringin_data = pd.read_excel(new_discretization,encoding='gbk')

if __name__ == '__main__':
    # new = totaldata.fillna(0)
    # new.to_excel(new_total)

    #去除运行容量变更次数为0的记录
    discretization_data = pd.read_excel(new_test,encoding='gbk')
    # oringin_data = pd.read_excel(oringin_total,encoding='gbk')
    # oringin_data[[u'CONS_NO',u'运行容量变更次数']] = oringin_data[[u'CONS_NO',u'运行容量变更次数']].dropna()
    # oringin_data[[u'CONS_NO',u'运行容量变更次数']].dropna().to_excel(new_discretization)

    #连接
    # del totaldata[u'运行容量变更次数']
    # totaldata = pd.merge(origin_data, totaldata, on='CONS_NO', how='left')
    # totaldata.to_excel(new_discretization)
    xiaohu = {u'是': u'a1', u'否': u'a2',0:u'a3'}

    fuhezhongyaodengji = {1: u'b1', 2: u'b2', 3: u'b3',0:u'b4'}

    sanfang = {u'是': u'c1', u'否': u'c2',0:u'c3'}

    dianyadengji  = {u'交流10kV':'d1',u'交流35kV':'d2',u'交流110kV':'d3',u'交流220kV':'d4',u'交流6kV':'d5',u'交流380V':'d6',u'交流220V':'d7',0:'d8'}

    kehuzhongyaodengji = {u'普通客户':'e1',u'临时性重要用户':'e2',u'二级重要用户':'e3',u'一级重要用户':'e4',u'特级重要用户':'e5'}

    shengchanbanci = {u'三班':'f3',u'二班':'f2',u'单班':'f1',0:'f4'}

    discretization_data['CONS_NO'] = oringin_data['CONS_NO']
    discretization_data[u'是否销户'] = oringin_data[u'是否销户'].map(lambda x : xiaohu[x])
    # discretization_data['行业类别'] = oringin_data['行业类别']    #行业类别数目太多，跑到崩溃
    discretization_data[u'电压等级'] = oringin_data[u'电压等级'].map(lambda x : dianyadengji[x])

    discretization_data[u'负荷重要等级'] = oringin_data[u'负荷重要等级'].map(lambda x : fuhezhongyaodengji[x])

    oringin_data[u'客户重要等级'][oringin_data[u'客户重要等级'] == 0] = u'普通客户'
    discretization_data[u'客户重要等级'] = oringin_data[u'客户重要等级'].map(lambda x : kehuzhongyaodengji[x])


    discretization_data[u'是否三方协议'] = oringin_data[u'是否三方协议'].map(lambda x : sanfang[x])
    discretization_data[u'生产班次'] = oringin_data[u'生产班次'].map(lambda x : shengchanbanci[x])

    print discretization_data.columns

    discretization_data.to_excel(new_test)