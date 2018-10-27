# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:33:16 2018

@author: Sruthi Pasumarthy(220651) & Rahul Kodarapu(220850)
"""

import csv #to work on incorrect calculations
#import os

threshold=float(input('Enter the Threshold :'))
learningRate=float(input('Enter the Learning Rate : '))
#fileLocation= input('Please enter file location : ')
#csvFileLoc = os.path.isdir(fileLocation)


#threshold = 0.0001
#learningRate= 0.0001
           
csvFileLoc = 'C:\\Users\\rahut\\Desktop\\p1linreg\\yacht.csv'
csvFile = open(csvFileLoc,'r')
reader = csv.reader(csvFile, delimiter = ',')
numOfRows = len(list(reader))
#print("Num of Rows: ",numOfRows)
csvFile.seek(0) #Goes back to the beginning of the file
listOfLists = []
firstRow = next(reader,None) #This is because the reader is omitting the first row, so we are forece feeding it. It
# None tells it that the first row is not a header
listOfLists.append(firstRow)
#print(len(listOfLists))
#rint(listOfLists)
csvFile.seek(0)
numOfCols = len(next(reader))
#print ("Num of Columns: ",numOfCols)

for row in reader:
        listOfLists.append(row)

#print(len(listOfLists))
weights = []
j = 0
while j < numOfCols:
    initialWeight = 0
    weights.append(initialWeight)
    j = j+1
#print('Weights: ',weights)

#weights=[-0.0940224666666667, -0.5375774493333338, -0.2591702260000002]

weightsList = []
weightsList.append(weights)
#print(weightsList)

i = 0
xVectors = []
yValues = []
counter = 0
for item in listOfLists:
    x = []
    while i < numOfCols:
        #print(item[i])
        if(i == numOfCols-1):
            yValues.append(item[i])
        else:
            x.append(item[i])
            #print(x)
        i = i+1
    xVectors.append(x)
    counter = counter + 1
    i=0 #reinitialising the value of i
#print(xVectors)
#print(yValues)
#print(counter)

def calculateLinearFunction(w):
    linearFunction = 0.0
    k = 0
    x0 = 1
    linearFuncList = []
    while k < len(yValues):
        #print('LF y : ',yValues[k])
       # print('LF x : ',xVectors[k])
        temp = xVectors[k]
        #print(temp)
        e=0
        while e < len(temp)+1:
            if(e==0):
                linearFunction = float(w[e])*float(x0) #Wo*x0, for random
                #print(linearFunction)
            else:
                #print(float(w[e])*float(temp[e-1]))
                #print(w[e])
               # print(temp[e-1])
                linearFunction = float(linearFunction) + (float(w[e]))*float(temp[e-1]) #w1*x1 + w2*x2,for random
               # print(linearFunction)
            e = e+1
      #  print('Iteration number: %d',k,' Linear function: %f',linearFunction)
        #print('value of linear function',linearFunction)
        linearFuncList.append(linearFunction)
        k = k+1
    #print('LinearFuncListLen: ',linearFuncList)
    return linearFuncList;


def calculateGradientsAndSSE(lf,w):
    p = 0
    q = 0
    i = 0
    e = 0
    gradientsList=[]
    while i< len(w):
        grad=0
        gradientsList.append(grad)
        i=i+1
    #gradient = 0.0
    SSE = 0.0
    elementTimesErrorList = []
    temp = xVectors[0]
    while e < len(temp):
        x = 0
        elementTimesErrorList.append(x)
        e = e+1
   # print('elementTimesErrorList:',elementTimesErrorList)
    while p < len(yValues):
    #    print(yValues[p])
        error = float(yValues[p]) - float(lf[p])
     #   print('Error: ',error)
        squaredError = float(error) * float(error)
      #  print('Squared Error: ',squaredError)
        temp = xVectors[p]
       # print('X Vector: ',temp)
        #elementTimesError = 0.0
        gradientsList[0]= float(gradientsList[0])+ float(error)
        while q < len(temp):
        #    print("X: ",temp[q])
            elementTimesErrorList[q] = float(elementTimesErrorList[q]) + (float(temp[q]) * float(error)) #xi(yi-f(xi))
         #   print("element x error: ",elementTimesErrorList[q])
            gradientsList[q+1] = float(gradientsList[q+1]) + (float(temp[q]) * float(error)) #float(elementTimesErrorList[q])
            #if(q==len(temp)-1):
             #   print('updated gradient(w2) Value', gradientsList[q+1])
            #if(q==len(temp)-2):
             #   print('updated gradient(w1) Value', gradientsList[q+1])
            q = q+1
        #gradient = float(gradient) + float(elementTimesError)
        SSE = float(SSE) + float(squaredError)
        p = p+1
        q=0

    #print('SSE: ',SSE)
    #print('Gradient: ',gradient)
    #print('GradientList:',gradientsList)
    return SSE,gradientsList; 

linearFunctions = []
linearFunctions = calculateLinearFunction(weights)
#print(linearFunctions)


SSEout=0
gradientsListOut=[]
SSEout,gradientsListOut=calculateGradientsAndSSE(linearFunctions, weights)
#print(SSEout)
#print(gradientsListOut)

iterationWiseResult=[]

resultDisplay= []
iteration= 0
resultDisplay.append(iteration)
resultDisplay.append(weights)
resultDisplay.append(SSEout)
#print(resultDisplay)
iterationWiseResult.append(resultDisplay)
#print(iterationWiseResult)

def calculateNewWeights(w,g):
    newWeights=[]
    i=0
    while i< len(w):
        nw= w[i]+ learningRate*g[i]
        newWeights.append(nw)
        i=i+1
        nw=0
    w=newWeights
 #   print('newWeights:',newWeights)
    weightsList.append(newWeights)
    return w;

newWeightsOut=[]
newWeightsOut= calculateNewWeights(weights,gradientsListOut)
#print(weightsList)

def updateIterationWeightsSSE(sse,newweightsout):
    iteration=1
    SSEnew = sse
    newWeights= newweightsout
    gradientsListNew=[]
    #print(1)
    #k=0
    #while k<2:
    while SSEnew > threshold :
        #print(2)
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
       # k=k+1
    i=0
    while i< len(iterationWiseResult):
  #      print(3)
        print(iterationWiseResult[i])
        i= i+1
    return;
    
updateIterationWeightsSSE(SSEout,newWeightsOut)

#print(iterationWiseResult)
#######################################################

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
        

'''
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
    
