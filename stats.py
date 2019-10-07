#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re
import os
import xlsxwriter
import time

engine = 'openpyxl'
sheetName = input("enter excel file name: ")
df = pd.read_excel(sheetName, skip_blank_lines=False)
header = list(df)
df.rename(columns={header[0] : "class", header[1] : sheetName, header[2] : "counts"},\
                                                                    inplace=True)
print(df)
