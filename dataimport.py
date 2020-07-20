# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:30:20 2020

@author: SID
"""

"""
assumptions
equal weights
trading days 250
"""

import pandas as pd
import numpy as np

def get_data():
    df = pd.read_csv("C:/Users/SID/Downloads/SMC internship/stockdata.csv", index_col ="Date")
    
    #setting index as datetime to resample the returns as monthly
    df['Date'] = pd.to_datetime(df.index)
    df = df.set_index('Date')
    return df

def get_index_data():
    df1 = pd.read_csv("C:/Users/SID/Downloads/SMC internship/indexdata.csv", index_col ="Date")
    
    df1['Date'] = pd.to_datetime(df1.index)
    df1 = df1.set_index('Date')
    return df1

#Assigning weights for stocks
weights = []
for i in range(25):
    weights.append(0.04)
weights = np.array(weights)












