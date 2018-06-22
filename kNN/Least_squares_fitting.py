#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:22:50 2018

@author: pengsu
"""
import numpy as np
def linear_regression(x, y):
    N = len(x)
    sumx = sum(x)
    sumy = sum(y)
    sumx2 = sum(x**2)
    sumxy = sum(x*y)

    A = np.mat([[N, sumx], [sumx, sumx2]])
    b = np.array([sumy, sumxy])

    return np.linalg.solve(A, b)

def gen_coefficient_matrix(X, Y):
    N = len(X)
    m = 3
    A = []
    # 计算每一个方程的系数
    for i in range(m):
        a = []
        # 计算当前方程中的每一个系数
        for j in range(m):
            a.append(sum(X ** (i+j)))
        A.append(a)
    return A

# 计算方程组的右端向量b
def gen_right_vector(X, Y):
    N = len(X)
    m = 3
    b = []
    for i in range(m):
        b.append(sum(X**i * Y))
    return b

