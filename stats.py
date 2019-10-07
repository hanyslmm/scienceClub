#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re
import re
import os
import xlsxwriter
import time

excelFile = "Science Club 2019_2020/attendSummary.xlsx"

# read excel file to create DataFrame sheet
df = pd.ExcelFile(excelFile)
sheetNames = df.sheet_names
print(sheetNames)
i = 0
for sheet in sheetNames:
    # READ specific excell sheet_name dfs
    dfs = pd.read_excel(excelFile, sheet_name=sheet)
    # READ list for columns in each sheet
    # header = list(dfs)
    print(dfs.shape)
    columns = dfs.columns.tolist()
    for col in columns:
        if not ("unnamed" in col.lower()):
            print(dfs.get_value(0, col)) #



    """primaryIp = dfs.columns.get_loc("RNC")

    primaryIp = int(primaryIp)
    secondaryIp = primaryIp + 2
    # CREATE new DataFrame RNC_name and it's IPs
    newdf = dfs.iloc[1:, primaryIp:secondaryIp]
    # GET list of columns header name and print
    header = list(newdf)
    # CHANGE columns header name
    newdf.rename(columns={header[0] : "primaryIp", header[1] : "secondaryIp"},\
                                                                    inplace=True)
    # TO change column name from RNCNUM to RNC NUM using split
    rncName = re.split('(\d.*)', sheet)
    # df.to_csv(file_name, sep='\t', encoding='utf-8')
    rncName = rncName[0] + " " + rncName[1]
    # ADDING the new column named RNC_Name
    newdf["RNC_Name"] = rncName
    # CHANGE columes order
    cols = newdf.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    newdf = newdf[cols]
    # CREATE empty DataFrame
    if i == 0:
        olddf = pd.DataFrame(columns=cols)
        i = 1
    olddf = pd.concat([olddf, newdf])

# EXPORT DataFrame to csv and excell
engine = 'openpyxl'
olddf.to_csv('extractedIps.csv')
olddf.to_excel('extractedIps.xlsx', engine=engine)
print ("Congratulation IPs successfully exported to extractedIps.csv and \
                                                            extractedIps.xlsx ")
                                                            """
