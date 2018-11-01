# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:27:54 2018

@author: Nils
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def ODEsolver(t, h, y0, y0prim, A, B, C, S):
    y = t.copy()
    y[0] = y0
    y[1] = y0prim*h + y0
    
    for i in range(2, len(y)):
        y[i] = (S(t[i])*h**2 + y[i-1]*(2*A(t[i]) - C(t[i])*h**2) + y[i-2]*(0.5*B(t[i])*h
         - A(t[i])))/(A(t[i]) + 0.5*B(t[i])*h)
    return y

def setupPlots(t, ys):
    r = len(ys)
    plt.figure(figsize=(9, 2*r))
    plt.subplots_adjust(hspace=1)
    for i in range(len(ys)):
        fig = plt.subplot(r, 1, i+1)
        fig.set_title("Fig" + str(i+1))
        plt.plot(t, ys[i])
        plt.axis((0,100,-3,3))
        

t, h = np.linspace(0, 100, 10000, retstep=True)

ys = []

ys.append(ODEsolver(t, h, 0, 1, lambda t : 1, lambda t : -5, lambda t : 4, lambda t : t**2))
ys.append(ODEsolver(t, h, 0, 1, lambda t : 1, lambda t : 0, lambda t : 3, lambda t : 0))
ys.append(ODEsolver(t, h, 0, 1, lambda t : 1, lambda t : 0, lambda t : 10, lambda t : 0))
ys.append(ODEsolver(t, h, 0, 1, lambda t : 1, lambda t : 0, lambda t : 4, lambda t : 2*math.cos(2*math.pi*t)))
ys.append(ODEsolver(t, h, 0, 1, lambda t : 1, lambda t : 1/t, lambda t : t, lambda t : 2*math.cos(2*math.pi*t)))

setupPlots(t, ys)

plt.show()