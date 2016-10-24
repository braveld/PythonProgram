#-*- coding: utf-8 -*-
#构建并测试CART决策树模型

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


#构建CART决策树模型
from sklearn.tree import DecisionTreeClassifier #导入决策树模型

tree = DecisionTreeClassifier() #建立决策树模型
tree.fit(train_data[:,:2], train) #训练

#保存模型
# from sklearn.externals import joblib
# joblib.dump(tree, treefile)

from prediction.cm_plot import * #导入自行编写的混淆矩阵可视化函数
cm_plot(test, tree.predict(test_data[:,:2])).show() #显示混淆矩阵可视化结果
#注意到Scikit-Learn使用predict方法直接给出预测结果。

from sklearn.metrics import roc_curve #导入ROC曲线函数
import matplotlib.pyplot as plt
fpr, tpr, thresholds = roc_curve(test, tree.predict_proba(test_data[:,:2])[:,1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label = 'ROC of CART', color = 'green') #作出ROC曲线
plt.xlabel('False Positive Rate') #坐标轴标签
plt.ylabel('True Positive Rate') #坐标轴标签
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc=4) #图例
plt.show() #显示作图结果