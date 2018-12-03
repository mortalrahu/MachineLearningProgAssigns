# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:36:17 2018

@authors: Srilakshmi Sruthi Pasumarthy(220651)
          Rahul Gupta Kodarapu(220850)
          Abdullah Al Zubaer(218074)
"""
import pandas as pd
#import math
#import sys
#import os


inputFileName = "C://Users//rahut//Documents//GitHub//MachineLearningProgAssigns//ProgAssgn3//perceptron//Example.tsv"#sys.argv[1]
#if os.path.exists(inputFileName):
dataFrame = pd.read_csv(inputFileName,sep = '\t',header = None)
learningRate = 0.0001
#else:
 #   print("Please enter a valid filepath")

#outputFileName = sys.argv[2]
rowCount = len(dataFrame.index)
columnCount = len(dataFrame.columns)
print(columnCount)
print(dataFrame.iloc[0][columnCount-1])
dataFrame.dropna()
if(pd.isnull(dataFrame.iloc[0][columnCount-1]) ==True):
    dataFrame = dataFrame.drop(columnCount-1,axis=1)
print(dataFrame)
columnCount = len(dataFrame.columns)
weights = []
j = 0

while j < columnCount:
    initialWeight = 0
    weights.append(initialWeight)
    j = j+1
    #Initializing all the weights to zero for the zeroth iteration and storing those values in the weights list

weightsList = []
weightsList.append(weights)

print(weights)
print(weightsList)

xVectorsDF = dataFrame.drop(0,axis=1)
print(xVectorsDF)
print(xVectorsDF.iloc[[0]])
xVectors=[]

for row in xVectorsDF.iterrows():
    index, data = row
    xVectors.append(data.tolist())
    
print(xVectors)
classList = dataFrame[0].tolist()
print(classList)
print(len(classList))
classListInNum = []
i=0
while i< len(classList):
    if(classList[i]== 'A'):
        classListInNum.append(1)
    else:
        classListInNum.append(0)
    i=i+1
    
print(classListInNum)

def decideNoOfDiff(dFrame,classList,w):
    diffCount = 0
    d=0
    perceptronFunction = 0.0
    k = 0
    x0 = 1
    perceptronFuncList = []
    p = 0
    perceptronFuncListInNum = []
    while k < len(classList):
        temp = xVectors[k]
        e=0
        while e < len(temp)+1:
            if(e==0):
                perceptronFunction = float(w[e])*float(x0) 
            else:
                perceptronFunction = float(perceptronFunction) + (float(w[e]))*float(temp[e-1]) #w1*x1 + w2*x2,for random
            e = e+1
        if(perceptronFunction>0):
            perceptronFuncList.append('A')
        else:
            perceptronFuncList.append('B')
        k = k+1
    while d < len(perceptronFuncList):
        if(perceptronFuncList[d]!= classList[d]):
            diffCount = diffCount +1
        d=d+1
    while p < len(perceptronFuncList):
        if(perceptronFuncList[p]== 'A'):
            perceptronFuncListInNum.append(1)
        else:
            perceptronFuncListInNum.append(0)
        p=p+1
    
    return diffCount, perceptronFuncList,perceptronFuncListInNum;

dc,pflout,pflinout= decideNoOfDiff(dataFrame,classList,weights)
print(dc)
print(pflout)
print(pflinout)

nonAnnealingError = []
annealingError = []

nonAnnealingError.append(dc)
annealingError.append(dc)

def calculateGradients(pflin,w):
    #This implements the calculation of gradient values and the sum of squared error(SSE)
    p = 0
    q = 0
    i = 0
    e = 0
    gradientsList=[]
    while i< len(w):
        grad=0
        gradientsList.append(grad)
        i=i+1
    #SSE = 0.0
    elementTimesErrorList = []
    temp = xVectors[0]
    while e < len(temp):
        x = 0
        elementTimesErrorList.append(x)
        e = e+1
    while p < len(classList):
        error = float(classListInNum[p]) - float(pflin[p])
        #squaredError = float(error) * float(error)
        temp = xVectors[p]
        gradientsList[0]= float(gradientsList[0])+ float(error)
        while q < len(temp):
            elementTimesErrorList[q] = float(elementTimesErrorList[q]) + (float(temp[q]) * float(error)) #xi(yi-f(xi))
            gradientsList[q+1] = float(gradientsList[q+1]) + (float(temp[q]) * float(error)) 
            q = q+1
        #SSE = float(SSE) + float(squaredError)
        p = p+1
        q=0
    return gradientsList; 


#SSEout=0
gradientsListOut=[]
gradientsListOut=calculateGradients(pflinout, weights)

def calculateNewWeights(w,g):
    #This implements the calculation of new values for weights
    newWeights=[]
    i=0
    while i< len(w):
        nw= w[i]+ learningRate*g[i]
        newWeights.append(nw)
        i=i+1
        nw=0
    w = newWeights
    weightsList.append(newWeights)
    return w;

newWeightsOut=[]
newWeightsOut= calculateNewWeights(weights,gradientsListOut)

def calculateNewWeightsAnnealing(w,g,af):
    #This implements the calculation of new values for weights
    newWeights=[]
    i=0
    while i< len(w):
        nw= w[i]+ (learningRate/af)*g[i]
        newWeights.append(nw)
        i=i+1
        nw=0
    w = newWeights
    weightsList.append(newWeights)
    return w;
newWeightsOutAnnealing=[]
newWeightsOutAnnealing= calculateNewWeightsAnnealing(weights,gradientsListOut,1)

#
#print('#1',newWeightsOut)
#      
#
#dc2,pflout2,pflinout2= decideNoOfDiff(dataFrame,classList,newWeightsOut)
#print(dc2)
#print(pflout2)
#print(pflinout2)
#
#gradientsListOut2=[]
#gradientsListOut2=calculateGradients(pflinout2, newWeightsOut)
#
#newWeightsOut2=[]
#newWeightsOut2= calculateNewWeights(newWeightsOut,gradientsListOut2)
#
#print('#2',newWeightsOut2)
#      
#dc3,pflout3,pflinout3= decideNoOfDiff(dataFrame,classList,newWeightsOut2)
#print(dc3)
#print(pflout3)
#print(pflinout3)
#
#gradientsListOut3=[]
#gradientsListOut3=calculateGradients(pflinout3, newWeightsOut2)
#
#newWeightsOut3=[]
#newWeightsOut3= calculateNewWeights(newWeightsOut2,gradientsListOut3)
#
#print('#3',newWeightsOut3)

def recursiveFunction(newWeightsOut):
    na = 0
    newWeightsNew = newWeightsOut
    while na < 100:
        dcNew,pflNew,pflinNew = decideNoOfDiff(dataFrame,classList,newWeightsNew)
        nonAnnealingError.append(dcNew)
        gradientsListNew =[]
        gradientsListNew = calculateGradients(pflinNew,newWeightsNew)
        newWeightsNew = calculateNewWeights(newWeightsNew,gradientsListNew)
        na= na+1
    print(nonAnnealingError)
    return;
    
def recursiveFunctionAnnealing(newWeightsOut):
    na = 0
    newWeightsNew = newWeightsOut
    while na < 100:
        dcNew,pflNew,pflinNew = decideNoOfDiff(dataFrame,classList,newWeightsNew)
        annealingError.append(dcNew)
        gradientsListNew =[]
        gradientsListNew = calculateGradients(pflinNew,newWeightsNew)
#        if(na==0):
#            newWeightsNew = calculateNewWeightsAnnealing(newWeightsNew,gradientsListNew,1)
#        else:
        newWeightsNew = calculateNewWeightsAnnealing(newWeightsNew,gradientsListNew,na+1)
        na= na+1
    print(annealingError)
    return;
    
recursiveFunction(newWeightsOut)
recursiveFunctionAnnealing(newWeightsOutAnnealing)
