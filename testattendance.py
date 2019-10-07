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
# LOOP in main directory
print (mainDir)
for subDir in mainDir:
    print ("loop in main directory of {}".format(subDir) + "\n" + fasl)

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
#            try:
        df = pd.read_excel(sheetName + ".xlsx", skip_blank_lines=False)
        df = df.filter(regex='^(?!Unnamed).*') # remove unnamed columns
