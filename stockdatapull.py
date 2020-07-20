# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas_datareader as web
from datetime import datetime, date
import pandas as pd

symbols = ["HDFCBANK.NS", "SBIN.NS", "AXISBANK.NS", "LT.NS", "HCLTECH.NS", "ULTRACEMCO.NS", "GAIL.NS", "AMBUJACEM.NS", "ASHOKLEY.NS", \
            "TVSMOTOR.NS", "JKLAKSHMI.NS", "JKTYRE.NS", "PFIZER.NS", "JSL.NS", "IOC.NS", "PHILIPCARB.NS", \
              "TCS.NS", "RELIANCE.NS", "INFY.NS", "ITC.NS", "HINDUNILVR.NS", "WIPRO.NS", "M&M.NS", "BHEL.NS", "CIPLA.NS"]
 

indices = ["^NSEI", "^NSEMDCP50", "^NSEBANK"]    
#end date updates automatically to the current date
start_date = datetime(2010,1,1)
end_date1 = date.today().strftime("%Y,%m,%d")
end_date = datetime.strptime(end_date1, "%Y,%m,%d")



#Pulling data from yahoo finance api using pandas datareader
#stock_data = web.get_data_yahoo(symbols, start_date, end_date)['Adj Close']

#stock_data.to_csv("C:/Users/SID/Downloads/SMC internship/stockdata.csv", index = True)

#pulling indices data for benchmarking
ind_data = web.get_data_yahoo(indices, start_date, end_date,)['Adj Close']
ind_data.to_csv("C:/Users/SID/Downloads/SMC internship/indexdata.csv", index = True)