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


RECURSIVE FUNCTION NOT WORKING---- INFINITE LOOP

'''
import pandas as pd
import math
from lxml import etree

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

attrList = listOfValues.copy()
attrList.pop()
print(attrList)

''' WORKING CODE
gainValues = {}
gainList = []
entropyList = []
attr = 0
numOfRows = rowCount
while(attr < (len(attrList))):
    tempEntropyList = []
    tempEntropies = {}
    substractionTerm = 0.0
    for attrValue in attrList[attr]:
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
x = max(zip(gainValues.values(),gainValues.keys()))
y = x[1]
print("***************************************")
print("Choosen attr: attr",y)
print("***************************************")
print(entropyList[y])
print("***************************************")
'''
# //To modify this code---- not working
attrListIsNotEmpty = True
selectedNode = {}
dataSetLength = -1
def recursiveCalculations(df, parentNode, parsedNodes, selectedSplitNode):
    dataSetLength = len(df.index)
    if dataSetLength == 0:
        return 0
    else:
        for key,val in selectedSplitNode.items():
            numOfRows = df[parentNode].value_counts()[str(key)]
            updatedDF = pd.DataFrame(df.loc[dataFrame[parentNode] == str(key)])
            print(updatedDF)
            dataSetLength = len(updatedDF)
            print("Attr: ",parentNode," Key: ",str(key)," numOfRows: ",numOfRows)
            attr = 0
            entropyList.clear()
            gainList.clear()
            gainValues.clear()
            while(attr < (len(attrList))):
              #  tempEntropyList = []
                tempEntropies = {}
                substractionTerm = 0.0
                print(attr,"   ", attrList[attr])
                for attrValue in attrList[attr]:
                    if attr in parsedNodes:
                        substractionTerm = val
                        continue
                    else:
                        print("AttrValue: ",attrValue)                            
                        tempLen = updatedDF[attr].value_counts()[attrValue]
                        print("#########TEMPLEN: ",tempLen)
                        tempDF = pd.DataFrame(updatedDF.loc[dataFrame[attr] == attrValue][classColumnNum])
                        if len(tempDF[classColumnNum].unique() == 1): #pureset
                            print("Pureset at attr ",attr," for value- ",attrValue," Class- ",tempDF[classColumnNum])
                            continue
                        else: 
                            print("#########TEMPDF:")
                            print(tempDF)
                            tempEntropy = calculateEntropy(tempDF,tempLen)
                            print(tempEntropy)
                            tempEntropyList.append(tempEntropy)
                            tempEntropies[attrValue] = tempEntropy
                            prob = tempLen / numOfRows
                            substractionTerm = substractionTerm + (prob * tempEntropy)
                #print(tempEntropyList)
                #print(tempEntropies)
                #if not bool(tempEntropies):
                entropyList.append(tempEntropies)
                gain = val - substractionTerm
                if gain != 0:
                    gainList.append(gain)
                    gainValues[attr] = gain
                else:
                    gainValues[attr] = 0
                attr = attr + 1
        
            print("*************For attr")
            print("*************Entropy values")
            print(entropyList)
            print("*************Gain values")
            print(gainValues)
            maxGain = max(zip(gainValues.values(),gainValues.keys()))
            if maxGain != 0:
                maxGainAttr = maxGain[1]
                tempKey = str(maxGainAttr)
                maxGainValues[tempKey] = maxGain[0]
                print("***************************************")
                print("Choosen attr: ","attr",maxGainAttr)
                print("***************************************")
                print(entropyList[maxGainAttr])
                print("***************************************")
                #attrList.pop(selectedNodeIndex)
                tempNodes.append(maxGainAttr)
                print("TempNodes: ",tempNodes)
                print(maxGainValues)
                parsedNodes.extend(tempNodes)
                parsedNodes = list(set(parsedNodes)) #removing duplicates
                print("Parsed nodes: ",parsedNodes)
                dataSetLength = recursiveCalculations(updatedDF, maxGainAttr, parsedNodes, entropyList[maxGainAttr])
                print(dataSetLength)
            else:
                dataSetLength = 0
    
    return dataSetLength;

gainValues = {}
gainList = []
entropyList = []
attr = 0
parsedNodes = []
counter = 0
numOfRows = rowCount
dsLength = -1
while(attrListIsNotEmpty):
    if not bool(selectedNode):
        print("1")
        while(attr < (len(attrList))):
            print("2")
            tempEntropyList = []
            tempEntropies = {}
            substractionTerm = 0.0
            for attrValue in attrList[attr]:
                #print("AttrValue: ",attrValue)
                print("3")
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
        print("*************For attr")
        print("*************Entropy values")
        print(entropyList)
        print("*************Gain values")
        print(gainValues)
        maxGain = max(zip(gainValues.values(),gainValues.keys()))
        selectedNodeIndex = maxGain[1]
        selectedNode.clear()
        selectedNode = entropyList[selectedNodeIndex]
        parsedNodes.append(selectedNodeIndex)
        counter = counter + 1
        print("Selected node: ",selectedNode)

    else:
        print("ELSE: **************************************")
        nodeValueEntropies = {}
        tempNodes = []
        maxGainValues = {}
        for key,val in selectedNode.items():
            if val == 0.0:
                continue
            else:
                dsLength = recursiveCalculations(dataFrame, selectedNodeIndex, parsedNodes, selectedNode)
    if dsLength == 0:
        attrListIsNotEmpty = False
        
                #print(dataFrame)
'''
                numOfRows = dataFrame[selectedNodeIndex].value_counts()[str(key)]
                updatedDF = pd.DataFrame(dataFrame.loc[dataFrame[selectedNodeIndex] == str(key)])
                print("Attr: ",selectedNodeIndex," Key: ",str(key)," numOfRows: ",numOfRows)
                attr = 0
                entropyList.clear()
                gainList.clear()
                gainValues.clear()
                while(attr < (len(attrList))):
                    tempEntropyList = []
                    tempEntropies = {}
                    substractionTerm = 0.0
                    print(attr,"   ", attrList[attr])
                    for attrValue in attrList[attr]:
                        if attr in parsedNodes:
                            substractionTerm = val
                            continue
                        else:
                            print("AttrValue: ",attrValue)                            
                            tempLen = updatedDF[attr].value_counts()[attrValue]
                            tempDF =pd.DataFrame(updatedDF.loc[dataFrame[attr] == attrValue][classColumnNum])
                            tempEntropy = calculateEntropy(tempDF,tempLen)
                            #tempEntropyList.append(tempEntropy)
                            tempEntropies[attrValue] = tempEntropy
                            prob = tempLen / numOfRows
                            substractionTerm = substractionTerm + (prob * tempEntropy)
                    #print(tempEntropyList)
                    #print(tempEntropies)
                    #if not bool(tempEntropies):
                    entropyList.append(tempEntropies)
                    gain = val - substractionTerm
                    if gain != 0:
                        gainList.append(gain)
                        gainValues[attr] = gain
                    attr = attr + 1
    
                print("*************For attr",selectedNodeIndex)
                print("*************Entropy values")
                print(entropyList)
                print("*************Gain values")
                print(gainValues)
                maxGain = max(zip(gainValues.values(),gainValues.keys()))
                maxGainAttr = maxGain[1]
                tempKey = str(maxGainAttr)
                maxGainValues[tempKey] = maxGain[0]
                print("***************************************")
                print("Choosen attr: ","attr",maxGainAttr)
                print("***************************************")
                print(entropyList[maxGainAttr])
                print("***************************************")
                #attrList.pop(selectedNodeIndex)
                tempNodes.append(maxGainAttr)
                print("TempNodes: ",tempNodes)
                print(maxGainValues)
       
        print(tempNodes)
        selectedNode.clear()
        selectedNode = entropyList[selectedNodeIndex]
        print(selectedNode)
        parsedNodes.extend(tempNodes)
        parsedNodes = list(set(parsedNodes)) #removing duplicates
        print("Parsed nodes: ",parsedNodes)
        counter = counter + 1
        print(maxGainValues)
        print("Counter: ",counter)
    if(len(parsedNodes) == columnCount - 1):
        attrListIsNotEmpty = False'''
    

  # HAVE TO UPDATE SELECTED INDEX!                      
                







''' //Working xml code... to add later
root = etree.Element('tree',entropy = str(treeEntropy))
print(etree.tostring(root))
for key,val in entropyList[y].items():
    z = etree.SubElement(root, 'node', entropy = str(val), value = str(key), feature = "attr"+str(y))
print(etree.tostring(root))
'''

