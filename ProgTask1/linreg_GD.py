# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:33:16 2018
@author: Srilakshmi Sruthi Pasumarthy(220651) & Rahul Gupta Kodarapu(220850)
Implementation of Gradient Descent -- Linear Regression
"""

import csv
import sys

csvFile = open(sys.argv[1],'r')
learningRate = float(sys.argv[2])
threshold = float(sys.argv[3])         

reader = csv.reader(csvFile, delimiter = ',')
numOfRows = len(list(reader))
csvFile.seek(0) #Goes back to the beginning of the file
listOfLists = []
firstRow = next(reader,None) #This is because the reader is omitting the first row, so we are forece feeding it. It
# None tells it that the first row is not a header
listOfLists.append(firstRow)
csvFile.seek(0)
numOfCols = len(next(reader))

for row in reader:
        listOfLists.append(row) 
        #To read all the rows of the csv, each row is stored as a list. All the rows are agaun stored in one-consolidated list 
weights = []
j = 0

while j < numOfCols:
    initialWeight = 0
    weights.append(initialWeight)
    j = j+1
    #Initializing all the weights to zero for the zeroth iteration and storing those values in the weights list

weightsList = []
weightsList.append(weights)

i = 0
xVectors = []
yValues = []
counter = 0
for item in listOfLists:
    x = []
    while i < numOfCols:
        if(i == numOfCols-1):
            yValues.append(item[i])
        else:
            x.append(item[i])
            
        i = i+1
    xVectors.append(x)
    counter = counter + 1
    i=0 #reinitialising the value of i
#Maintaing two seperate lists for X-values and Y-values of each csv row

def calculateLinearFunction(w):
    #This implements the calculation of linear function(summation of the products of weight(w)&x) 
    linearFunction = 0.0
    k = 0
    x0 = 1
    linearFuncList = []
    while k < len(yValues):
        temp = xVectors[k]
        e=0
        while e < len(temp)+1:
            if(e==0):
                linearFunction = float(w[e])*float(x0) 
            else:
                linearFunction = float(linearFunction) + (float(w[e]))*float(temp[e-1]) #w1*x1 + w2*x2,for random
            e = e+1
        linearFuncList.append(linearFunction)
        k = k+1
    return linearFuncList;


def calculateGradientsAndSSE(lf,w):
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
    SSE = 0.0
    elementTimesErrorList = []
    temp = xVectors[0]
    while e < len(temp):
        x = 0
        elementTimesErrorList.append(x)
        e = e+1
    while p < len(yValues):
        error = float(yValues[p]) - float(lf[p])
        squaredError = float(error) * float(error)
        temp = xVectors[p]
        gradientsList[0]= float(gradientsList[0])+ float(error)
        while q < len(temp):
            elementTimesErrorList[q] = float(elementTimesErrorList[q]) + (float(temp[q]) * float(error)) #xi(yi-f(xi))
            gradientsList[q+1] = float(gradientsList[q+1]) + (float(temp[q]) * float(error)) 
            q = q+1
        SSE = float(SSE) + float(squaredError)
        p = p+1
        q=0
    return SSE,gradientsList; 

linearFunctions = []
linearFunctions = calculateLinearFunction(weights)


SSEout=0
gradientsListOut=[]
SSEout,gradientsListOut=calculateGradientsAndSSE(linearFunctions, weights)

iterationWiseResult=[]

resultDisplay= []
iteration= 0
resultDisplay.append(iteration)
resultDisplay.append(weights)
resultDisplay.append(SSEout)
iterationWiseResult.append(resultDisplay)

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

def updateIterationWeightsSSE(sse,newweightsout):
    #This implements the updation of the final results list(Iteration number, weights & SSE)
    iteration=1
    SSEnew = sse
    newWeights= newweightsout
    gradientsListNew=[]
    while SSEnew > threshold :
        linearFunctionsNew = []
        linearFunctionsNew = calculateLinearFunction(newWeights)
        SSEnew,gradientsListNew=calculateGradientsAndSSE(linearFunctionsNew, newWeights)
        resultDisplayNew= []
        resultDisplayNew.append(iteration)
        resultDisplayNew.append(newWeights)
        resultDisplayNew.append(SSEnew)
        iterationWiseResult.append(resultDisplayNew)
        newWeights= calculateNewWeights(newWeights,gradientsListNew)
        iteration= iteration+1
    i=0
    print('[Iteration Nr, [Weights i.e., wo, w1, w2 etc..], SSE]')
    while i< len(iterationWiseResult)-1:
        print(iterationWiseResult[i])
        i= i+1
    return;
    
updateIterationWeightsSSE(SSEout,newWeightsOut) #Final results list
