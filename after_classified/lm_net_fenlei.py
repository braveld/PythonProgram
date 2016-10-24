#-*- coding: utf-8 -*-
import pandas as pd #导入数据分析库
quchu = u'F:/data/去除第一次样本集.csv'
zengrong = u'F:/data/1.csv'
jianrong = u'F:/data/2.csv'
jianronghuifu = u'F:/data/3.csv'
zanting = u'F:/data/4.csv'
zantinghuifu = u'F:/data/5.csv'
data = pd.read_csv(zanting,encoding='gbk') #读取数据，数据的前三列是特征，第四列是标签
deal = {u'年初':1,u'年中':2,u'年末':3}
data[u'阶段'] = data[u'阶段'].map(lambda x : deal[x])
train = data[data[u'申请执行月'] < 201602][u'是否容量变更']
test = data[data[u'申请执行月'] > 201602][u'是否容量变更']
test = test.tolist()
train = train.tolist()
# data = (data - data.mean(axis=0)) / (data.std(axis=0))
train_data = data[data[u'申请执行月'] < 201602]
test_data = data[data[u'申请执行月'] > 201602]
del train_data[u'申请执行月']
del test_data[u'申请执行月']
train_data = train_data.as_matrix()
test_data = test_data.as_matrix()
train_data = (train_data - train_data.mean(axis=0)) / (train_data.std(axis=0))
test_data = (test_data - test_data.mean(axis=0)) / (test_data.std(axis=0))

from keras.models import Sequential #导入神经网络初始化函数
from keras.layers.core import Dense, Activation #导入神经网络层函数、激活函数

netfile = '/home/bigdata/Downloads/tmp/net.model' #构建的神经网络模型存储路径

net = Sequential() #建立神经网络
net.add(Dense(10, input_dim=3)) #添加输入层（3节点）到隐藏层（10节点）的连接
net.add(Activation('relu')) #隐藏层使用relu激活函数
net.add(Dense(1, input_dim=10)) #添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation('sigmoid')) #输出层使用sigmoid激活函数
net.compile(loss = 'binary_crossentropy', optimizer = 'adam', class_mode = "binary") #编译模型，使用adam方法求解

net.fit(train_data[:,:2], train, nb_epoch=100, batch_size=5) #训练模型，循环1000次
net.save_weights(netfile) #保存模型

predict_result = net.predict_classes(test_data[:,:2]).reshape(len(test)) #预测结果变形
'''这里要提醒的是，keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n x 1维数组，而不是通常的 1 x n'''

from prediction.cm_plot import * #导入自行编写的混淆矩阵可视化函数
cm_plot(test[:,3], predict_result).show() #显示混淆矩阵可视化结果

from sklearn.metrics import roc_curve #导入ROC曲线函数
import matplotlib.pyplot as plt
predict_result = net.predict(test_data[:,:2]).reshape(len(test))
fpr, tpr, thresholds = roc_curve(test, predict_result, pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label = 'ROC of LM') #作出ROC曲线
plt.xlabel('False Positive Rate') #坐标轴标签
plt.ylabel('True Positive Rate') #坐标轴标签
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc=4) #图例
plt.show() #显示作图结果