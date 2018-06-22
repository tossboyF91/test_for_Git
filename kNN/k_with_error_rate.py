#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 00:27:20 2018

@author: pengsu
"""
import kNN
import matplotlib.pyplot as plt
#import Least_squares_fitting as lsf
import numpy as np
from scipy import optimize
k=0
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlabel('k')
plt.ylabel('error')
x = np.arange(0, 100, 1.0)
x_list=[]
y=[]
for i in range (0,100,1):    
    k=k+1
#    print k
    s=kNN.datingClassTest(k)
    x_list.append(k)
    y.append(s)
#print x
#print y
ax.scatter(x,y)

# linear fitting
"""a0,a1 = lsf.linear_regression(x,y)
_X = [0, 100]
_Y = [a0 + a1 * m for m in _X]

plt.plot(x, y, 'ro', _X, _Y, 'b', linewidth=2)
plt.title("y = {} + {}x".format(a0, a1))
plt.show()
"""
# curve fitting
"""
A = lsf.gen_coefficient_matrix(x, y)
b = lsf.gen_right_vector(x, y)
a0, a1, a2 = np.linalg.solve(A, b)
_X = [0, 100]
_Y = np.array([a0 + a1*m + a2*m**2 for m in _X])
plt.plot(x, y, 'ro', _X, _Y, 'b', linewidth=2)
plt.show()
"""
def f_2(x,A,B,C):
    return A*x**2+B*x+C

A2 , B2 , C2 =optimize.curve_fit(f_2, x_list ,y)[0]
x2=np.arange(0,100,1.0)
y2=A2*x2**2+B2*x2+C2
plt.plot(x2,y2,'r',linewidth=2,)
def f_3(x,A,B,C,D):
    return A*x**3+B*x**2+C*x+D
A3 ,B3 ,C3, D3 = optimize.curve_fit(f_3,x_list,y)[0]
x3=np.arange(0,100,1.0)
y3=A3*x3**3+B3*x2**2+C3*x2+D3
plt.plot(x3,y3,'b',linewidth=2)