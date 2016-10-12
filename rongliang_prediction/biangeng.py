#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse



user_info_file = u'F:/data/用户基本信息.xls'

after_change = u'F:/data/转化后的500户容量变更记录明细数据.xls'

final = u'F:/data/测试真的容量变更记录明细数据.csv'


if __name__ == '__main__':
    after_change_data = pd.read_excel(after_change, encoding='gbk')
    user_info = pd.read_excel(user_info_file, encoding='gbk')
    grouped = after_change_data.groupby('CONS_NO')
    group_date = after_change_data.groupby(u'申请执行月')
    pieces = dict(list(grouped))
    pieces_date = dict(list(group_date))

    # 获取500个用户
    a = []
    for name, group in grouped:
        a.append(name)

    # 训练集列表
    first_distant = []  # 第一次容量变更距开户日期时长
    latest_2 = []  # 距上一次减容时长
    latest_3 = []  # 距上一次减容恢复时长
    latest_4 = []  # 距上一次暂停时长
    latest_5 = []  # 距上一次暂停恢复时
    target = []
    for i in a:
        d = pieces[i]
        # 计算第一次容量变更距开户日期时长
        today = d.as_matrix()[0][4]
        u = user_info[user_info['CONS_NO'] == i].as_matrix()
        lihu_date = parse(str(u[0][7]))
        today_datetime = parse(str(today))
        days = (today_datetime - lihu_date).days  # 第一次容量变更距开户日期时长

        for q in d.as_matrix():
            this_date = q[4]
            # 计算距上一次减容时长
            length_2_df = d[d[u'申请执行起日期'] < this_date][d[u'申请业务类型'] == 2]
            if length_2_df.empty:
                latest_2_distant = 0
            else:
                length_2 = len(length_2_df[u'申请执行起日期'].index)
                latest_2_date = parse(str(length_2_df[u'申请执行起日期'].tolist()[length_2 - 1]))
                latest_2_distant = (today_datetime - latest_2_date).days

            # 计算距上一次减容恢复时长
            length_3_df = d[d[u'申请执行月'] < this_date][d[u'申请业务类型'] == 3]
            if length_3_df.empty:
                latest_3_distant = 0
            else:
                length_3 = len(length_3_df[u'申请执行起日期'].index)
                latest_3_date = parse(str(length_3_df[u'申请执行起日期'].tolist()[length_3 - 1]))
                latest_3_distant = (today_datetime - latest_3_date).days

            # 计算距上一次暂停时长
            length_4_df = d[d[u'申请执行月'] < this_date][d[u'申请业务类型'] == 4]
            if length_4_df.empty:
                latest_4_distant = 0
            else:
                length_4 = len(length_4_df[u'申请执行起日期'].index)
                latest_4_date = parse(str(length_4_df[u'申请执行起日期'].tolist()[length_4 - 1]))
                latest_4_distant = (today_datetime - latest_4_date).days

            # 计算距上一次暂停恢复时长
            length_5_df = d[d[u'申请执行月'] < this_date][d[u'申请业务类型'] == 5]
            if length_5_df.empty:
                latest_5_distant = 0
            else:
                length_5 = len(length_5_df[u'申请执行起日期'].index)
                latest_5_date = parse(str(length_5_df[u'申请执行起日期'].tolist()[length_5 - 1]))
                latest_5_distant = (today_datetime - latest_5_date).days

            first_distant.append(days)
            latest_2.append(latest_2_distant)
            latest_3.append(latest_3_distant)
            latest_4.append(latest_4_distant)
            latest_5.append(latest_5_distant)
            target.append(1)


    data = { u'第一次容量变更距开户时长': first_distant, u'距上一次减容时长': latest_2,
             u'距上一次减容恢复时长': latest_3, u'距上一次暂停时长': latest_4,u'距上一次暂停恢复时长': latest_5,u'是否容量变更': target}
    after_change_data[u'第一次容量变更距开户时长'] = pd.Series(first_distant)
    after_change_data[u'距上一次减容时长'] = pd.Series(latest_2)
    after_change_data[u'距上一次减容恢复时长'] = pd.Series(latest_3)
    after_change_data[ u'距上一次暂停时长'] = pd.Series(latest_4)
    after_change_data[u'距上一次暂停恢复时长'] = pd.Series(latest_5)
    after_change_data[u'是否容量变更'] = pd.Series(target)

    after_change_data.to_csv(final, encoding='gbk')