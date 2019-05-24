#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re
import os
os.chdir(r"test")
mainDir = os.listdir(".")
for subDir in mainDir:
    print ("#############\n")
    os.chdir(r"{}".format(subDir))
    print (os.getcwd())
    subDir = os.listdir(".")
    for sN in subDir:
        sheetName = sN[0:-5]
        print ("#############")
        print (sheetName)
        print ("#############")
        try:
            df = pd.read_excel(sheetName + ".xlsx", skip_blank_lines=False)
            dfF = df.filter(regex='^(?!Unnamed).*') # remove unnamed columns
        except:
            print("###############")
            print (sN + "{} is not in xlsx format".format(sheetName))
            print("###############")
        try:
            dfF['Name']
            nameCount = dfF['Name'].count()
            dfF = dfF.iloc[1:nameCount+1]
            dfSummary = dfF.count()
            print(dfSummary)
        except:
            try:
                dfF['name']
                nameCount = dfF['name'].count()
                dfF = dfF.iloc[1:nameCount+1]
                dfSummary = dfF.count()
                print(dfSummary)
            except:
                print("###############")
                print("Name not found!")
                print("###############")
    os.chdir("..")

    # engine = 'openpyxl'
    # dfSummary.to_excel(sheetName + ".xlsx", engine=engine)
#print (df.columns.get_loc("Aug"))
#print (df['Sept.'].value_counts())
#print (df['Sept.'].count())
#print (df['Name'].count())
#print (list(df))
