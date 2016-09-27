# -*- coding: utf-8 -*-
from numpy import *


def euclDistance(data, center):
    return sqrt(sum(power(data - center, 2)))


if __name__ == '__main__':
    

    dataset = matrix([[1, 2]])
    center = matrix([[3, 4]])

    print euclDistance(dataset[0],center[0])