#-*- coding: utf-8 -*-
#给所有训练集打上用电量的标签，“行为”、“程度”、
import pandas as pd

#源文件
zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业.csv'
jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业.csv'
jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业.csv'

#新文件
new_zhen = u'F:/data/真容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签.csv'
new_jia_1000 = u'F:/data/1000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签.csv'
new_jia_2000 = u'F:/data/2000户容量变更数据+用户基本信息+去除没有用电记录的+前五个月+时间距离+用电增长+离散度+转化行业+用电行为标签.csv'

#加载文件
zhen = pd.read_csv(zhen,encoding='gbk')
jia_1000 = pd.read_csv(jia_1000,encoding='gbk')
jia_2000 = pd.read_csv(jia_2000,encoding='gbk')



#处理方式
def xingwei(x):
    if x == 0:
        return u'没有用电'
    if x == -1:
        return u'没有记录'
    if 0 < x < 20110:
        return u'用电量极低'
    if 20110 < x < 133392:
        return u'用电量低'
    if 133392 < x < 1021520:
        return u'用电量中'
    if 1021520 < x < 5064800:
        return u'用电量高'
    if 5064800 < x:
        return u'用电量极高'

def chengdu(x):
    #用电量极低
    if x == 0:
        return 0
    if x == -1:
        return -1
    if 0 < x <= 1884:
        return 1
    if 1884 < x <= 3831:
        return 2
    if 3831 < x <= 5796:
        return 3
    if 5796 < x <= 7795:
        return 4
    if 7795 < x <= 9836:
        return 5
    if 9836 < x <= 11899:
        return 6
    if 11899 < x <= 13928:
        return 7
    if 13928 < x <= 15930:
        return 8
    if 15930 < x <= 17986:
        return 9
    if 17986 < x <= 20109:
        return 10

    #用电量低
    if 20109 < x <= 25050:
        return 11
    if 25050 < x <= 30018:
        return 12
    if 30018 < x <= 35025:
        return 13
    if 35025 < x <= 40132:
        return 14
    if 40132 < x <= 45336:
        return 15
    if 45336 < x <= 58920:
        return 16
    if 58920 < x <= 72930:
        return 17
    if 72930 < x <= 87204:
        return 18
    if 87204 < x <= 101780:
        return 19
    if 101780 < x <= 117064:
        return 20
    if 117064 < x <= 133391:
        return 21


    #用电量中
    if 133391 < x <= 160450:
        return 22
    if 160450 < x <= 189879:
        return 23
    if 189879 < x <= 222205:
        return 24
    if 222205 < x <= 257117:
        return 25
    if 257117 < x <= 293964:
        return 26
    if 293964 < x <= 332700:
        return 27
    if 332700 < x <= 465300:
        return 28
    if 465300 < x <= 624600:
        return 29
    if 624600 < x <= 810660:
        return 30
    if 810660 < x <= 1021317:
        return 31

    #用电量高
    if 1021317 < x <= 1195560:
        return 32
    if 1195560 < x <= 1384440:
        return 33
    if 1384440 < x <= 1589865:
        return 34
    if 1589865 < x <= 1812420:
        return 35
    if 1812420 < x <= 2050560:
        return 36
    if 2050560 < x <= 2648320:
        return 37
    if 2648320 < x <= 3316440:
        return 38
    if 3316440 < x <= 4112880:
        return 39
    if 4112880 < x <= 5063520:
        return 40

    #用电量超高
    if 5063520 < x <= 12903200:
        return 41
    if 12903200 < x <= 25731200:
        return 42
    if 25731200 < x <= 43150800:
        return 43
    if 43150800 < x <= 63769200:
        return 44
    if 63769200 < x <= 90191200:
        return 45
    if 90191200 < x <= 149424000:
        return 46
    if 149424000 < x <= 269842100:
        return 47
    if 269842100 < x:
        return 48

#转化
# zhen[u'近一个月用电标签'] = zhen[u'近一个月用电量'].map(lambda x : xingwei(x))
# zhen[u'近二个月用电标签'] = zhen[u'近二个月用电量'].map(lambda x : xingwei(x))
# zhen[u'近三个月用电标签'] = zhen[u'近三个月用电量'].map(lambda x : xingwei(x))
# zhen[u'近四个月用电标签'] = zhen[u'近四个月用电量'].map(lambda x : xingwei(x))
# zhen[u'近五个月用电标签'] = zhen[u'近五个月用电量'].map(lambda x : xingwei(x))
#
# zhen[u'近一个月用电程度'] = zhen[u'近一个月用电量'].map(lambda x : chengdu(x))
# zhen[u'近二个月用电程度'] = zhen[u'近二个月用电量'].map(lambda x : chengdu(x))
# zhen[u'近三个月用电程度'] = zhen[u'近三个月用电量'].map(lambda x : chengdu(x))
# zhen[u'近四个月用电程度'] = zhen[u'近四个月用电量'].map(lambda x : chengdu(x))
# zhen[u'近五个月用电程度'] = zhen[u'近五个月用电量'].map(lambda x : chengdu(x))
#
# zhen.to_csv(new_zhen,encoding='gbk')

# jia_1000[u'近一个月用电标签'] = jia_1000[u'近一个月用电量'].map(lambda x : xingwei(x))
# jia_1000[u'近二个月用电标签'] = jia_1000[u'近二个月用电量'].map(lambda x : xingwei(x))
# jia_1000[u'近三个月用电标签'] = jia_1000[u'近三个月用电量'].map(lambda x : xingwei(x))
# jia_1000[u'近四个月用电标签'] = jia_1000[u'近四个月用电量'].map(lambda x : xingwei(x))
# jia_1000[u'近五个月用电标签'] = jia_1000[u'近五个月用电量'].map(lambda x : xingwei(x))
#
# jia_1000[u'近一个月用电程度'] = jia_1000[u'近一个月用电量'].map(lambda x : chengdu(x))
# jia_1000[u'近二个月用电程度'] = jia_1000[u'近二个月用电量'].map(lambda x : chengdu(x))
# jia_1000[u'近三个月用电程度'] = jia_1000[u'近三个月用电量'].map(lambda x : chengdu(x))
# jia_1000[u'近四个月用电程度'] = jia_1000[u'近四个月用电量'].map(lambda x : chengdu(x))
# jia_1000[u'近五个月用电程度'] = jia_1000[u'近五个月用电量'].map(lambda x : chengdu(x))
#
# jia_1000.to_csv(new_jia_1000,encoding='gbk')

jia_2000[u'近一个月用电标签'] = jia_2000[u'近一个月用电量'].map(lambda x : xingwei(x))
jia_2000[u'近二个月用电标签'] = jia_2000[u'近二个月用电量'].map(lambda x : xingwei(x))
jia_2000[u'近三个月用电标签'] = jia_2000[u'近三个月用电量'].map(lambda x : xingwei(x))
jia_2000[u'近四个月用电标签'] = jia_2000[u'近四个月用电量'].map(lambda x : xingwei(x))
jia_2000[u'近五个月用电标签'] = jia_2000[u'近五个月用电量'].map(lambda x : xingwei(x))

jia_2000[u'近一个月用电程度'] = jia_2000[u'近一个月用电量'].map(lambda x : chengdu(x))
jia_2000[u'近二个月用电程度'] = jia_2000[u'近二个月用电量'].map(lambda x : chengdu(x))
jia_2000[u'近三个月用电程度'] = jia_2000[u'近三个月用电量'].map(lambda x : chengdu(x))
jia_2000[u'近四个月用电程度'] = jia_2000[u'近四个月用电量'].map(lambda x : chengdu(x))
jia_2000[u'近五个月用电程度'] = jia_2000[u'近五个月用电量'].map(lambda x : chengdu(x))

jia_2000.to_csv(new_jia_2000,encoding='gbk')








