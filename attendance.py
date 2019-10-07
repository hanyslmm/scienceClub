#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re
import os
import xlsxwriter
import time
engine = 'openpyxl'
mainDirName = input("enter main directory name: ") #"science club 2019_2020"
os.chdir(r"{}".format(mainDirName))
cwDir = os.getcwd()
mainDir = os.listdir(".")
fasl = "##########################################"
command = "find . -mindepth 2 -type f -print -exec mv {} . \;"
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('attendSummary.xlsx', engine='xlsxwriter')
# LOOP in main directory
print (mainDir)
for subDir in mainDir:
    print ("loop in main directory of {}".format(subDir) + "\n" + fasl)
    try:
        #time.sleep(3)
        os.chdir(r"{}".format(subDir))
        os.system(command)
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
                        print(fasl + "\nName column not found! in: " + sheetName)
                df = df.count()#.rename_axis(subDir).to_frame('counts')
                listDf.append(df)
                listKey.append(sheetName)

                # print(listDf)
                # print(listKey)
            except:
                print("###############")
                print (sN + "{} is not in xlsx format".format(sheetName))
                print("###############")
        newdf = pd.concat(listDf, keys = listKey)
        #newdf.rename(columns = {list(newdf)[0]: 'Class'}, inplace = True)
        newdf = newdf.to_frame()

        print("columns name??????")
        print(type(newdf))
        #newdf.columns = ['Col_1', 'Col_2', 'test']


        #newdf.rename(columns = {'Unnamed: 0': 'class'}, inplace = True)
        os.chdir(r"{}".format(cwDir))
        print("change directory to "+os.getcwd())
        newdf.to_excel(subDir + "_Summary" + ".xlsx", engine='xlsxwriter')


        # Convert the dataframe to an XlsxWriter Excel object.
        newdf.to_excel(writer, sheet_name=subDir)



    except:
        print ("{} is not directory".format(subDir))
        os.chdir(r"{}".format(cwDir))


# Close the Pandas Excel writer and output the Excel file.
writer.save()

# engine = 'openpyxl'
# dfSummary.to_excel(sheetName + ".xlsx", engine=engine)
#print (df.columns.get_loc("Aug"))
#print (df['Sept.'].value_counts())
#print (df['Sept.'].count())
#print (df['Name'].count())
#print (list(df))
