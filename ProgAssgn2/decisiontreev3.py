# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:35:24 2018

@author: rahut
"""

import pandas as pd
import math
import xml.etree.ElementTree as ET
#from lxml import etree
# rahul's csv path :  E://courses' materials//drittes Semester//Machine Learning//Prog Ass//ProgAssgn2//decisiontree/car.csv
#sruthi'S csv path : D://car.csv

dataFrame = pd.read_csv("D://car.csv", header = None)
listOfValues = []
print(dataFrame)
print(dataFrame[0])

for i, item in dataFrame.iteritems():
    temp = item.unique()
    listOfValues.append(temp.tolist())
print(listOfValues)

rowCount = len(dataFrame.index)
print("Num of rows: ",rowCount)

columnCount = len(dataFrame.columns)
print("Num of columns: ",columnCount)

noOfClasses = len(listOfValues[len(listOfValues)-1])
print(noOfClasses)
classColumnNum = columnCount - 1
print(listOfValues[classColumnNum])

classLabels= listOfValues[classColumnNum]


def calculateEntropy(df, numOfRows): 
        classesCount = []
        for label in listOfValues[classColumnNum]:
            if(label in df.values):
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

treeEntropy,classesCountOpt = calculateEntropy(dataFrame,rowCount)
print("Tree Entropy: ",treeEntropy)
print('classesCount for tree entropy',classesCountOpt )

attrList = listOfValues.copy()
attrList.pop()
print(attrList)


def subDataFrame(df,attrValue,attrNo):    
    sdf = df[df[attrNo]==attrValue]
    return sdf


def calculateGain(mainEntropy,entropyList,dfLength,sdfLength):
    i=0
    gain = mainEntropy
    while i< len(entropyList):
        gain = gain - (sdfLength/dfLength)*(entropyList[i])
        i= i+1
    return gain

def infoFetcher(df, aList,currentRootEntropy,attrNameListLocal):
    entropyList= []
    listOfEntropyLists = []
    gainList= []
    nameToGain ={}
    
    print(attrNameListLocal)
    i=0
    while i< len(aList):
        r=0
       
        for label in aList[i]:
            sdf= subDataFrame(df,label,i)
            noOfRows= len(sdf.index)
            tempEntropy,tempClassesCount = calculateEntropy(sdf,noOfRows)
           
            if r < len(aList[i]):
                entropyList.append(tempEntropy)
            if r==len(aList[i])-1:
                listOfEntropyLists.append(entropyList)
                entropyList= []
            r=r+1
        tempGain= calculateGain(currentRootEntropy,listOfEntropyLists[i],len(df.index),len(sdf.index))
        gainList.append(tempGain)
        i=i+1
    #hashmap for attnames and gains
    j=0
    while j< len(gainList):
        nameToGain[attrNameListLocal[j]]= gainList [j]
        j=j+1
    maxGain = max(gainList)
    maxGainIndex= gainList.index(maxGain)
    return aList, gainList,nameToGain,maxGainIndex,attrNameListLocal

a=0
attrNameList= []
while a< len(attrList):
        temp = "attr"+ str(a)
        attrNameList.append(temp)
        a=a+1
print(attrNameList)


slice = 'attr'
root = ET.Element('tree', entropy = str(treeEntropy))

def recursiveFunc(df,atList,plantEntropy,aNameList, xmlParent):     #Note: pop the element out once you get the index out
    optAlist,optGainList,Att2Gain,selIndex,optAnameList = infoFetcher(df,atList,plantEntropy,aNameList)
    print('attribute List :',optAlist)
    print('gain List :',optGainList)
    print('attribute to Gain :',Att2Gain)
    print('Selected Index :',selIndex)
    print('attribute name list :',optAnameList)
    decision= optAnameList[selIndex] #make xmlhere
    furtherDiv= optAlist[selIndex]
    print(furtherDiv)
    cuttingIndexNum = int(decision.replace(slice,''))
    print(cuttingIndexNum)
    ##########use the decision to initialize the tree
    updatedNameList = optAnameList.copy()
    print(updatedNameList)
    del updatedNameList[selIndex]
    print(updatedNameList)
    updatedaList = optAlist.copy()
    del updatedaList[selIndex]
    i=0
    subElementAttributes = {}
    while i < len(furtherDiv):
        node = xmlParent
        label= furtherDiv[i]
        print('decisionvalue',label)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        nextDataFrame = subDataFrame(df,label,cuttingIndexNum)
        ent,localClassesCount =calculateEntropy(nextDataFrame,len(nextDataFrame.index))
        print(ent)
        if(ent==0):
            j=0
            non0Class = ""
            while j < len (classLabels):
                if localClassesCount[j]!=0:
                    non0Class= classLabels[j]
                #take non0class and print to xml
                j=j+1
            subElementAttributes["entropy"] = "0.0"
            subElementAttributes["value"] = label
            subElementAttributes["feature"] = decision
            ET.SubElement(xmlParent, 'node', attrib = subElementAttributes).text = str(non0Class)
            i=i+1
            continue
        else:
            subElementAttributes["entropy"] = str(ent)
            subElementAttributes["value"] = label
            subElementAttributes["feature"] = decision
            node = ET.SubElement(xmlParent, 'node', attrib = subElementAttributes)
        a,b,c,d,e = infoFetcher(nextDataFrame,updatedaList,ent,updatedNameList)
        print('attribute List :',a)
        print('gain List :',b)
        print('attribute to Gain :',c)
        print('Selected Index :',d)
        print('attribute name list :',e)
        recursiveFunc(nextDataFrame, a, ent, e, node)   
        i=i+1
    return

recursiveFunc(dataFrame, attrList, treeEntropy, attrNameList, root)
print(ET.tostring(root))
