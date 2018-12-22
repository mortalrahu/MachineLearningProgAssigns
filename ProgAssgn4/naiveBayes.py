# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:47:57 2018

@authors: Srilakshmi Sruthi Pasumarthy(220651)
          Rahul Gupta Kodarapu(220850)
          Abdullah Al Zubaer(218074)
"""
import pandas as pd
import math
#import csv
#import sys

#Rahul's path = C://Users//rahut//Documents//GitHub//MachineLearningProgAssigns//ProgAssgn4//nb//Example.tsv
#Sruti's Path = 

inputFileName ="C://Users//rahut//Documents//GitHub//MachineLearningProgAssigns//ProgAssgn4//nb//Example.tsv" #sys.argv[1]
#outputFileName = sys.argv[2]

dataFrame = pd.read_csv(inputFileName,sep = '\t',header = None)
#learningRate = 1
#MAX_NUM_OF_ITERATIONS = 100

rowCount = len(dataFrame.index)
columnCount = len(dataFrame.columns)
dataFrame.dropna()
if(pd.isnull(dataFrame.iloc[0][columnCount-1]) == True):
    dataFrame = dataFrame.drop(columnCount-1,axis=1)
columnCount = len(dataFrame.columns)
#print(dataFrame)
#print(columnCount)
#print(dataFrame[0][0])

uniqueValues = []

for i, item in dataFrame.iteritems():
    temp = item.unique()
    uniqueValues.append(temp.tolist())
    
listOfClasses = uniqueValues[0]

numOfClasses= len(uniqueValues[0])

amtOfClassInstances = []

classList = dataFrame[0].tolist()


i=0
while i < numOfClasses:
   j=0
   tempClass = listOfClasses[i]
   temp = 0
   while j < rowCount:
       if(dataFrame[0][j]==tempClass):
           temp = temp+1
       j=j+1
   amtOfClassInstances.append(temp)    
   i=i+1

def calcMyuSigmaAndProbability(aCI,indexOfaCI):
    k=0
    p=0
    sumOfACI=0
    listOfMyus = []
    listOfSigmas = []
    resultFormat = []
    while k < len(aCI):
        sumOfACI =sumOfACI + aCI[k]
        k=k+1
    probability = aCI[indexOfaCI]/sumOfACI
    m=1
    while m < columnCount:
        n=0
        l=0
        sumOfCurrentAttr=0
        SquaredOfCurrentDiff= 0
        while n < rowCount:
            if(dataFrame[0][n]==listOfClasses[indexOfaCI]):
                sumOfCurrentAttr = sumOfCurrentAttr + dataFrame[m][n]  
            n = n+1
        tempMyu=(1/aCI[indexOfaCI])*sumOfCurrentAttr
        listOfMyus.append(tempMyu)
        while l < rowCount:
            if(dataFrame[0][l]==listOfClasses[indexOfaCI]):
                SquaredOfCurrentDiff = SquaredOfCurrentDiff + ((dataFrame[m][l]-tempMyu)* (dataFrame[m][l]-tempMyu))
            l = l+1
        tempSigma=(1/(aCI[indexOfaCI]-1))*SquaredOfCurrentDiff
        listOfSigmas.append(tempSigma)
        m=m+1
    while p < len(listOfMyus):
        resultFormat.append(listOfMyus[p])
        resultFormat.append(listOfSigmas[p])
        p=p+1
    resultFormat.append(probability)
    return resultFormat

#a = calcMyuSigmaAndProbability(amtOfClassInstances,0)
#print(a)


def resultCalculator():
    listOfResult=[]
    classDecision=[]
    missClass=0
    decHelp=[]
    g=0
    while g < 2:
        temp = calcMyuSigmaAndProbability(amtOfClassInstances,g)
        listOfResult.append(temp)
        g=g+1
    tempResult = listOfResult
    j=0
    print('#1')
    while j < numOfClasses:
        print('#2')
        h=0
        tempDecHelp=[]
        refBox = tempResult[j]
        while h < rowCount:     
            b= 1
            tempCondProb=[]
            o=0
            den =0
            while b < columnCount:
                if((b%2) ==1):
                    temp = (1/(math.sqrt(2.*math.pi)*refBox[b]))*math.exp(-(dataFrame[b][h]-refBox[b-1])/(2*refBox[b]*refBox[b]))
                else:
                    temp = (1/(math.sqrt(2.*math.pi)*refBox[b+1]))*math.exp(-(dataFrame[b][h]-refBox[b])/(2*refBox[b+1]*refBox[b+1]))
                tempCondProb.append(temp)
                b=b+1
            while o < len(tempCondProb):
                den = den + (tempCondProb[o]*refBox[len(refBox)-1])
                o=o+1
            condProbCX = ((tempCondProb[0]*refBox[len(refBox)-1])/den) #*((tempCondProb[1]*refBox[len(refBox)-1])/den) 
            tempDecHelp.append(condProbCX)
            h=h+1
        decHelp.append(tempDecHelp)
        j= j+1
    r=0
    print(len(decHelp[0]),len(decHelp[1]))
    print(decHelp)
    while r < rowCount:
        if(decHelp[0][r] > decHelp[1][r]):
            classDecision.append('A')
        else:
            classDecision.append('B')
        r=r+1
    print(classDecision)
    u=0
    while u < rowCount:
        if(classList[u]!= classDecision[u]):
            missClass = missClass +1
        u=u+1
    listOfResult.append(missClass)
    return listOfResult

r = resultCalculator()
print(r)