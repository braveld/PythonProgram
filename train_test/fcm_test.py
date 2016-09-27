#-*- coding: utf-8 -*-
from numpy import  *



def euclDistance(data, center):
    return sqrt(sum(power(data - center, 2)))

if __name__ == '__main__':
    dataset = matrix([[1,2],[3,4],[9,10],[11,12]])
    center = matrix([[3,4],[5,6],[7,8]])
    numSamples, dim = center.shape
    new = []

    for i in range(dim):
        new.append((center.T[i] * dataset / float(sum(center.T[i]))).tolist()[0])
    print matrix(new)

