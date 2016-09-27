#-*- coding: utf-8 -*-
from numpy import  *

if __name__ == '__main__':
    new = [1,2,3,4]
    new.append(5)
    new.append(6)
    print array(new).reshape(3,2)