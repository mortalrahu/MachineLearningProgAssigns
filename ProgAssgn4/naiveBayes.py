# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:47:57 2018

@authors: Srilakshmi Sruthi Pasumarthy(220651)
          Rahul Gupta Kodarapu(220850)
          Abdullah Al Zubaer(218074)
"""
import pandas as pd
import math
import csv
import sys

inputFileName = sys.argv[1]
outputFileName =sys.argv[2]

dataFrame = pd.read_csv(inputFileName,sep = '\t',header = None)
rowCount = len(dataFrame.index)
columnCount = len(dataFrame.columns)
dataFrame.dropna()
if(pd.isnull(dataFrame.iloc[0][columnCount-1]) == True):
    dataFrame = dataFrame.drop(columnCount-1,axis=1)
columnCount = len(dataFrame.columns)

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
   
"""
function: calcMyuSigmaAndProbability
Input Params: Number of Class Instances, Index 
Output Params: list of Myus, Sigmas and Class Probabilities
This function computes the Myu, Sigma and Perobability for each class for appropriate attributes.
"""

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

"""
function: resultCalculator
Input Params: No Parameters
Output Params: List of Mys, Sigmas. Probabilities for each class and Number of Missclassificiations
This function invokes 'calcMyuSigmaAndProbability' function and uses the output of that function to further calculate Number of Missclassifications .
"""

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
    while j < numOfClasses:
        h=0
        tempDecHelp=[]
        refBox = tempResult[j]
        while h < rowCount:     
            b= 1
            tempCondProbXC=[]
            while b < columnCount:
                if((b%2) ==1):
                    temp = (1/(math.sqrt(2.*math.pi*refBox[b])))*math.exp(-((dataFrame[b][h]-refBox[b-1])*(dataFrame[b][h]-refBox[b-1]))/(2*refBox[b]))
                else:
                    temp = (1/(math.sqrt(2.*math.pi*refBox[b+1])))*math.exp(-((dataFrame[b][h]-refBox[b])*(dataFrame[b][h]-refBox[b]))/(2*refBox[b+1]))
                tempCondProbXC.append(temp)
                b=b+1
            proCondProbXC = tempCondProbXC[0]*tempCondProbXC[1] 
            tempDecHelp.append(proCondProbXC)
            h=h+1
        decHelp.append(tempDecHelp)
        j= j+1
    r=0
    listOfCondProbCX = [] 
    while r < rowCount:
        tempCPCXs =[]
        den = decHelp[0][r]*0.5+ decHelp[1][r]*0.5
        o= 0
        while o < numOfClasses:
            temp= decHelp[o][r]*0.5/den
            tempCPCXs.append(temp)
            o=o+1
        listOfCondProbCX.append(tempCPCXs)
        r=r+1
    y=0
    while y< rowCount:     
        if(listOfCondProbCX[y][0] > listOfCondProbCX[y][1]):
            classDecision.append('A')
        else:
            classDecision.append('B')
        y=y+1
    u=0
    while u < rowCount:
        if(classList[u]!= classDecision[u]):
            missClass = missClass +1
        u=u+1
    listOfMissClass = []
    listOfMissClass.append(missClass)
    listOfResult.append(listOfMissClass)
    return listOfResult

listToBePrinted = resultCalculator()

with open(outputFileName, 'w', encoding='utf8', newline='') as outputTSV:
    tsvWriter = csv.writer(outputTSV, delimiter='\t', lineterminator='\n')
    if listToBePrinted:
        tsvWriter.writerows(listToBePrinted)
    else:
        print("no values to display")

print('The output is generated in the following file: ',outputFileName)