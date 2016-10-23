#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse



user_info_file = u'F:/data/用户基本信息.xls'

after_change = u'F:/data/转化后的容量变更记录明细数据.xls'
yongdianliang = u'F:/data/新的每月用电量.csv'
final = u'F:/data/测试真的容量变更记录明细数据.csv'
yongdianliang_data = pd.read_csv(yongdianliang,encoding='gbk')
user_info = pd.read_excel(user_info_file, encoding='gbk')
if __name__ == '__main__':
    after_change_data = pd.read_excel(after_change, encoding='gbk')
    after_change_data = after_change_data[after_change_data[u'申请执行月'] >= 201407]
    #
    after_change_data = after_change_data[after_change_data['CONS_NO'].isin(user_info['CONS_NO'].tolist())]
    after_change_data = after_change_data[after_change_data['CONS_NO'].isin(yongdianliang_data['CONS_NO'].tolist())]
    # after_change_data.to_csv(guodu,encoding='gbk')

    grouped = after_change_data.groupby('CONS_NO')
    group_date = after_change_data.groupby(u'申请执行月')
    pieces = dict(list(grouped))
    pieces_date = dict(list(group_date))
    data_matrix = after_change_data.as_matrix()
    print len(data_matrix)
    # 训练集列表
    after_change_data.to_csv(u'F:/data/一般测试真的容量变更记录明细数据.csv',encoding='gbk')
    first_distant = []  # 第一次容量变更距开户日期时长
    latest_1 = []  # 距上一次增容时长
    latest_2 = []  # 距上一次减容时长
    latest_3 = []  # 距上一次减容恢复时长
    latest_4 = []  # 距上一次暂停时长
    latest_5 = []  # 距上一次暂停恢复时
    target = []

    for i in range(len(after_change_data)):

        user = data_matrix[i][0]
        user_data = pieces[user]
        this_date = data_matrix[i][4]
        this_datetime = parse(str(int(data_matrix[i][2])))

        lihu_date = user_info[user_info['CONS_NO'] == user].as_matrix()[0][12]
        lihui_datetime = parse(str(lihu_date))
        days = (this_datetime - lihui_datetime).days

        last_1_date = user_data[user_data[u'申请执行月'] < this_date][user_data[u'申请业务类型'] == 1]
        if last_1_date.empty:
            latest_1_distant = 0
        else:
            length_1 = len(last_1_date[u'受理申请时间'].tolist())
            latest_1_date = parse(str(last_1_date[u'受理申请时间'].tolist()[length_1 - 1]))
            latest_1_distant = (this_datetime - latest_1_date).days

        last_2_date = user_data[user_data[u'申请执行月'] < this_date][user_data[u'申请业务类型'] == 2]
        if last_2_date.empty:
            latest_2_distant = 0
        else:
            length_2 = len(last_2_date[u'受理申请时间'].tolist())
            # print last_2_date[u'受理申请时间'].tolist()
            latest_2_date = parse(str(last_2_date[u'受理申请时间'].tolist()[length_2 - 1]))
            latest_2_distant = (this_datetime - latest_2_date).days

        last_3_date = user_data[user_data[u'申请执行月'] < this_date][user_data[u'申请业务类型'] == 3]
        if last_3_date.empty:
            latest_3_distant = 0
        else:
            length_3 = len(last_3_date[u'受理申请时间'].tolist())
            latest_3_date = parse(str(last_3_date[u'受理申请时间'].tolist()[length_3 - 1]))
            latest_3_distant = (this_datetime - latest_3_date).days

        last_4_date = user_data[user_data[u'申请执行月'] < this_date][user_data[u'申请业务类型'] == 4]
        if last_4_date.empty:
            latest_4_distant = 0
        else:
            length_4 = len(last_4_date[u'受理申请时间'].tolist())
            latest_4_date = parse(str(last_4_date[u'受理申请时间'].tolist()[length_4 - 1]))
            latest_4_distant = (this_datetime - latest_4_date).days

        last_5_date = user_data[user_data[u'申请执行月'] < this_date][user_data[u'申请业务类型'] == 5]
        if last_5_date.empty:
            latest_5_distant = 0
        else:
            length_5 = len(last_5_date[u'受理申请时间'].tolist())
            latest_5_date = parse(str(last_5_date[u'受理申请时间'].tolist()[length_5 - 1]))
            latest_5_distant = (this_datetime - latest_5_date).days

        first_distant.append(days)
        latest_1.append(latest_1_distant)
        latest_2.append(latest_2_distant)
        latest_3.append(latest_3_distant)
        latest_4.append(latest_4_distant)
        latest_5.append(latest_5_distant)
        target.append(1)
    #     print i
    #     print latest_4_distant
    #     print latest_5_distant
    # print '-------------------------------------'
    # print latest_1[23576]
    data = {u'第一次容量变更距开户时长':first_distant,u'距上一次增容时长':latest_1,u'距上一次减容时长':latest_2,u'距上一次减容恢复时长':latest_3,
            u'距上一次暂停时长':latest_4,u'距上一次暂停恢复时长':latest_5,u'是否容量变更':target
            }
    data = pd.DataFrame(data)
    data.to_csv(final,encoding='gbk')
    # after_change_data[u'第一次容量变更距开户时长'] = pd.Series(first_distant)
    # after_change_data[u'距上一次增容时长'] = pd.Series(latest_1)
    # after_change_data[u'距上一次减容时长'] = pd.Series(latest_2)
    # after_change_data[u'距上一次减容恢复时长'] = pd.Series(latest_3)
    # after_change_data[ u'距上一次暂停时长'] = pd.Series(latest_4)
    # after_change_data[u'距上一次暂停恢复时长'] = pd.Series(latest_5)
    # after_change_data[u'是否容量变更'] = pd.Series(target)
    # after_change_data.to_csv(final,encoding='gbk')