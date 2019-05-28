#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re
import os
import xlsxwriter
import time
engine = 'openpyxl'
os.chdir(r"test")
mainDir = os.listdir(".")
fasl = "##########################################"
# LOOP in main directory
for subDir in mainDir:
    print ("loop in main directory of {}".format(subDir) + "\n" + fasl)
    try:
        time.sleep(3)
        os.chdir(r"{}".format(subDir))
        subDirList = os.listdir(".")
        print (subDirList)
# LOOP in each teacher director
        i = 1 # start datafram name with df1
        listDf = [] # array of DataFrame
        listKey = [] # array of keys
        for sN in subDirList:
            sheetName = sN[0:-5]
            print (fasl + "\n" +sheetName + "\n" + fasl + "\n")
            try:
                df = pd.read_excel(sheetName + ".xlsx", skip_blank_lines=False)
                df = df.filter(regex='^(?!Unnamed).*') # remove unnamed columns
                try:
                    nameCount = df['Name'].count()
                    df = df.iloc[1:nameCount+1]
                    # dfSummary = df.count()
                    # print(dfSummary)
                except:
                    try:
                        df['name']
                        nameCount = df['name'].count()
                        df = df.iloc[1:nameCount+1]
                        # dfSummary = df.count()
                        # print(dfSummary)
                    except:
                        print(fasl + "\nName column not found!\n" + fasl)
                df = df.count().rename_axis(subDir).to_frame('counts')
                listDf.append(df)
                listKey.append(sheetName)
            except:
                print("###############")
                print (sN + "{} is not in xlsx format".format(sheetName))
                print("###############")
        newdf = pd.concat(listDf, keys = listKey)
        newdf.to_excel(subDir + "Summary" + ".xlsx", engine=engine)
    except:
        print ("{} is not directory".format(subDir))



# engine = 'openpyxl'
# dfSummary.to_excel(sheetName + ".xlsx", engine=engine)
#print (df.columns.get_loc("Aug"))
#print (df['Sept.'].value_counts())
#print (df['Sept.'].count())
#print (df['Name'].count())
#print (list(df))
