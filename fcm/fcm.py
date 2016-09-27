#-*- coding: utf-8 -*-
from numpy import  *

 # 计算样本点距离聚类中心的距离
 # 输入：
 #   center     ---- 聚类中心array
 #   data       ---- 样本点array
 # 输出：
 #   out        ---- 距离
def euclDistance(data, center):
    return sqrt(sum(power(data - center, 2))) #sqrt,sum,power function are all imported from numpy


# 采用模糊C均值对数据集data聚为cluster_n类
# input:
#     data - --- n x m矩阵, 表示n个样本, 每个样本具有m的维特征值
#     N_cluster - --- 标量, 表示聚合中心数目, 即类别数
#     options - --- 4x1矩阵，其中
#         options(1):  隶属度矩阵U的指数,模糊度， > 1(缺省值: 2.0)
#         options(2):  最大迭代次数(缺省值: 100)
#         options(3):  隶属度最小变化量, 迭代终止条件(缺省值: 1e-5)
#         options(4):  每次迭代是否输出信息标志(缺省值: 1) 0 or 1
#
# output：
#     center - --- 聚类中心
#     U - --- 隶属度矩阵
#     obj_fcn - --- 目标函数值
def FCMClustering(data,N_cluster,options=[2,100,1e-5,1]):
    m = options[0]  #模糊度
    max_interation = options[1] #最大迭代次数
    min_change = options[2] #隶属度最小变化量, 迭代终止条件
    print_flag = options[3] #每次迭代是否输出信息标志

    count = 0

    U = initial(data,N_cluster)     #随机生成样本隶属矩阵
    center = cluster_center_update(U,data)  #

    while(count < max_interation):
        v = caculateV(U, data, center, m)
        if print_flag == 1:
            print count,v
            print '--------------------'
        if v < min_change :
            break
        U = updateU(center, data, m)
        center = cluster_center_update(U, data)
    return center, U, v



# 随机生成样本隶属矩阵
# input:
#   dataset   n x m矩阵, 表示n个样本, 每个样本具有m的维特征值
#   N_cluster   聚类中心的数量
# output:
#   data    隶属矩阵
def initial(dataset,N_cluster):
    numSamples, dim = dataset.shape
    data = matrix(random.rand(dim,N_cluster))   #随机生成一个隶属矩阵
    # 隶属度数据归一化处理
    #data.dtype = float
    sum_columns = data.sum(1).tolist()
    for i in range(size(sum_columns)):
        data[i] = data[i] / float(sum_columns[i][0])
    return data

# 初始化聚类中心
# input:
#    U  隶属矩阵matrix
#   dataset     n x m矩阵, 表示n个样本, 每个样本具有m的维特征值 matrix
# output:
#   new_cluster_center  聚类中心
def cluster_center_update(U,dataset):
    numSamples, dim = U.shape
    new_center = []
    for i in range(dim):
        new_center.append((U.T[i] * dataset / float(sum(U.T[i]))).tolist()[0])
    new_cluster_center = matrix(new_center)
    return new_cluster_center

#计算各个样本到各个聚类中心的距离
# input:
#   cluster_center  聚类中心
#   dataset n x m矩阵, 表示n个样本, 每个样本具有m的维特征值
# output:
#   d_matrix    各个样本到各个聚类中心的距离矩阵
def caculateDistance(cluster_center,dataset):
    size_dataset = size(dataset)
    size_cluster = size(cluster_center)
    d = []
    for i in range(size_dataset):
        for j in range(size_cluster):
            d.append(euclDistance(dataset[i], cluster_center[j]))
    d_matrix = array(d).reshape(size_dataset, size_cluster)
    return d_matrix

# 更新隶属度矩阵
# input
#    cluster_center     聚类中心
#    dataset    n x m矩阵, 表示n个样本, 每个样本具有m的维特征值
#    m      模糊度
# output:
#   matrix  更新的隶属度矩阵
def updateU(cluster_center,dataset,m):
    new = []

    size_cluster = size(cluster_center)
    size_dataset = size(dataset)


    for i in range(size_dataset):
        a = []
        s = 0.0
        for j in range(size_cluster):
            d = euclDistance(dataset[i],cluster_center[j])
            a.append(d)

        for p in range(size_cluster):
            for o in a:
                s = s + power((float(a[p]) / o),(2.0 / (m - 1)))
        new.append(1.0 / s)
    return matrix(array(new).reshape(size_dataset,size_cluster))

#计算价值函数的值
# input:
#   U       隶属度矩阵
#   dataset     n x m矩阵, 表示n个样本, 每个样本具有m的维特征值
#   cluster_center      聚类中心
#   m       模糊度
def caculateV(U,dataset,cluster_center,m):

    v = sum(power(U,m) * power(caculateDistance(cluster_center,dataset),2))
    return v
