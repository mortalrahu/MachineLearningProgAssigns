# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 22:53:18 2018

@author: Sruthi Pasumarthy
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:33:16 2018
@author: Sruthi Pasumarthy(220) & Rahul Kodarapu(220850)
"""

import csv 
import os
import sys

fileName = sys.argv[1]
if os.path.exists(fileName):
    csvFileLoc = os.path.basename(fileName)
learningRate = float(sys.argv[2])
threshold = float(sys.argv[3])

    


'''threshold=float(input('Enter the Threshold :'))
learningRate=float(input('Enter the Learning Rate : '))
fileLocation= input('Please enter file location : ')
csvFileLoc = os.path.isdir(fileLocation)'''


#threshold = 0.0001
#learningRate= 0.0001
           
#csvFileLoc = 'C:\\Users\\rahut\\Desktop\\p1linreg\\random.csv'
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
                linearFunction = float(w[e])*float(x0) 
            else:
                linearFunction = float(linearFunction) + (float(w[e]))*float(temp[e-1]) #w1*x1 + w2*x2,for random
            e = e+1
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
    i=0
    while i< len(iterationWiseResult):
        print(iterationWiseResult[i])
        i= i+1
    return;
    
updateIterationWeightsSSE(SSEout,newWeightsOut)

        
