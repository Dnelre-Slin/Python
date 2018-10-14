# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 23:10:34 2018

@author: nilsh
"""

import matplotlib.pyplot as plt
import numpy as np

def F1(x, a=5, d=20):
    return ((np.e**(a*(1-(x/d))) - 1) / (np.e**(a) - 1))

#def F2(x, e=2.7, a=5, d=20):
#    return ((e**(a*(1-(x/d))) - 1) / (e**(a) - 1))

#e = 1.4
a = np.e
d = 20

x = np.linspace(0,d,101)

y = F1(x, a, d)
#y = F2(x, e, a, d)

plt.plot(x, y)

plt.axis([0,d,0,1])

plt.show()