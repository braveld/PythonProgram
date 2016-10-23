#-*- coding: utf-8 -*-

import pandas as pd
from dateutil.parser import parse
from random import shuffle

new_500 = u'F:/data/前1000户容量变更记录明细数据.xls'
zhong_1000 = u'F:/data/中间1000户容量变更记录明细数据.xls'
user_info_file = u'F:/data/用户基本信息.xls'

after_change = u'F:/data/转化后的容量变更记录明细数据.xls'
yongdianliang = u'F:/data/新的每月用电量.csv'
final = u'F:/data/测试容量变更记录明细数据.csv'


if __name__ == '__main__':
    zhong_1000_data = pd.read_excel(zhong_1000)
    yongdianliang_data = pd.read_csv(yongdianliang,encoding='gbk')
    after_change_data = pd.read_excel(after_change, encoding='gbk')
    after_change_data = after_change_data[after_change_data[u'申请执行月'] >= 201407]
    group_dianliang = yongdianliang_data.groupby('CONS_NO')

    after_change_data = after_change_data[after_change_data['CONS_NO'].isin(yongdianliang_data['CONS_NO'].tolist())]
    group1000 = zhong_1000_data.groupby('CONS_NO')

    user_info = pd.read_excel(user_info_file, encoding='gbk')
    grouped = after_change_data.groupby('CONS_NO')
    group_date = after_change_data.groupby(u'申请执行月')
    pieces = dict(list(grouped))
    pieces_date = dict(list(group_date))

    #获取1000个用户的数据，使得这1000个用户既有用电缴费记录，又有容量变更记录
    # a = []
    # b = []
    # for name, group in grouped:
    #     a.append(name)
    # print len(a)
    # for p in range(1000):
    #     b.append(a[p])
    # print len(b)
    # after_change_data = after_change_data[after_change_data['CONS_NO'].isin(b)]
    # after_change_data.to_excel(zhong_1000)

    #获取1000个用户
    a = []
    for name, group in group1000:
        a.append(name)

    #训练集列表
    users = []#用户编号
    dates = []#申请执行日期
    months = []#申请执行月
    leibie = []#申请业务类型
    type_label = [1, 2, 3, 4, 5]#1=增容，2=减容，3=减容恢复，4=暂停，5=暂停恢复
    yunxingrongliang = []#原有运行容量
    first_distant = []#第一次容量变更距开户日期时长
    latest_1 = []#距上一次增容时长
    latest_2 = []#距上一次减容时长
    latest_3 = []#距上一次减容恢复时长
    latest_4 = []#距上一次暂停时长
    latest_5 = []#距上一次暂停恢复时
    target = []
    c = []#获取所有的日期
    for name, group in group_date:
        c.append(name)
    for k in range(len(c)):
        print c[k]
        yes_name = pieces_date[c[k]]['CONS_NO'].tolist()  # 该时间点有记录的用户编号
        no_name = list(set(a).difference(set(yes_name)))  # 该时间点没有记录的用户编号

        for i in no_name:

            #计算原有运行容量和执行后运行容量
            d = pieces[i].sort([u'申请执行月'])
            d1 = d[d[u'申请执行月'] > c[k]]  #注意处理没有满足条件的情况
            if d1.empty:
                length = len(d[u'受理申请时间'].index) #必须统计的是index，不然会报int is not callable错误
                r = d[u'原有运行容量'].tolist()[length - 1]
            else:
                r = d1.sort([u'申请执行月']).as_matrix()[0][1]

            #计算第一次容量变更距开户日期时长
            first = pieces[i].sort([u'申请执行月']).as_matrix()[0][2] #第一次容量变更日期
            u = user_info[user_info['CONS_NO'] == i].as_matrix()
            lihu_date = parse(str(u[0][12]))
            first_datetime = parse(str(int(first)))
            days = (first_datetime - lihu_date).days #第一次容量变更距开户日期时长

            today = str(c[k]) + '10'
            today_datetime = parse(today)

            # 计算距上一次增容时长
            length_1_df = d[d[u'申请执行月'] < c[k]][d[u'申请业务类型'] == 1]
            if length_1_df.empty:
                latest_1_distant = 0
            else:
                length_1 = len(length_1_df[u'受理申请时间'].index)
                latest_1_date = parse(str(length_1_df[u'受理申请时间'].tolist()[length_1 - 1]))
                latest_1_distant = (today_datetime - latest_1_date).days

            # 计算距上一次减容时长
            length_2_df = d[d[u'申请执行月'] < c[k]][d[u'申请业务类型'] == 2]
            if length_2_df.empty:
                latest_2_distant = 0
            else:
                length_2 = len(length_2_df[u'受理申请时间'].index)
                latest_2_date = parse(str(length_2_df[u'受理申请时间'].tolist()[length_2 - 1]))
                latest_2_distant = (today_datetime - latest_2_date).days

            # 计算距上一次减容恢复时长
            length_3_df = d[d[u'申请执行月'] < c[k]][d[u'申请业务类型'] == 3]
            if length_3_df.empty:
                latest_3_distant = 0
            else:
                length_3 = len(length_3_df[u'受理申请时间'].index)
                latest_3_date = parse(str(length_3_df[u'受理申请时间'].tolist()[length_3 - 1]))
                latest_3_distant = (today_datetime - latest_3_date).days

            # 计算距上一次暂停时长
            length_4_df = d[d[u'申请执行月'] < c[k]][d[u'申请业务类型'] == 4]
            if length_4_df.empty:
                latest_4_distant = 0
            else:
                length_4 = len(length_4_df[u'受理申请时间'].index)
                latest_4_date = parse(str(length_4_df[u'受理申请时间'].tolist()[length_4 - 1]))
                latest_4_distant = (today_datetime - latest_4_date).days


            # 计算距上一次暂停恢复时长
            length_5_df = d[d[u'申请执行月'] < c[k]][d[u'申请业务类型'] == 5]
            if length_5_df.empty:
                latest_5_distant = 0
            else:
                length_5 = len(length_5_df[u'受理申请时间'].index)
                latest_5_date = parse(str(length_5_df[u'受理申请时间'].tolist()[length_5 - 1]))
                latest_5_distant = (today_datetime - latest_5_date).days

            for j in type_label:
                # if latest_1_distant or latest_2_distant or latest_3_distant or latest_4_distant or latest_5_distant:
                users.append(i)
                leibie.append(j)
                months.append(c[k])
                dates.append(c[k])
                yunxingrongliang.append(r)

                first_distant.append(days)
                latest_1.append(latest_1_distant)
                latest_2.append(latest_2_distant)
                latest_3.append(latest_3_distant)
                latest_4.append(latest_4_distant)
                latest_5.append(latest_5_distant)
                target.append(0)
    data = {'CONS_NO': users, u'申请业务类型': leibie, u'原有运行容量': yunxingrongliang,
            u'申请执行月': months,u'受理申请时间': dates,  u'第一次容量变更距开户时长': first_distant,
            u'距上一次增容时长':latest_1,u'距上一次减容时长':latest_2,u'距上一次减容恢复时长':latest_3,u'距上一次暂停时长':latest_4,u'距上一次暂停恢复时长':latest_5,
            u'是否容量变更':target}
    data = pd.DataFrame(data)

    data.to_csv(final,encoding='gbk')