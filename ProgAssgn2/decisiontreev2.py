# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:49:49 2018

@author: Sruthi Pasumarthy
"""

import pandas as pd
import math

dataFrame = pd.read_csv("D://car.csv", header = None)
listOfValues = []

for i, item in dataFrame.iteritems():
    temp = item.unique()
    listOfValues.append(temp.tolist())

rowCount = len(dataFrame.index)
print("Num of rows: ",rowCount)

columnCount = len(dataFrame.columns)
print("Num of columns: ",columnCount)

classColumnNum = columnCount - 1

attrList = listOfValues.copy()
attrList.pop()
targetAttr = listOfValues[classColumnNum]
entropyList = []

def calculateEntropy(df, attrList): 
        classesCount = {}
        for label in listOfValues[classColumnNum]:
            if(label in df.values):
                temp = df[classColumnNum].value_counts()[label]
                classesCount[label] = temp
            else:
                classesCount[label] = 0
                
        entropy = 0.0
        for k,v in classesCount.items():
            if(v > 0):
                probabilityValue = v / sum(classesCount.values())
                entropy = entropy - (probabilityValue * (math.log(probabilityValue)/math.log(len(classesCount))))
            else:
                continue
         
        return entropy;  
    
treeEntropy = calculateEntropy(dataFrame, attrList)
numOfRows = rowCount

def calculateGain(df, attrList, attr):
    classesCount = {}
    tempEntropy = 0.0
    gain = 0.0
    for label in listOfValues[classColumnNum]:
        if(label in df.values):
                temp = df[classColumnNum].value_counts()[label]
                classesCount[label] = temp
        else:
                classesCount[label] = 0
    
    for k,v in classesCount.items():
        if(v > 0):
            probabilityValue = v / sum(classesCount.values())
            tempDF = pd.DataFrame(df.loc[dataFrame[classColumnNum] == k])
            tempEntropy += probabilityValue * calculateEntropy(tempDF, attrList)
        
    gain = calculateEntropy(df, attrList) - tempEntropy
    
    return tempEntropy, gain;        

def selectSplitAttr(df, attrList):
    selected = -1
    maxGain = 0.0
    attr = 0
    gainValues = {}
    entropies = {}
    entropy = 0.0
    selectedEntropy = 0.0
    while(attr < len(attrList)):
        entropy, gain = calculateGain(df, attrList, attr)
        gainValues[str(attr)] = gain
        entropies[str(attr)] = entropy
        #print("Attr: ",attr)
        attr = attr + 1
    maxGain = max(zip(gainValues.values(),gainValues.keys()))
    if maxGain != 0:
        selected = int(maxGain[1])
        maxGain = maxGain[0]
        selectedEntropy = entropies[str(selected)]
    print("Selected: ",selected,"  Entropy: ",selectedEntropy)
    print("MaxGain: ",maxGain)
    return selected;
   
def decisionTree(df, attrList, targetAttr, counter):
    counter += 1
    print("Counter", counter)
    df = df
    if df.empty or len(attrList) <= 0:
        return "unacc"
    elif targetAttr.count(targetAttr[0]) == len(targetAttr):  
        return targetAttr[0]
    else:
        best = selectSplitAttr(df, attrList)
        #print("Best: ",best)
        tree = {best:{}}
        selectedAttr = attrList[best]

        for attrVal in selectedAttr:
            #print("line 97 -  ",attrVal)
            tempDF = pd.DataFrame(df.loc[df[best] == attrVal])
            #print(len(tempDF[classColumnNum].unique()))
            #print(len(tempDF))
            if len(tempDF[classColumnNum].unique()) == 1: #pureset
                tempStr = ''.join(tempDF[classColumnNum].unique())
                print("Pureset at attr ",best," for value- ",attrVal," Class- ",tempStr)
                continue
            else: 
                #print(best)
                newAttr = attrList.copy()
                parsed = attrList[best]
                #print(parsed)
                newAttr.remove(parsed)
                subtree = decisionTree(tempDF, newAttr, targetAttr, counter)
                
                tree[best][attrVal] = subtree
        
        return tree;
        
tree = decisionTree(dataFrame, attrList, targetAttr, 0)
print(tree)       


        