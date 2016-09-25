import sklearn.datasets as datasets
import scipy.cluster.hierarchy as hcluster
import numpy.random as random
import numpy as np
import numpy.core.fromnumeric
import time

import matplotlib.pyplot as plt


def irisSample():
    iris = datasets.load_iris()
    irisdata = iris.data
    result = hcluster.fclusterdata(irisdata, criterion='maxclust', t=3)
    print("result is %s" % result)


def gaussianSample():
    timeCheckin = time.clock()
    X = random.randn(100, 100)
    X[:50, :100] += 10
    result = hcluster.fclusterdata(X, criterion='maxclust', t=2)
    print("hierachical clustering on sample with shape(%d,%d) cost %s seconds " % (
    np.shape(X)[0], np.shape(X)[1], time.clock() - timeCheckin))
    print("result is %s" % result)
    clusterA = [label for label in result if (label == 1)]
    clusterB = [label for label in result if (label == 2)]
    print("There are %d samples in cluster 1" % (len(clusterA)))
    print("ClusterA is %s" % clusterA)
    print("There are %d samples in cluster 2" % (len(clusterB)))
    print("ClusterB is %s" % clusterB)


def testPerformanceByNum(start, end, increment):
    """
    """
    mapPerformance = dict()
    for sampleNum in range(start, end, increment):
        X = random.randn(sampleNum, 100)
        X[:50, :100] += 10
        timeCheckin = time.clock()
        result = hcluster.fclusterdata(X, criterion='maxclust', t=2)
        timeCost = time.clock() - timeCheckin
        mapPerformance[sampleNum] = timeCost
    return mapPerformance


def testPerformanceByDim(start, end, increment):
    """
    """
    mapPerformance = dict()
    for dim in range(start, end, increment):
        X = random.randn(100, dim)
        X[:50, :dim] += 10
        timeCheckin = time.clock()
        result = hcluster.fclusterdata(X, criterion='maxclust', t=2)
        timeCost = time.clock() - timeCheckin
        mapPerformance[dim] = timeCost
    return mapPerformance


def showPerformance(mapPerformance):
    """
    """
    xAxisData = numpy.core.fromnumeric.sort(mapPerformance.keys())
    yAxisData = [mapPerformance[key] for key in xAxisData]
    plt.plot(xAxisData, yAxisData, '*-')
    plt.show()


# irisSample()
# gaussianSample()
if __name__ == '__main__':

    mapPerformance = testPerformanceByNum(100, 3100, 100)
    showPerformance(mapPerformance)
    mapPerformance = testPerformanceByDim(100, 10100, 100)
    showPerformance(mapPerformance)