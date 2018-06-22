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
    returnMat = zeros((numberOfLines,4))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:4]
        classLabelVector.append(int(listFromLine[-1]))
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
    hoRatio = 0.7     #hold out 10%
    datingDataMat,datingLabels = file2matrix('test_exist.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    AssumedNumber=[]
    RealValue = []
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],k)
        AssumedNumber.append(classifierResult)
        RealValue.append( datingLabels[i] )
        print "the number of the item is %d"  % (i) 
        if (datingLabels[i] == 0):
            print "acuatlly, D dose not exist"
        else:
            print "acuatlly, D exists!"
        if (classifierResult == 0) :
            print "by calculateing , we reckon the D point does not exist "
        else:
                print "by calculateing , the D point exists!"
        if (classifierResult  != datingLabels[i]): 
            print "The estimated situation does not match the actual situation "
            errorCount += 1.0
        else:
            print "The estimated situation matches with the actual situation "
    
        
    if (errorCount==0):
        print "the we could not count error"
    else:
        print "the rate of error is %f" %(errorCount/float(numTestVecs))
        
    print "the sum of the estimated data is %d , the error number is %d"% ((numTestVecs), errorCount)     
    return AssumedNumber ,  RealValue


def classifyPerson():
#    resultList = [0,1]
#    resultList = ['not at all' , 'in small doses' , 'in large doses']
    eagleA = float(raw_input("eagle A?"))
    eagleC = float(raw_input("eagle C?"))
    distance_AB = float(raw_input("distance_AB?"))
    distance_BC = float(raw_input("distance_BC?"))
    datingDataMat , datingLabels = file2matrix('test_exist.txt')
#    resultList = datingLabels 
    norMat, ranges , minVals = autoNorm(datingDataMat)
    inArr = array([eagleA , eagleC , distance_AB , distance_BC])
    classifierResult = classify0((inArr-minVals)/ranges , norMat , datingLabels, 3 )
    if (classifierResult== 0 ):
        print ("the D point does not exist!")
    else:
        print ("the D point exists!")
#    print "You will probably like this person:",  resultList[classifierResult - 1] # why -1?



