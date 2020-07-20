# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 03:18:32 2020

@author: SID
"""

"""
code for plotting charts for calculations done in calculations.py
"""
import matplotlib.pyplot as plt
from calculations import *
import seaborn as sns



#plotting returns of stocks
col = get_m_returns(df).columns

def plot_m_returns(df):
    #l = len(m_returns.columns)
    plt.figure(figsize = (45,20))
    m_returns = get_m_returns(df)
    
    for i in range(len(m_returns.columns)):
        plt.subplot(14,2,i+1)
        plt.plot(m_returns[col[i]])
        plt.title(col[i])
    plt.tight_layout()
    plt.show()

   
#plotting protfolio returns
def plot_pf_returns(df):
    plt.figure(figsize=(5,2))
    plt.plot(get_pf_returns(df))
    plt.title("RETURNS OF PORTFOLIO OVER TIME")
    plt.show()

    
    
    
#plotting drawdown of the portfolio
def plot_drawdown(df):
    plt.figure()
    plt.plot(get_wealth_index(df))
    plt.plot(get_peaks(df))
    plt.xlabel("Maximum drawdown: " + str(get_drawdown(df)))
    plt.title("PORTFOLIO DRAWDOWN")
    plt.show()



#plotting drawdown of the index
def plot_ind_drawdown(df):
    plt.figure()
    plt.plot(get_ind_wealth_index(df))
    plt.plot(get_ind_peaks(df))



    

#plotting returns of portfolio vs indices
def plot_benchmark(df,df1):
    #l = len(m_returns.columns)
    plt.figure(figsize = (20,len(df1.columns)*4))
    pf_returns = get_pf_returns(df)
    index_returns = get_a_returns(df1)

    for i in range(len(df1.columns)):
        plt.subplot(len(df1.columns),1,i+1)
        plt.plot(pf_returns.values, linewidth=3, label = "portfolio")
        plt.plot(index_returns.iloc[:,i].values, linestyle='dashed', label = "index")
        plt.title(index_returns.columns[i])

        
        #plt.tight_layout()
        plt.legend()
    plt.show()





       
#print(df1.columns.shape())

#plotting correlation matrix of all stocks in portfolio
def plot_corr_matrix(df):
    m_returns = get_m_returns(df)
    corr = m_returns.corr()
    plt.figure(figsize = (20,15))
    matrix = sns.heatmap(corr, annot = True)
    plt.show()
    #return matrix

#plot portfolio value over time
def plot_pf_value(df,amt = 5000000):
        x= []
        y = []
        for i in range(2010,2021):
            x.append(round(((get_pf_value(df,i)+1)*amt),2))
            y.append(i)
        
        #show pf value
        table_value = pd.DataFrame()
        table_value["YEAR"] = np.array(y)
        table_value["AMOUNT"] = np.array(x)
        print(table_value)
        
        #plot pf value
        fig,ax = plt.subplots()
        ax.plot(y,x)
        plt.title("Portfolio wealth over the years")
        plt.ylabel("Amount in crores")

        plt.show()



        

#pf_returns = get_pf_returns(df)
#print(pf_returns.index.year)

