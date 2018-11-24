# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:35:24 2018

@author: rahut
"""

import pandas as pd
import math
#from lxml import etree
# rahul's csv path :  E://courses' materials//drittes Semester//Machine Learning//Prog Ass//ProgAssgn2//decisiontree/car.csv
#sruthi'S csv path : D://car.csv

dataFrame = pd.read_csv("E://courses' materials//drittes Semester//Machine Learning//Prog Ass//ProgAssgn2//decisiontree/car.csv", header = None)
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
print(dataFrame.values)
print(dataFrame.iloc[[2]]) #location index
print(dataFrame.loc[[2]]) # acc to assigned value
print(dataFrame.iat[2,6]) # location iundex
print(dataFrame.at[2,6]) # acc to assigned value
#for us both are the same
classLabels= listOfValues[classColumnNum]


def calculateEntropy(df, numOfRows): 
        classesCount = []
        for label in listOfValues[classColumnNum]:
            print(label," ",label in df.values)
            if(label in df.values):
                temp = df[classColumnNum].value_counts()[label]
                print(temp)
                classesCount.append(temp)
            else:
                classesCount.append(0)
        print(classesCount)
        
        entropy = 0.0
        for i in classesCount:
            if(i > 0):
                probabilityValue = i / numOfRows
                entropy = entropy - (probabilityValue * (math.log(probabilityValue)/math.log(len(classesCount))))
            else:
                continue
#        if(entropy == 0):
#            j=0
#            while j < len (classLabels):
#                if classesCount[j]!=0:
#                    non0Class= classLabels[j]
#                    print('nonZeroClass for Entropy 0.0 case',non0Class)
#                    return entropy,j
#                #non0Class = classesCount[j]
#                j=j+1
        return entropy,classesCount  

treeEntropy,classesCountOpt = calculateEntropy(dataFrame,rowCount)
print("Tree Entropy: ",treeEntropy)
print('classesCount for tree entropy',classesCountOpt )

attrList = listOfValues.copy()
attrList.pop()
print(attrList)

#sdf = dataFrame[dataFrame[0] == "low"]
#print(sdf)

def subDataFrame(df,attrValue,attrNo):    
    sdf = df[df[attrNo]==attrValue]
    return sdf

#sdf= subDataFrame(dataFrame,"low",0)
#print(sdf)

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
    #listOfLabelToEntropy= []
    nameToGain ={}
    
    print(attrNameListLocal)
    i=0
    while i< len(aList):
        #labelToEntropy ={}
        r=0
        #k=0
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')             
        print('i=',i)
        print(aList[i])
        print(len(aList[i]))
        print('########################################################')
        for label in aList[i]:
            sdf= subDataFrame(df,label,i)
            print(label,i)
            noOfRows= len(sdf.index)
            tempEntropy,tempClassesCount = calculateEntropy(sdf,noOfRows)
            print(sdf,noOfRows)
            print(tempEntropy)
            if r < len(aList[i]):
                entropyList.append(tempEntropy)
                print(entropyList)
                print('---------------------------------------------')             
            if r==len(aList[i])-1:
                listOfEntropyLists.append(entropyList)
                print('loel',listOfEntropyLists)
                entropyList= []
            r=r+1
            print('r=',r)
            print('**************************************************')             
            #while k< len(aList[i]):
             #   x= aList[i].copy()
              #  labelToEntropy[attrNameList[k]]= x[k]
               # k=k+1
        tempGain= calculateGain(currentRootEntropy,listOfEntropyLists[i],len(df.index),len(sdf.index))
        gainList.append(tempGain)
        #listOfLabelToEntropy.append(labelToEntropy)
        i=i+1
    #hashmap for attnames and gains
    j=0
    while j< len(gainList):
        nameToGain[attrNameListLocal[j]]= gainList [j]
        j=j+1
    maxGain = max(gainList)
    maxGainIndex= gainList.index(maxGain)
    #aList.pop(maxGainIndex)
    return aList, gainList,nameToGain,maxGainIndex,attrNameListLocal
a=0
attrNameList= []
while a< len(attrList):
        temp = "attr"+ str(a)
        attrNameList.append(temp)
        a=a+1
print(attrNameList)

#a,b,c,d,e = infoFetcher(dataFrame,attrList,treeEntropy,attrNameList)
#print('attribute List :',a)
#print('gain List :',b)
#print('attribute to Gain :',c)
#print('Selected Index :',d)
#print('attribute name list :',e)
#print(f)
slice = 'attr'
def recursiveFunc(df,atList,plantEntropy,aNameList):     #Note: pop the element out once you get the index out
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
    while i < len(furtherDiv):
        print('#3')
        label= furtherDiv[i]
        print(label)
        print('decision',decision)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        nextDataFrame = subDataFrame(df,label,cuttingIndexNum)
        print(nextDataFrame)
        ent,localClassesCount =calculateEntropy(nextDataFrame,len(nextDataFrame.index))
        print(updatedaList)
        print(ent)
        if(ent==0):
            j=0
            while j < len (classLabels):
                if localClassesCount[j]!=0:
                    non0Class= classLabels[j]
                    print('#1')
                    print('nonZeroClass for Entropy 0.0 case: ',non0Class)
                    print('#2')
                #take non0class and print to xml
                j=j+1
            i=i+1
            print('i:',i)
            continue
        print(updatedNameList)
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        a,b,c,d,e = infoFetcher(nextDataFrame,updatedaList,ent,updatedNameList)
        print('attribute List :',a)
        print('gain List :',b)
        print('attribute to Gain :',c)
        print('Selected Index :',d)
        print('attribute name list :',e)
        recursiveFunc(nextDataFrame,a,ent,e)   
        i=i+1
    return

recursiveFunc(dataFrame,attrList,treeEntropy,attrNameList)
