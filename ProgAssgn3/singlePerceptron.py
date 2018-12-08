# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:36:17 2018

@authors: Srilakshmi Sruthi Pasumarthy(220651)
          Rahul Gupta Kodarapu(220850)
          Abdullah Al Zubaer(218074)
"""
import pandas as pd
import csv
import sys

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

dataFrame = pd.read_csv(inputFileName,sep = '\t',header = None)
learningRate = 1
MAX_NUM_OF_ITERATIONS = 100

rowCount = len(dataFrame.index)
columnCount = len(dataFrame.columns)
dataFrame.dropna()
if(pd.isnull(dataFrame.iloc[0][columnCount-1]) == True):
    dataFrame = dataFrame.drop(columnCount-1,axis=1)
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

xVectorsDF = dataFrame.drop(0,axis=1)
xVectors=[]

for row in xVectorsDF.iterrows():
    index, data = row
    xVectors.append(data.tolist())
    
classList = dataFrame[0].tolist()

classListInNum = []
i=0
while i< len(classList):
    if(classList[i] == 'A'):
        classListInNum.append(1)
    else:
        classListInNum.append(0)
    i=i+1
    
"""
function: applyPerceptron
Inputs Params: dataframe, list of classes, list of weights
Output Params: errorValue, list of Activation function output values
This function implements the functionality of a single perceptron with an activation function.
"""
def applyPerceptron(dFrame,classList,w):
    errorValue = 0
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
            if(e == 0):
                perceptronFunction = float(w[e])*float(x0) 
            else:
                perceptronFunction = float(perceptronFunction) + (float(w[e]))*float(temp[e-1]) #w1*x1 + w2*x2,for random
            e = e+1
        if(perceptronFunction > 0):
            perceptronFuncList.append('A')
        else:
            perceptronFuncList.append('B')
        k = k+1
    while d < len(perceptronFuncList):
        if(perceptronFuncList[d] != classList[d]):
            errorValue = errorValue +1
        d=d+1
    while p < len(perceptronFuncList):
        if(perceptronFuncList[p] == 'A'):
            perceptronFuncListInNum.append(1)
        else:
            perceptronFuncListInNum.append(0)
        p=p+1
    
    return errorValue,perceptronFuncListInNum;

error, activationFuncOutputs= applyPerceptron(dataFrame,classList,weights)

errorValuesConstantLR = []
errorValuesAnnealingLR = []

errorValuesConstantLR.append(error)
errorValuesAnnealingLR.append(error)

"""
function: calculateGradients
Input Params: list of perception activation function output values, list of weights
Output Params: list of gradient values
This function implements the calculation of gradient values.
"""
def calculateGradients(afOutputs,w):
    p = 0
    q = 0
    i = 0
    e = 0
    gradientValues=[]
    while i< len(w):
        grad=0
        gradientValues.append(grad)
        i=i+1

    elementTimesErrorList = []
    temp = xVectors[0]
    while e < len(temp):
        x = 0
        elementTimesErrorList.append(x)
        e = e+1
    while p < len(classList):
        error = float(classListInNum[p]) - float(afOutputs[p])
        temp = xVectors[p]
        gradientValues[0]= float(gradientValues[0])+ float(error)
        while q < len(temp):
            elementTimesErrorList[q] = float(elementTimesErrorList[q]) + (float(temp[q]) * float(error)) #xi(yi-f(xi))
            gradientValues[q+1] = float(gradientValues[q+1]) + (float(temp[q]) * float(error)) 
            q = q+1
        p = p+1
        q=0
    return gradientValues; 

listOfGradientValues=[]
listOfGradientValues = calculateGradients(activationFuncOutputs, weights)


"""
function: updateWeightsConstantLR
Input Params: list of weights, list of gradient values
Output Params: list of weights(updated)
This function implements the calculation of new weights with constant learning rate
"""
def updateWeightsConstantLR(w,g):
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

updatedWeights=[]
updatedWeights= updateWeightsConstantLR(weights,listOfGradientValues)

"""
function: updateWeightsAnnealingLR
Input Params: list of weights, list of gradient values, activation function
Output Params: list of weights(updated)
This function implements the calculation of new weights with annealing learning rate
"""
def updateWeightsAnnealingLR(w,g,af):
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

updatedWeightsAnnealing=[]
updatedWeightsAnnealing= updateWeightsAnnealingLR(weights,listOfGradientValues,1)

"""
function: getErrorValuesWithConstantLearningRate
Input Params: list of weights
Output Params: list of error values
This function invokes the function for calculation of errors with constant learning rate, iteratively.
"""
def getErrorValuesWithConstantLearningRate(updatedWeights):
    counter = 0
    weightsListTemp = updatedWeights
    while counter < MAX_NUM_OF_ITERATIONS:
        errorNew,afOutputs = applyPerceptron(dataFrame,classList,weightsListTemp)
        errorValuesConstantLR.append(errorNew)
        gradientsListTemp = []
        gradientsListTemp = calculateGradients(afOutputs,weightsListTemp)
        weightsListTemp = updateWeightsConstantLR(weightsListTemp,gradientsListTemp)
        counter = counter + 1
        
    return errorValuesConstantLR;
 
"""
function: getErrorValuesWithAnnealingLearningRate
Input Params: list of weights
Output Params: list of error values
This function invokes the function for calculation of errors with annealing learning rate, iteratively.
"""
def getErrorValuesWithAnnealingLearningRate(updatedWeights):
    counter = 0
    weightsListTemp = updatedWeights
    while counter < MAX_NUM_OF_ITERATIONS:
        errorNew,afOutputs = applyPerceptron(dataFrame,classList,weightsListTemp)
        errorValuesAnnealingLR.append(errorNew)
        gradientsListTemp = []
        gradientsListTemp = calculateGradients(afOutputs,weightsListTemp)
        weightsListTemp = updateWeightsAnnealingLR(weightsListTemp,gradientsListTemp,counter+2)
        counter = counter + 1
        
    return errorValuesAnnealingLR;
    
nonAnnealingList = getErrorValuesWithConstantLearningRate(updatedWeights)
annealingList = getErrorValuesWithAnnealingLearningRate(updatedWeightsAnnealing)

with open(outputFileName, 'w', encoding='utf8', newline='') as outputTSV:
    tsvWriter = csv.writer(outputTSV, delimiter='\t', lineterminator='\n')
    if nonAnnealingList:
        tsvWriter.writerow(nonAnnealingList)
    else:
        print("With constant learning rate, no error values to display")
    
    if annealingList:
        tsvWriter.writerow(annealingList)
    else:
        print("With annealing learning rate, no error values to display")

print('The output is generated in the following file: ',outputFileName)
        