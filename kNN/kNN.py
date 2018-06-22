#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 00:14:55 2018

@author: pengsu
"""

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
 #   print "the number of dataSize is %d" %dataSetSize
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()     
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(float(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector
    
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals
   
def datingClassTest(k):
    hoRatio = 0.6      #hold out 10%
    datingDataMat,datingLabels = file2matrix('test2oral.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],k)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
        
    if (errorCount==0):
        print "the we could not count error"
    else:
        print "the rate of error is %f" %(errorCount/float(numTestVecs))
        
    print errorCount     
    return errorCount

def classifyPerson():
    resultList = [1,2,3]
#    resultList = ['not at all' , 'in small doses' , 'in large doses']
    percentTats = float(raw_input("percentage of time playing video games?"))
    ffMile = float(raw_input("frequent fliter miles earned per year?"))
    icecream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat , datingLabels = file2matrix('datingTestSet2.txt')
    norMat, ranges , minVals = autoNorm(datingDataMat)
    inArr = array([ffMile , percentTats , icecream])
    classifierResult = classify0((inArr-minVals)/ranges , norMat , datingLabels, 3 )
    print classifierResult
    print "You will probably like this person:",  resultList[classifierResult - 1] # why -1?



