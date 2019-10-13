#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re
import re
import os
import xlsxwriter
# use of json package
import json
import re

stats= {}
excelFile = "attendSummary.xlsx"

# read excel file to create DataFrame sheet
df = pd.ExcelFile(excelFile)
sheetNames = df.sheet_names
print(sheetNames)
i = 0
for sheet in sheetNames:
    # READ specific excell sheet_name dfs
    dfs = pd.read_excel(excelFile, sheet_name=sheet)
    width = dfs.shape[1]
    stats[sheet] = {}
    # READ list for columns in each sheet
    # header = list(dfs)
    columns = dfs.columns.tolist()
    colList = []
    for col in columns:
        if not ("unnamed" in col.lower()):
            colList.append(col)


    for col in colList:
        stats[sheet][col] = {}
        j = 0
        colIndex = dfs.columns.get_loc(col) # get index of col with name
        # obj = dfs.loc[0].at[colIndex] # get the value of Name column
        obj = dfs.iat[0, colIndex]
        stats[sheet][col]["SUM"] = dfs.iat[2, colIndex] # get count of Name column
        colIndex += 1
        while True:
            obj = dfs.iat[0, colIndex]
            obj = obj.lower()
            if re.search("sep.*", obj):
                obj = "Sep"
                stats[sheet][col][obj] = dfs.iat[2, colIndex]
            elif (re.search("oct.*", obj)):
                obj = "Oct"
                stats[sheet][col][obj] = dfs.iat[2, colIndex]
            elif re.search("aug.*", obj):
                obj = "Aug"
                stats[sheet][col][obj] = dfs.iat[2, colIndex]
            else:
                stats[sheet][col][obj] = dfs.iat[2, colIndex]

            if stats[sheet][col]["SUM"] > 0:
                stats[sheet][col][obj + "_%"] = round(((dfs.iat[2, colIndex]\
                                        /stats[sheet][col]["SUM"])*100), 1)
            j +=1
            colIndex += 1
            if colIndex >= width:
                break
            if ((j >= 5) or ("name" in (dfs.iat[0, colIndex].lower()))):
                break


print(stats['M.Basem Rashed']['B2_Sat_8-Al'])
#print(i)

with open('data.json', 'w') as outfile:
    json.dump(stats, outfile)

"""



primaryIp = dfs.columns.get_loc("RNC")

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
