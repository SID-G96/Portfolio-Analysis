# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:53:42 2020

@author: SID
"""


"""
file for calculations


assumptions
risk free rate rf = 6%
all calcualtions for period 2010 -2020

"""

#module imports

import pandas as pd
import numpy as np
from dataimport import *
import scipy.stats as si

#gettiing stock data from file dataimport
df = get_data()
df1= get_index_data()

#daily return
def get_d_returns(df):
    d_returns = df.pct_change()
    return d_returns
#d_returns = get_d_returns(df)
#d_i_returns = get_d_returns(df1)

#monthly compounded returns
def get_m_returns(df):
     #converting daily returns to monthly returns
    d_returns = get_d_returns(df)
    m_returns = d_returns.resample('m').agg(lambda x: (x + 1).prod() - 1)
    return m_returns 
#m_returns = get_m_returns(df)
#m_i_returns = get_m_returns(df1)
#annual compunded returns
def get_a_returns(df):
    #converting monthly returns to annual returns
    m_returns = get_m_returns(df)
    a_returns = m_returns.resample("y").agg(lambda y: (y +1).prod() -1)
    
    return a_returns
#a_returns = get_a_returns(df)
#a_i_returns = get_a_returns(df1)

#calculating annulised volatility of stocks
def get_a_volatility(df):
    m_returns = get_m_returns(df)
    a_volatility = m_returns.resample("y").agg(lambda z : z.std()*np.sqrt(12))
    return a_volatility
    

#total portfolio volatility
def get_pf_volatility(df):
    a_returns = get_a_returns(df)
    #preparing covariance matrix for calculating volatility
    cov_m = get_m_returns(df).cov() * a_returns.shape[0]
    
    #calculating portfolio volatility
    pf_var = np.dot(weights.T, np.dot(cov_m, weights))
    return pf_var


#getting annualised portfolio rate of returns
def get_pf_returns(df):
    pf_returns = get_a_returns(df).dot(weights)
    
    return pf_returns


#calculating average annual returns
def get_aar(df):
    aar = get_a_returns(df).mean()
    return aar

def get_pf_aar(df):
    pf_aar = get_pf_returns(df).mean()
    return pf_aar

#monthly portfolio returns for internal calculation
def get_m_pf_returns(df):
    m_pf_returns = get_m_returns(df).dot(weights)
    return m_pf_returns


#calculate drawdown of portfolio returns over the entire period
def get_drawdown(df):
    
      
    #calculating wealth index 
    wealth_index = 1000*(1+get_m_pf_returns(df)).cumprod()
    peaks = wealth_index.cummax()
    #calculating drawdown
    drawdown = (wealth_index - peaks)/peaks
    #rounding and adjusting value for display
    adj_value = str(round(((drawdown.min()*100)*-1),2)) + "%"
    adj_date = drawdown.idxmin().strftime("%d-%b-%Y")
    return adj_value, adj_date

def get_wealth_index(df):
    return 1000*(1+get_m_pf_returns(df)).cumprod()

def get_peaks(df):
    return 1000*(1+get_m_pf_returns(df)).cumprod().cummax()


#calcualting index drawdowns
def get_ind_drawdown(df):
    
      
    #calculating wealth index 
    wealth_index = 1000*(1+get_m_returns(df)).cumprod()
    peaks = wealth_index.cummax()
    #calculating drawdown
    drawdown = (wealth_index - peaks)/peaks
    #rounding and adjusting value for display
    adj_value = str(round(((drawdown.min()*100)*-1),2)) + "%"
    adj_date = drawdown.idxmin().strftime("%d-%b-%Y")
    return adj_value, adj_date

def get_ind_wealth_index(df):
    return 1000*(1+get_m_returns(df)).cumprod()

def get_ind_peaks(df):
    return 1000*(1+get_m_returns(df)).cumprod().cummax()



    

#calculating Value at risk for 5% level of confidence
""" since the returns from the data are not normally distributed we need to 
find modified VaR ( cornish fisher modification)

to explain that returns are not normally distributed we will run a jarque-bera test 
for normality
"""

def get_jb_test(df, col = 0):
    return si.jarque_bera(get_a_returns(df).iloc[:,col])
    """thus the p value is much greater and hence proved that return series
    have much fatter tails and are not normally distributed"""
#.iloc[:,col]  
#k, p = get_jb_test(df)
#print(p)


def get_var_modified(df):
    k = si.kurtosis(get_m_pf_returns(df))
    s = si.skew(get_m_pf_returns(df))
    #getting z score for normally distributed data
    z = si.norm.ppf(0.05)
    
    #applying cornish fisher modification to z score
    z = (z + (z**2 - 1)*s/6 + (z**3 -3*z)*(k-3)/24 -(2*z**3 - 5*z)*(s**2)/36)
  
    var = -(get_m_pf_returns(df).mean() + z*get_m_pf_returns(df).std())
    return var

#calculating shapre ratio for portfolio
def get_sharpe_ratio(df, rf=0.06):
    pf_returns = get_pf_returns(df)
    pf_volatility = get_pf_volatility(df)
    sharpe = (pf_returns - rf)/pf_volatility
    sharpe = sharpe.mean()
    return sharpe
        

#calcutating portfolio beta
""" we can calculate beta by regressing our portfolio returns against the index returns
using sci py library
"""
    # returns beta and alpha both
def get_pf_beta(df,df1):
    col_len = df1.columns
    m_pf_returns = get_m_pf_returns(df)
    m_index_returns = get_m_returns(df1)
    beta = []
    alpha=[]
    """
    the function returns beta for all market index data that is passed as 2nd arguement
    """
    for i in col_len:
        b, a = si.linregress(m_index_returns.loc[:,i],m_pf_returns)[0:2]
        beta.append(round(b,2))
        alpha.append(round(a,2))
    return beta , alpha


#calculating treynor ratio for reward per unit of risk

def get_treynor_ratio(df, rf= 0.06):
    beta = get_pf_beta(df, df1)[0]
    #calculating for all betas
    pf_returns = get_pf_returns(df)
    #print(pf_returns)
    ratio_list = [(pf_returns - rf)/beta[i] for i in range(len(beta))]
    
    ratio = np.array(ratio_list)
    treynor = np.mean(ratio, axis = 1)
    return treynor
   

#calculate portfolio value held for n years for amt invested
def get_pf_value(df, year = 2020):
    pf_returns = get_pf_returns(df)
    pf_returns.index = pf_returns.index.year
    pf_value = ((pf_returns.loc[:year,] + 1).prod() - 1)
    return pf_value

#print(get_pf_value(df))
#.iloc[:i,]    
#sector allocation
#map the weights to sectors

#calculate value of 50 lakhs invested in 2015,2016        

