#-*- coding: utf-8 -*-
#计算日期之间的相加减

#年月减法,
# a 被减年月
# b 月份数
def minus(a,b):
    year = int(a) / 100
    month = int(a) % 100
    y = 0
    m = 0
    if month <= int(b):
        m = 12 - int(b) + month
        y = year -1
        if m < 10:
            return str(y) + '0' + str(m)
        else:
            return  str(y) + str(m)
    else:
        m = month - int(b)
        y = year
        if m < 10:
            return str(y) + '0' + str(m)
        else:
            return str(y) + str(m)


#年月相减得月份
# a 被减年月
# b 减年月
def get_month(a,b):
    year_a = int(a) / 100
    month_a = int(a) % 100
    year_b = int(b) / 100
    month_b = int(b) % 100

    if month_a < month_b:
        year = year_a - year_b -1
        month = month_a + 12 - month_b
        return year * 12 + month
    else:
        year = year_a - year_b
        month = month_a - month_b
        return year * 12 + month

#年月相加
def plus_ym(a,b):
    year_a = int(a) / 100
    month_a = int(a) % 100
    month_b = month_a + b
    if month_b > 12:
        if month_b % 12 != 0:
            year = year_a + month_b / 12
            month = month_b % 12
            if month < 10:
                return str(year) + '0' + str(month)
            else:
                return str(year) + str(month)
        else:
            year = year_a + month_b / 12 - 1
            month = 12
            return str(year) + str(month)
    else:
        if month_b < 10:
            return str(year_a) + '0' + str(month_b)
        else:
            return str(year_a) + str(month_b)

#年月相对应
def ny_duiying(a):
    dates = [201401, 201402, 201403, 201404, 201405, 201406, 201407, 201408, 201409, 201410, 201411, 201412, 201501,
             201502, 201503, 201504, 201505, 201506, 201507, 201508,
             201509, 201510, 201511, 201512,
             201601, 201602, 201603, 201604, 201605, 201606]
    for j in range(30):
        if dates[j] == int(a):
            return j