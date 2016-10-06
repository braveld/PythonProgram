#-*- coding: utf-8 -*-

import pandas as pd

new_total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/用户基本信息表.xls'

merge_datafile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/容量变更相关数据/全量减容恢复次数.xls'

def merge_data(new_total,merge_datafile):
    merge_data = pd.read_excel(merge_datafile, encoding='gbk')

    totaldata = pd.read_excel(new_total, encoding='gbk')

    totaldata = pd.merge(totaldata, merge_data, on='CONS_NO', how='left')
    #
    # del totaldata[u'申请业务类型']
    del totaldata[u'   ']

    print totaldata.columns
    totaldata.to_excel(new_total)




if __name__ == '__main__':
    merge_data(new_total,merge_datafile)


