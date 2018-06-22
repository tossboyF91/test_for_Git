#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:57:52 2018

@author: pengsu
"""

import kNN
import matplotlib.pyplot as plt
#import the matplotlib in to the python

datingDataMat , datingLabels = kNN.file2matrix('datingTestSet2.txt')
fig = plt.figure()
ax = fig.add_subplot(111)

#subplot means divide the screen to some pieces, for example (111) means split whole figure to 
#one line one row and only only one picture

ax.scatter(datingDataMat[:,1], datingDataMat[:,2],c='r',marker='1')
plt.show()