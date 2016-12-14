#-*- coding: utf-8 -*-
#使用函数
import numpy as np
import pandas as pd
#分层抽样
#input dataframe['data'],dataframe['category']
#outpt dataframe['data']

def stratified_sampling(data,category,percent):
    cateforys = data[category].drop_duplicates().tolist()
    after = pd.DataFrame()
    for i in cateforys:
        tmp = data[data[category] == i]
        # tmp.index = range(len(tmp))

        if len(tmp) < percent:
            percent =  10
        if len(tmp) < 50:
            percent = 1
        print i
        print len(tmp)
        print percent
        print '==============='
        sampler = np.random.randint(0, len(tmp), size=len(tmp) / percent)
        tmp = data[data.index.isin(sampler)]
        after = pd.concat([after,tmp])
    after.index = range(len(after))
    return after


if __name__ == '__main__':
    data = {'CONS_NO':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],'category':[1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1]}
    data = pd.DataFrame(data)
    print stratified_sampling(data,'category',5)



