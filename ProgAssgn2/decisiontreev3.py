# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 18:18:17 2018

@authors: Srilakshmi Sruthi Pasumarthy(220651)
          Rahul Gupta Kodarapu(220850)
          Abdullah Al Zubaer(218074)
"""

import pandas as pd
import math
import xml.etree.ElementTree as ET
import sys
import os

inputFileName = sys.argv[1]
if os.path.exists(inputFileName):
    dataFrame = pd.read_csv(inputFileName, header = None)
else:
    print("Please enter a valid filepath")


outputFileName = sys.argv[2]


uniqueValues = []

for i, item in dataFrame.iteritems():
    temp = item.unique()
    uniqueValues.append(temp.tolist())

rowCount = len(dataFrame.index)

columnCount = len(dataFrame.columns)

noOfClasses = len(uniqueValues[len(uniqueValues)-1])
classColumnNum = columnCount - 1

classLabels= uniqueValues[classColumnNum]

slice = 'att'

attrList = uniqueValues.copy()
attrList.pop()

a=0
attrNameList= []
while a< len(attrList):
        temp = "att"+ str(a)
        attrNameList.append(temp)
        a=a+1

"""
function: calculateEntropy
Inputs Params: dataFrame, length of the dataFrame
Output Params: entropy, number of classes in the dataFrame
This function implements the calculation of entropy on a given dataset(here, dataframe)
"""
def calculateEntropy(df, numOfRows): 
        classesCount = []
        for label in uniqueValues[classColumnNum]:
            if(label in df[classColumnNum].values):
                temp = df[classColumnNum].value_counts()[label]
                classesCount.append(temp)
            else:
                classesCount.append(0)
        
        entropy = 0.0
        for i in classesCount:
            if(i > 0):
                probabilityValue = i / numOfRows
                entropy = entropy - (probabilityValue * (math.log(probabilityValue)/math.log(len(classesCount))))
            else:
                continue
        return entropy,classesCount  

#treeEntropy - the total entropy of the dataset
treeEntropy,classesCountOutput = calculateEntropy(dataFrame,rowCount)

#xmlRoot - root node for the output xml
xmlRoot = ET.Element('tree', entropy = str(treeEntropy))

"""
function: subDataFrame
Inputs Params: dataFrame, attribute value, attribute(index of the attribute)
Output Params: part of the dataFrame
This function implements the split on a given dataframe, based on a value of an attribute 
"""
def subDataFrame(df,attrValue,attrNum):    
    sdf = df[df[attrNum]==attrValue]
    return sdf


"""
function: calculateGain
Inputs Params: parent node entropy, list of entropy values, length of the dataframe, length of the sub dataframe
Output Params: gain value
This function implements the calculation of Gain on a particular attribute 
"""
def calculateGain(parentNodeEntropy,entropyList,dfLength,sdfLength):
    i=0
    gain = parentNodeEntropy
    while i< len(entropyList):
        gain = gain - (sdfLength/dfLength)*(entropyList[i])
        i= i+1
    return gain


"""
function: infoFetcher
Inputs Params: dataframe, list of attributes, node entropy, list of entropy values, list of attributes with assigned names
Output Params: list of attributes, list of gain values, list of attributes with respective gain values, index of attribute with maximum gain value, list of attribute names
This function implements the calculation of Gain on a given attribute 
"""
def infoFetcher(df, attributesList,currentNodeEntropy,attrNameListUpdated):
    entropyList= []
    listOfEntropyLists = []
    gainList= []
    attrNameWithGainValues ={}
    
    i=0
    while i< len(attributesList):
        r=0
        splitColumn = int(attrNameListUpdated[i].replace(slice,''))
        for label in attributesList[i]:
            sdf= subDataFrame(df,label,splitColumn)
            noOfRows= len(sdf.index)
            tempEntropy,tempClassesCount = calculateEntropy(sdf,noOfRows)
           
            if r < len(attributesList[i]):
                entropyList.append(tempEntropy)
            if r==len(attributesList[i])-1:
                listOfEntropyLists.append(entropyList)
                entropyList= []
            r=r+1
        tempGain= calculateGain(currentNodeEntropy,listOfEntropyLists[i],len(df.index),len(sdf.index))
        gainList.append(tempGain)
        i=i+1
    #hashmap for attnames and gains
    j=0
    while j< len(gainList):
        attrNameWithGainValues[attrNameListUpdated[j]]= gainList [j]
        j=j+1
    maxGain = max(gainList)
    maxGainIndex= gainList.index(maxGain)
    return attributesList, gainList,attrNameWithGainValues,maxGainIndex,attrNameListUpdated

"""
function: decisionTree
Inputs Params: dataframe, list of attributes, entropy of the parent node, list of attribute names, parent node for XML 
This function recursively implements the decision tree based on Quinlan's ID3 algorithm.
"""
def decisionTree(df,attributesList,parentNodeEntropy,attributeNamesList, xmlParent):
    outputAttributesList,outputGainList,outputAttributeWithGain,selectedIndex,outputAttributeNamesList = infoFetcher(df,attributesList,parentNodeEntropy,attributeNamesList)
    decision= outputAttributeNamesList[selectedIndex] 
    furtherDiv= outputAttributesList[selectedIndex]
    splitIndex = int(decision.replace(slice,''))
    #use the decision to initialize the tree
    updatedNameList = outputAttributeNamesList.copy()
    del updatedNameList[selectedIndex]
    updatedattributesList = outputAttributesList.copy()
    del updatedattributesList[selectedIndex]
    i=0
    xmlSubElementAttributes = {}
    while i < len(furtherDiv):
        xmlNode = xmlParent
        label= furtherDiv[i]
        nextDataFrame = subDataFrame(df,label,splitIndex)
        entropy,currentClassesCount =calculateEntropy(nextDataFrame,len(nextDataFrame.index))
        if(entropy==0):
            j=0
            pureSetLabel = ""
            while j < len (classLabels):
                if currentClassesCount[j]!=0:
                    pureSetLabel= classLabels[j]
                j=j+1
            xmlSubElementAttributes["entropy"] = "0.0"
            xmlSubElementAttributes["value"] = label
            xmlSubElementAttributes["feature"] = decision
            ET.SubElement(xmlParent, 'node', attrib = xmlSubElementAttributes).text = str(pureSetLabel)
            i=i+1
            continue
        else:
            xmlSubElementAttributes["entropy"] = str(entropy)
            xmlSubElementAttributes["value"] = label
            xmlSubElementAttributes["feature"] = decision
            xmlNode = ET.SubElement(xmlParent, 'node', attrib = xmlSubElementAttributes)
        attList,gainList,attNameToGain,maxGainIndex,attNameList = infoFetcher(nextDataFrame,updatedattributesList,entropy,updatedNameList)
        decisionTree(nextDataFrame, attList, entropy, attNameList, xmlNode)   
        i=i+1
    return

#invocation of decision tree function
decisionTree(dataFrame, attrList, treeEntropy, attrNameList, xmlRoot)

#writing into xml
xml = ET.ElementTree(xmlRoot)
xml.write(outputFileName)
print("ID3 has been performed successfully on the given dataset. The generated output is in the following XML: ",outputFileName)
