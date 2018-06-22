#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:14:40 2018

@author: pengsu
"""

import numpy as np    
label = array(datingLabels)
idx_1 = np.where(label == 1)
idx_2 = np.where(label == 2)
idx_3 = np.where(label == 3)
p1 = plt.scatter(datingDataMat[idx_1,1], datingDataMat[idx_1,2],marker = 'x',color = 'm',label = 'not at all')
p2 = plt.scatter(datingDataMat[idx_2,1], datingDataMat[idx_2,2],marker = '+',color = 'c',label = 'in small doses')
p3 = plt.scatter(datingDataMat[idx_3,1], datingDataMat[idx_3,2],marker = 'o',color = 'r',label = 'in large doses')
plt.legend(loc = 'upper right')
plt.show()