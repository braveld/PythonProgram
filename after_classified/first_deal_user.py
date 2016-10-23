#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse

new_yongdianlaing_datafile = u'F:/data/新的每月用电量.csv'
user_info = u'F:/data/用户基本信息.xls'
all_info = u'F:/data/汇总宽表.xlsx'
user_all = u'F:/data/用户全部基本信息.xls'
get_500 = u'F:/data/转化后的500户容量变更记录明细数据.xls'
all_rongliang = u'F:/data/转化后的容量变更记录明细数据.xls'
final = u'F:/data/样本集.csv'
last = u'F:/data/新的最终样本集.csv'
duofenlei = u'F:/data/多分类样本集.csv'
quchu = u'F:/data/去除第一次样本集.csv'
zengrong = u'F:/data/1.csv'
jianrong = u'F:/data/2.csv'
jianronghuifu = u'F:/data/3.csv'
zanting = u'F:/data/4.csv'
zantinghuifu = u'F:/data/5.csv'
hah = u'F:/data/0.csv'
guodu = u'F:/data/过度.csv'


def change(x):
    a = str(x) + '01'
    return a


if __name__ == '__main__':
    # user_info_data = pd.read_excel(user_info)
    # user_all_data = pd.read_excel(user_all)[['CONS_NO',u'客户服务中心或县级单位',u'立户时间',u'用电类别']]
    # user_info_data = pd.merge(user_info_data,user_all_data,on='CONS_NO',how='left')
    # user_info_data.to_excel(user_info)

    # user_all_data = pd.read_excel(all_info)
    # user_all_data = pd.merge(user_all_data,user_info_data,on='CONS_NO',how='left')
    # user_all_data.to_csv(final,encoding='gbk')

    # yangben = pd.read_csv(final,encoding='gbk')
    # yangben = yangben.fillna(0)
    # # hangye = {u'1.电力、热力的生产和供应业':1,u'2.燃气生产和供应业':2,u'⑵建筑安装业':3,u'3.畜牧业':4,u'⑶建筑装饰业':5,
    # #           u'6.其他采矿业':6,u'⑹管道运输业':7,u'焙烤食品制造':8,u'泵、阀门、压缩机及类似机械的制造':9,u'玻璃保温容器制造':10,
    # #           u'玻璃纤维及制品制造':11,u'玻璃仪器制造':12,u''}
    # diqu = {u'承德供电公司':1,u'廊坊供电公司':2,u'秦皇岛供电公司':3,u'唐山供电公司':4,u'张家口供电公司':5}
    # yongdianleibie = {u'大工业其它优待':1,u'大工业用电':2,u'大工业中小化肥':3,0:0}
    # yangben[u'客户服务中心或县级单位'] = yangben[u'客户服务中心或县级单位'].map(lambda x : diqu[x])
    # yangben[u'用电类别'] = yangben[u'用电类别'].map(lambda x:yongdianleibie[x])
    # # print yangben[u'用电类别'].value_counts()
    # yangben.to_csv(last,encoding='gbk')

    # yangben = pd.read_csv(last, encoding='gbk')
    # yangben = yangben[yangben[u'是否容量变更'] == 0]
    # yangben[u'申请业务类型'] = 0
    # yangben.to_csv(duofenlei,encoding='gbk')

    # yangben = pd.read_csv(last, encoding='gbk')
    # yangben = yangben[yangben[u'距上一次增容时长'] + yangben[u'距上一次减容时长'] + yangben[u'距上一次减容恢复时长'] + yangben[u'距上一次暂停时长'] + yangben[u'距上一次暂停恢复时长'] != 0]
    # yangben.to_csv(quchu,encoding='gbk')

    # yangben = pd.read_csv(last, encoding='gbk')
    # yangben = yangben[yangben[u'申请业务类型'] < 3]
    # yangben = yangben[yangben[u'申请业务类型'] != 1]
    # yangben.to_csv(jianrong,encoding='gbk')

    # yangben = pd.read_csv(last, encoding='gbk')
    # yangben = yangben[yangben[u'申请业务类型'] < 4]
    # yangben = yangben[yangben[u'申请业务类型'] != 1]
    # yangben = yangben[yangben[u'申请业务类型'] != 2]
    # yangben.to_csv(jianronghuifu,encoding='gbk')

    # yangben = pd.read_csv(last, encoding='gbk')
    # yangben = yangben[yangben[u'申请业务类型'] < 5]
    # yangben = yangben[yangben[u'申请业务类型'] != 1]
    # yangben = yangben[yangben[u'申请业务类型'] != 2]
    # yangben = yangben[yangben[u'申请业务类型'] != 3]
    # yangben.to_csv(zanting, encoding='gbk')

    # yangben = pd.read_csv(last, encoding='gbk')
    # # yangben = yangben[yangben[u'申请业务类型'] < 5]
    # yangben = yangben[yangben[u'申请业务类型'] != 1]
    # yangben = yangben[yangben[u'申请业务类型'] != 2]
    # yangben = yangben[yangben[u'申请业务类型'] != 3]
    # yangben = yangben[yangben[u'申请业务类型'] != 4]
    # yangben.to_csv(zantinghuifu, encoding='gbk')

    yangben = pd.read_csv(last, encoding='gbk')
    yangben = yangben[yangben[u'是否容量变更'] == 0]
    yangben[u'受理申请时间'] =yangben[u'受理申请时间'].map(lambda x : change(x))
    yangben.to_csv(guodu, encoding='gbk')

    # yangben = pd.read_csv(last, encoding='gbk')
    # list = [u'前六个月',u'前五个月',u'前四个月',u'前三个月',u'前二个月',u'前一个月']
    # ke = yangben[list].T
    #
    # yangben['total'] = ke.sum()
    # yangben['mean'] = ke.mean()
    #
    # yangben[u'方差'] = ke.var()
    # yangben.to_csv(last, encoding='gbk')