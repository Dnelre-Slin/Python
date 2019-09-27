# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:36:33 2018

@author: nilsh
"""

import random
import math

def getNrFromSize(size):
    return 2**size

def isPrime(prime):
    if prime % 2 == 0 or prime % 3 == 0:
        return False
    f1 = lambda x : 6*x - 1
    f2 = lambda x : 6*x + 1
    rootNr = int(math.floor(math.sqrt(prime)))
    for i in range(1,rootNr):
        if prime % f1(i) == 0 or prime % f2(i) == 0:
            return False
    return True

def getLargePrime(_size, _range):
    nrSize = getNrFromSize(_size)
    prime = random.randint(nrSize - _range, nrSize + _range)
    while not isPrime(prime):
        prime += 2
    return prime
        
def main():
    print(isPrime(2**64 + 5))

if __name__ == "__main__":
    main()