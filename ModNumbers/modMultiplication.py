# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:31:26 2018

@author: nilsh
"""

def onlyEven(i):
    if (i&1): #odd
        raise ValueError("Odd numbers illegal in onlyEven")
    return i

def nrLen(nr):
    return len(str(nr))

def modTable(modNr, nr, _range = 20):
    formatStr = "{:>" + str(nrLen(modNr * _range + nr)) + "}"; #Set format length to length of largest nr
    for i in range(_range):
        print(formatStr.format(i*modNr + nr))
        
#modTable(9,4)

#for i in range(20):
#    print("{:>3}".format(3*i))
    
print(onlyEven(3))