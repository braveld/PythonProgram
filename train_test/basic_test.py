#-*- coding: utf-8 -*-
from numpy import  *

def prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def monisen(no):
    begin = 2
    while no > 0:
        if prime(begin) and prime(2 ** begin -1):
            no -= 1
        begin += 1
    begin = begin - 1
    return 2 ** begin - 1

if __name__ == '__main__':
    print monisen(4)


