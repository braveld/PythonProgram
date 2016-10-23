#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
new_yongdianlaing_datafile = u'F:/data/新的每月用电量.csv'
new = u'F:/data/用电模式.csv'
fenlei = u'F:/data/以总用电量分类后的用电模式.csv'
yongdian_data = pd.read_csv(new_yongdianlaing_datafile,encoding='gbk')
fenlei_data = pd.read_csv(fenlei,encoding='gbk')

# lei_1 = fenlei_data[fenlei_data['leibie'] == 1].head()['CONS_NO'].tolist()
# lei_2 = fenlei_data[fenlei_data['leibie'] == 2].head()['CONS_NO'].tolist()
lei_4 = fenlei_data[fenlei_data['leibie'] == 4]['CONS_NO'].tolist()
# lei_5 = fenlei_data[fenlei_data['leibie'] == 5].head()['CONS_NO'].tolist()
# lei_6 = fenlei_data[fenlei_data['leibie'] == 6].head()['CONS_NO'].tolist()
# lei_7 = fenlei_data[fenlei_data['leibie'] == 7].head()['CONS_NO'].tolist()
# lei_0 = fenlei_data[fenlei_data['leibie'] == 0].head()['CONS_NO'].tolist()

if __name__ == '__main__':
    # columns = [201401,201402,201403,201404,201405,201406,201407, 201408, 201409, 201410, 201411, 201412, 201501, 201502, 201503, 201504, 201505, 201506, 201507, 201508,
    #      201509, 201510, 201511, 201512,
    #      201601, 201602, 201603, 201604, 201605, 201606]
    grouped = yongdian_data.groupby('CONS_NO')
    d = {}
    users = []
    for name,group in grouped:
        users.append(name)
        data = group[u'总电量'].tolist()
        d[name] = data
    old = pd.DataFrame(d)
    chaogao = old[lei_4]
    # chaogao.index = columns
    chaogao.plot()
    plt.show()

