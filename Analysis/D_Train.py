import spams
import numpy as np
import Image
import time
img_file = 'D:/spams-python-v2.5-svn2014-07-04/spams-python/boat.png'
try:
    img = Image.open(img_file)
except:
    print "Cannot load image %s : skipping test" %img_file
I = np.array(img) / 255.
if I.ndim == 3:
    A = np.asfortranarray(I.reshape((I.shape[0],I.shape[1] * I.shape[2])))
    rgb = True
else:
    A = np.asfortranarray(I)
    rgb = False

m = 8;n = 8;
X = spams.im2col_sliding(A,m,n,rgb)

X = X - np.tile(np.mean(X,0),(X.shape[0],1))
X = np.asfortranarray(X / np.tile(np.sqrt((X * X).sum(axis=0)),(X.shape[0],1)),dtype = 'float64')
param = { 'K' : 100, # learns a dictionary with 100 elements
          'lambda1' : 0.15, 'numThreads' : 4, 'batchsize' : 400,
          'iter' : 1000}

########## FIRST EXPERIMENT ###########
tic = time.time()
D = spams.trainDL(X,**param)
tac = time.time()
t = tac - tic
print 'time of computation for Dictionary Learning: %f' %t

##param['approx'] = 0
# save dictionnary as dict.png
#_objective(X,D,param,'dict')

#### SECOND EXPERIMENT ####
print "*********** SECOND EXPERIMENT ***********"

X1 = X[:,0:X.shape[1]/2]
X2 = X[:,X.shape[1]/2 -1:]
param['iter'] = 500
tic = time.time()
(D,model) = spams.trainDL(X1,return_model = True,**param)
tac = time.time()
t = tac - tic
print 'time of computation for Dictionary Learning: %f\n' %t

#_objective(X,D,param,'dict1')

# Then reuse the learned model to retrain a few iterations more.
param2 = param.copy()
param2['D'] = D
tic = time.time()
(D,model) = spams.trainDL(X2,return_model = True,model = model,**param2)
tac = time.time()
t = tac - tic
print 'time of computation for Dictionary Learning: %f' %t
#_objective(X,D,param,'dict2')

#################### THIRD & FOURTH EXPERIMENT ######################
# let us add sparsity to the dictionary itself

print '*********** THIRD EXPERIMENT ***********'
param['modeParam'] = 0
param['iter'] = 1000
param['gamma1'] = 0.3
param['modeD'] = 1

tic = time.time()
D = spams.trainDL(X,**param)
tac = time.time()
t = tac - tic
print 'time of computation for Dictionary Learning: %f' %t
#_objective(X,D,param)

print '*********** FOURTH EXPERIMENT ***********'
param['modeParam'] = 0
param['iter'] = 1000
param['gamma1'] = 0.3
param['modeD'] = 3

tic = time.time()
D = spams.trainDL(X,**param)
tac = time.time()
t = tac - tic
print 'time of computation for Dictionary Learning: %f' %t
#_objective(X,D,param)