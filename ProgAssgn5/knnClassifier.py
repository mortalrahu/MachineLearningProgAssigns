# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:47:57 2018

@authors: Srilakshmi Sruthi Pasumarthy(220651)
          Rahul Gupta Kodarapu(220850)
          Abdullah Al Zubaer(218074)
"""
import pandas as pd
#import csv
#import sys

#Rahul's path = C://Users//rahut//Documents//GitHub//MachineLearningProgAssigns//ProgAssgn4//nb//Example.tsv
#Sruti's Path = 

inputFileName ="C://Users//rahut//Documents//GitHub//MachineLearningProgAssigns//ProgAssgn5//kNN//Example-shuffled.tsv" #sys.argv[1]
#outputFileName = sys.argv[2]

dataFrame = pd.read_csv(inputFileName,sep = '\t',header = None)
#learningRate = 1
#MAX_NUM_OF_ITERATIONS = 100

rowCount = len(dataFrame.index)
columnCount = len(dataFrame.columns)
dataFrame.dropna()
if(pd.isnull(dataFrame.iloc[0][columnCount-1]) == True):
    dataFrame = dataFrame.drop(columnCount-1,axis=1)
columnCount = len(dataFrame.columns)
#print(dataFrame)
#print(columnCount)