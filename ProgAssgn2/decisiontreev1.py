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

csvFile = open("D://car.csv",'r')
reader = csv.reader(csvFile, delimiter = ',')

listOfAttributesAndClass = list(reader)
numOfRows = len(listOfAttributesAndClass)
print("Num of rows: ",numOfRows)
csvFile.seek(0) 
numOfCols = len(next(reader))
print("Num of cols: ",numOfCols) 

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

classesCount = []
for label in listOfValues[columnCount - 1]:
    temp = dataFrame[columnCount - 1].value_counts()[label]
    classesCount.append(temp.tolist())
 #dataFrame[columnCount - 1].value_counts()
#print(classesCount)
print(classesCount)

treeEntropy = 0.0
for i in classesCount:
    probabilityValue = i / rowCount
    treeEntropy = treeEntropy - (probabilityValue * (math.log(probabilityValue)/math.log(len(classesCount))))

print("Entropy: ",treeEntropy)






