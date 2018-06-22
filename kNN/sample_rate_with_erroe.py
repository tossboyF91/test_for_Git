#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 00:34:07 2018

@author: pengsu
"""

import kNN
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
x=[]
a=0
y=[]
rate=[]
for i in range (0,9):
    a=a+0.1
    x.append(a)
    

for i in range(0,9):
    rate.append(x[i])
    y.append(kNN.datingClassTest(x[i],3)) 
    
def f_2(x,A,B,C):
    return A*x**2+B*x+C
ax.scatter(rate, y)
A2 , B2 , C2 =optimize.curve_fit(f_2, rate ,y)[0]
x2=np.arange(0,1,0.1)
y2=A2*x2**2+B2*x2+C2
ax.plot(x2,y2,'r',linewidth=2,)   