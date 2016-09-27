#-*- coding: utf-8 -*-
from numpy import  *

def euclDistance(data, center):
    return sqrt(sum(power(data - center, 2)))

if __name__ == '__main__':
    new = []

    dataset = matrix([[1, 2], [3, 4], [9, 10], [11, 12]])
    center = matrix([[3, 4], [5, 6], [7, 8]])
    # center.dtype = float



    for i in range(4):
        for j in range(3):

            new.append(euclDistance(dataset[i],center[j]))

    print array(new).reshape(4,3)
