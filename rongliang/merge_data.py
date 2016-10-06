#-*- coding: utf-8 -*-

import pandas as pd
import os

new_total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/用户基本信息表.xls'

oringin_total = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/关联性指标数据/用户基本信息.xls'

merge_datafile = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/容量变更相关数据/变更次数'

merge_dir = '/home/bigdata/Downloads/data/luodi/容量变更预测指标数据/容量变更相关数据/变更次数'

def file_name(file_dir):
    list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            list.append(os.path.join(root, file))
    return list
        # return files #当前路径下所有非目录子文件

def merge_data(oringin_total,merge_datafile):
    merge_data = pd.read_excel(merge_datafile, encoding='gbk')

    totaldata = pd.read_excel(oringin_total, encoding='gbk')

    totaldata = pd.merge(totaldata, merge_data, on='CONS_NO', how='left')
    #
    if u'申请业务类型' in totaldata.columns:
        del totaldata[u'申请业务类型']
    if u'   ' in totaldata.columns:
        del totaldata[u'   ']
    if u'   _y' in totaldata.columns:
        del totaldata[u'   _y']
    if u'   _x' in totaldata.columns:
        del totaldata[u'   _x']

    print totaldata.columns
    totaldata.to_excel(oringin_total)




if __name__ == '__main__':
    filenames = file_name(merge_dir)
    for filename in filenames:

        merge_data(oringin_total,filename)


