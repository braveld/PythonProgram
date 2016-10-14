#-*- coding: utf-8 -*-
if __name__ == '__main__':
    #join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
    # data = [['A1', 'A2'], ['A1', 'A3']]
    # ms = '--'
    # index = [ms.join(i) for i in data]  #i是一个属性都是字符串的列表，i必须是列表或者字符串、元组
    # print index
    #
    # str = "-";
    # seq = ("a", "b", "c");  # 字符串序列
    # test = 'asd'
    # print str.join(seq);
    # print str.join(test)

    #找出列表的差集
    # a = [2, 5]
    # b = [2, 5, 8]
    # print list(set(b).difference(set(a)))  # b中有而a中没有的

    #列表的增加,不可行
    a = [2, 5]
    b = []
    b = b.append(a)
    print b
