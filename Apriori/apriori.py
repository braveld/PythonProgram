#create a simple dataset
def loadDataset():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

#create a dataset which item size is 1
def createC1(dataSet):
    C1=[]
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset,C1)    #create a dictionary

#scan the support rate of each item
def scanD(D,Ck,minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList,supportData

def aproiriGen(Lk,k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList

def apriori(dataSet,minSupport = 0.5):
    C1 = createC1(dataSet)
    D = map(set,dataSet)
    L1,supportData = scanD(D,C1,minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aproiriGen(L[k-2],k)
        Lk,supK = scanD(D,Ck,minSupport)
        supportData.update(supK)   #hebing
        L.append(Lk)
        k += 1
    return L,supportData

def calcConf(freqSet,H,supportData,brl,minConf = 0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq]
        if conf > minConf:
            print freqSet-conseq,'----->',conseq,'conf:',conf
            brl.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH


def ruleFromConseq(freqset,H,supportData,brl,minConf = 0.7):
    m = len(H[0])
    if (len(freqset) > m + 1):
        Hmp1 = aproiriGen(H,m + 1)
        Hmp1 = calcConf(freqset,Hmp1,supportData,brl,minConf)
        if (len(Hmp1) > 1):
            ruleFromConseq(freqset, Hmp1, supportData, brl, minConf)


def generateRules(L,supportData,minConf = 0.7):
    bigRuleList = []
    for i in range(1,len(L)):
        for freqset in L[i]:
            H1 = [frozenset([item]) for item in freqset]
            if i > 1:
                ruleFromConseq(freqset,H1,supportData,bigRuleList,minConf)
            else:
                calcConf(freqset,H1,supportData,bigRuleList,minConf)
    return bigRuleList


if __name__ == '__main__':
   dataSet = loadDataset()
   L,Sup = apriori(dataSet)
   print Sup
   rules = generateRules(L,Sup)
   print rules



