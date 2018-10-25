# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:33:16 2018

@author: Sruthi Pasumarthy
"""

import csv #to work on incorrect calculations
           
csvFileLoc = 'C:\\Users\\Sruthi Pasumarthy\\Desktop\\lr\\random.csv'
csvFile = open(csvFileLoc,'r')
reader = csv.reader(csvFile, delimiter = ',')
numOfRows = len(list(reader))
print("Num of Rows: ",numOfRows)
csvFile.seek(0)
listOfLists = []
firstRow = next(reader,None)
listOfLists.append(firstRow)
#print(len(listOfLists))
#print(listOfLists)
csvFile.seek(0)
numOfCols = len(next(reader))
print ("Num of Columns: ",numOfCols)

for row in reader:
        listOfLists.append(row)

print(len(listOfLists))
weights = []
j = 0
while j < numOfCols:
    initialWeight = 0
    weights.append(initialWeight)
    j = j+1
print('Weights: ',weights)

i = 0
xVectors = []
yValues = []
counter = 0
for item in listOfLists:
    x = []
    while i < numOfCols:
        print(item[i])
        if(i == numOfCols-1):
            yValues.append(item[i])
        else:
            x.append(item[i])
            print(x)
        i = i+1
    xVectors.append(x)
    counter = counter + 1
    i=0 #reinitialising the value of i
#print(xVectors)
#print(yValues)

def calculateLinearFunction(w):
    linearFunction = 0.0
    k = 0
    x0 = 1
    linearFuncList = []
    while k < len(yValues):
        #print('LF y : ',yValues[k])
       # print('LF x : ',xVectors[k])
        temp = xVectors[k]
        e=0
        while e < len(temp):
            if(e==0):
                linearFunction = float(w[e])*float(x0)
            else:
                linearFunction = float(linearFunction) + (float(w[e])*float(temp[e]))
            e = e+1
      #  print('Iteration number: %d',k,' Linear function: %f',linearFunction)
        linearFuncList.append(linearFunction)
        k = k+1
    print('LinearFuncListLen: ',linearFuncList)
    return linearFuncList;


def calculateGradientAndSSE(lf,w):
    p = 0
    q = 0
    gradient = 0.0
    SSE = 0.0
    while p < len(yValues):
        print(yValues[p])
        error = float(yValues[p]) - float(lf[p])
        print('Error: ',error)
        squaredError = float(error) * float(error)
        print('Squared Error: ',squaredError)
        temp = xVectors[p]
        print('X Vector: ',temp)
        elementTimesError = 0.0
        while q < len(temp):
            print("X: ",temp[q])
            elementTimesError = float(elementTimesError) + (float(temp[q]) * float(error))
            print("element x error: ",elementTimesError)
            q = q+1
        gradient = float(gradient) + float(elementTimesError)
        SSE = float(SSE) + float(squaredError)
        p = p+1

    print('SSE: ',SSE)
    print('Gradient: ',gradient)
    return; 

linearFunctions = []
linearFunctions = calculateLinearFunction(weights)

calculateGradientAndSSE(linearFunctions, weights)

#print('xVectors: %d',len(xVectors))
#print('yValues: %d',len(yValues))
#calculate SSE & gradient should accept the parameters: xVectors, yValues 
    #in this, we also should calculate f(x), which would need weights
    #for zeroth iteration, all weights are zero => f(x)=0 but we have to calculte SSE
#(additional: equate size of xVectors & yValues, remove data from listOfLists)
#calculate weights accepts parameters: learning rate, weights vector, gradient  

 

#print(len(listOfLists))

#while i<numOfRows:
 #   while j<numOfCols:
        


'''numOfCols = len(next(reader))
print ("Num of Columns: ",numOfCols)
i = 0
listOfLists = []
list1 = []
print("At 17: ")
print(len(listOfLists))
while i < numOfCols:
    for column in reader:
        listOfLists.append(column[i])
        list1.insert(i,column[i])
    print(len(listOfLists))
    print(len(list1))
    i = i+1
print("At 26: ")
print(len(listOfLists))
print(list1)
csvHeaders = []
while i < numOfCols:
    headerNum = 'x'+str(i+1)
    csvHeaders.append(headerNum)
    i = i+1 
    
print(csvHeaders)


data = pd.read_csv(csvFileLoc, header = None, names = csvHeaders)
    
print(csvHeaders.x1.tolist())
import csv
from collections import defaultdict
d = defaultdict(list)

csvFileLoc = 'C:\\Users\\Sruthi Pasumarthy\\Desktop\\lr\\random.csv'
csvFile = open(csvFileLoc,'r')
reader = csv.reader(csvFile, delimiter = ',')
numOfCols = len(next(reader))
i = 0
csvHeaders = []
while i < numOfCols:
    csvHeaders.append(i)
    i = i+1 
    
print(csvHeaders)

for csvHeader in csvHeaders:
    for column in reader:
        d[csvHeader].append(column)

print(d)'''
#print(d)
'''import pandas as pd
import csv

csvFileLoc = 'C:\\Users\\Sruthi Pasumarthy\\Desktop\\lr\\random.csv'
csvFile = open(csvFileLoc,'r')
reader = csv.reader(csvFile, delimiter = ',')
numOfCols = len(next(reader))
print ("Num of Columns: ",numOfCols)
i = 0
listOfLists = []
list1 = []
print("At 17: ")
print(len(listOfLists))
while i < numOfCols:
    for column in reader:
        listOfLists.append(column[i])
        list1.insert(i,column[i])
    print(len(listOfLists))
    print(len(list1))
    i = i+1
print("At 26: ")
print(len(listOfLists))
print(list1)'''
'''csvHeaders = []
while i < numOfCols:
    headerNum = 'x'+str(i+1)
    csvHeaders.append(headerNum)
    i = i+1 
    
print(csvHeaders)


data = pd.read_csv(csvFileLoc, header = None, names = csvHeaders)
    
print(csvHeaders.x1.tolist())'''
    
