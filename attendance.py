#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import re
import os
listDir = os.listdir("MR.Basem Sun")
print (os.getcwd())
os.chdir(r"MR.Basem Sun")
print (os.getcwd())
for sN in listDir:
    sheetName = sN[0:-5]
    print (sheetName)
    df = pd.read_excel(sheetName + ".xlsx", skip_blank_lines=False)
    #listCol = list(df)
    #regex = re.compile(r"Unnamed*")
    #listUname = list(filter(regex.match, listCol))
    # GET list of required remove unnamed columns
    #listReq = list(set(listCol).difference(set(listUname)))
    dfF = df.filter(regex='^(?!Unnamed).*')
    try:
        dfF['Name']
        nameCount = dfF['Name'].count()
        dfF = dfF.iloc[1:nameCount+1]
        dfSummary = dfF.count()
        print(nameCount)
        print(dfSummary)
    except:
        print("name not found")

    # engine = 'openpyxl'
    # dfSummary.to_excel(sheetName + ".xlsx", engine=engine)
#print (df.columns.get_loc("Aug"))
#print (df['Sept.'].value_counts())
#print (df['Sept.'].count())
#print (df['Name'].count())
#print (list(df))
