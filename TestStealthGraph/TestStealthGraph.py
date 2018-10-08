# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 23:10:34 2018

@author: nilsh
"""

import matplotlib.pyplot as plt
import numpy as np

def F1(x, a=5, d=20):
    return ((np.e**(a*(1-(x/d))) - 1) / (np.e**(a) - 1))


a = 6
d = 40

x = np.linspace(0,d,101)

y = F1(x, a, d)

plt.plot(x, y)

plt.axis([0,d,0,1])

plt.show()