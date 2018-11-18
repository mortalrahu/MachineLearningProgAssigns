# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 18:18:17 2018

@author: Sruthi Pasumarthy
"""
'''
n columns-- n-1 attributes, nth - class
csv reader---> all rows to list
last column ---> class
uniqueValuesList
listOfAttributesAndClass
entropy calculation(listOfAttributesAndClass)
-->from classes--- find unique values-- number of classes/////
-->count the number of instances with each class of the classList
-->calculate entropy as -E(countofclassi/totalnumofinstances)
-->return entropy.
//to update listOfAttributesAndClass
///-----

remainingAttrs--num of attributes on which inf gain has to be calculated
calculate infGain from i =1 to remainingAttrs 
{
 entropy(updatedList)
 IG = entropy(root) - E(count)

}

print(dataFrame[0])
print(dataFrame.loc[[0]])
print(dataFrame.iloc[0][4])

'''
import pandas as pd
import math

dataFrame = pd.read_csv("D://car.csv", header = None)
listOfValues = []

for i, item in dataFrame.iteritems():
    temp = item.unique()
    listOfValues.append(temp.tolist())
print(listOfValues)

rowCount = len(dataFrame.index)
print("Num of rows: ",rowCount)

columnCount = len(dataFrame.columns)
print("Num of columns: ",columnCount)

classColumnNum = columnCount - 1

def calculateEntropy(df, numOfRows): 
        classesCount = []
        for label in listOfValues[classColumnNum]:
            #print(label," ",label in df.values)
            if(label in df.values):
                temp = df[classColumnNum].value_counts()[label]
                #print(temp)
                classesCount.append(temp)
            else:
                classesCount.append(0)
        #print(classesCount)
        
        entropy = 0.0
        for i in classesCount:
            if(i > 0):
                probabilityValue = i / numOfRows
                entropy = entropy - (probabilityValue * (math.log(probabilityValue)/math.log(len(classesCount))))
            else:
                continue
         
        return entropy;  

treeEntropy = calculateEntropy(dataFrame,rowCount)
print("Tree Entropy: ",treeEntropy)

gainValues = {}
gainList = []
entropyList = []
attr = 0
numOfRows = rowCount
while(attr < (len(listOfValues) - 1)):
    tempEntropyList = []
    tempEntropies = {}
    substractionTerm = 0.0
    for attrValue in listOfValues[attr]:
        #print("AttrValue: ",attrValue)
        tempLen = dataFrame[attr].value_counts()[attrValue]
        tempDF =pd.DataFrame(dataFrame.loc[dataFrame[attr] == attrValue][classColumnNum])
        tempEntropy = calculateEntropy(tempDF,tempLen)
        #tempEntropyList.append(tempEntropy)
        tempEntropies[attrValue] = tempEntropy
        prob = tempLen / numOfRows
        substractionTerm = substractionTerm + (prob * tempEntropy)
    #print(tempEntropyList)
    #print(tempEntropies)
    entropyList.append(tempEntropies)
    gain = treeEntropy - substractionTerm
    gainList.append(gain)
    gainValues[attr] = gain
    attr = attr + 1
print("***************************************")
print(entropyList)
print("***************************************")
print(gainValues)
     






