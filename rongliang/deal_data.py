#-*- coding: utf-8 -*-

import pandas as pd
new_total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/处理后的用户基本信息表.xls'
oringin_total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/用户基本信息.xls'

totaldata = pd.read_excel(new_total,encoding='gbk')

if __name__ == '__main__':
    new = totaldata.fillna(0)
    new.to_excel(new_total)


