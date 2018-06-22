#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 01:50:11 2018

@author: pengsu
"""

import kNN_test
import matplotlib.pyplot as plt
import numpy as np
EstimiatedValue = []
RealValue = []
EstimiatedValue, RealValue = kNN_test.datingClassTest(3)
fig = plt.figure()
print np.size(EstimiatedValue)
print np.size(RealValue)

