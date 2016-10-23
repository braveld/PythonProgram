#-*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt


def zhuzhuangtu(x,y):
    # plt.figure(figsize=(9, 6))

    plt.bar(x, y, width=0.35, facecolor='lightskyblue', edgecolor='white')
    # width:柱的宽度
    # plt.bar(X + 0.35, Y2, width=0.35, facecolor='yellowgreen', edgecolor='white') 如果需要绘制两条柱状图
    # 水平柱状图plt.barh，属性中宽度width变成了高度height
    # 打两组数据时用+
    # facecolor柱状图里填充的颜色
    # edgecolor是边框的颜色
    # 想把一组数据打到下边，在数据前使用负号
    # plt.bar(X, -Y2, width=width, facecolor='#ff9999', edgecolor='white')
    # 给图加text
    for x, y in zip(x, y):
        plt.text(x + 0.3, y + 0.05, '%.2f' % y, ha='center', va='bottom')

    # plt.ylim(0, +1.25)
    plt.show()

if __name__ == '__main__':
    x = [1,2,3]
    y = [4,5,6]
    zhuzhuangtu(x,y)



