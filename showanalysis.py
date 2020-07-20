# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 17:34:49 2020

@author: SID
"""


"""
user file for showing all information and analysis done on portfolio
"""

from calculations import *
from plotcode import *


def print_assets():
    #showing assets in the porfolio
    print(" THE ASSETS IN THE PORTFOLIO ARE - ")
    print(df.columns.values)


def print_asset_corr():
    
    #plotting correlation between portfolio assets
    print("Plotting correlation between the assets on a heatmap: \n")
    plot_corr_matrix(df)

def print_individual_returns():
    
    #returns of indivdual assets in the portfolio
    print("\n The returns of invidual assets: \n")
    print(round(get_a_returns(df)*100,2))
    plot_m_returns(df)


def print_pf_returns():
    #showing Returns and volatility of portfolio
    print(" The returns of the portfolio: \n")
    print(round(get_pf_returns(df)*100,2))
    plot_pf_returns(df)
    
    print("\n The average annual return: ")
    print(str(round(get_pf_aar(df)*100,2)) + "%")
    print("\n The volatility of portfolio is: ")
    print(str(round(get_pf_volatility(df)*100,2)) + "%")


def print_drawdowns():
    #drawdowns of indices vs drawdowns of portfolio
    print("\n\nThe drawdowns in index : ")
    
    for i in range(len(df1.columns)):
        plot_ind_drawdown(df1.iloc[:,i])
        plt.xlabel("Maximum drawdown: " + str(get_ind_drawdown(df1.iloc[:,i])))
        plt.title("{} DRAWDOWN".format(df1.columns[i]))
        plt.show()

    
    print("\n\nThe drawdowns in portfolio is : ")
    plot_drawdown(df)



def print_benchmark():            
    #plotting returns against benhcmark
    print("\n\n Benchmarking Portfolio reutrns: \n")
    plot_benchmark(df, df1)
    
print_benchmark()

def print_var():
    #display portfolio's Value at risk and describing data distribution
    print("\nOn Running a Jaerque-Bera test it can be ascertained that returns are")
    print("NOT normally distributed.\n")
    print("P Value at 5% level: ")
    k, p = get_jb_test(df)
    print(p)
    print("\n\nThus after applying Cornish Fisher modification,")
    
    
    print("The Portfolio's Value at risk at 5% level: ")
    print(str(round(get_var_modified(df)*100,2)) + "%")


def print_beta():
    #display portfolio Beta and Alpha against benchmarks
    print("\n***Alpha,Beta of portfolio against all benchmarks:*** \n")
    beta, alpha = get_pf_beta(df, df1)
    for i in range(len(df1.columns)):
        print("The protfolio beta for {} is: {}".format(df1.columns[i], beta[i]))
        print("Alpha against the same: {}\n".format(alpha[i]))
    

def print_treynor():
    #display Treynor ratio
    print("\n^taking 6% as average risk free rate^\n\n")
    print("Tryenor Ratio of Portfolio: \n")
    
    for j in range(len(df1.columns)):
        print("Ratio(for index {}) is : {}".format(df1.columns[j], round(get_treynor_ratio(df)[j],2))) 
    

def print_sharpe():
    #displlay sharpe ratio
    
    print("\nThe sharpe ratio of portfolio is: {}".format(round(get_sharpe_ratio(df),2)))


def print_pf_value():
    print("\nThe portfolio value over the years -")
    plot_pf_value(df,amt = 5000000)




def do_the_thing(a):
    if a == 1:
        print_assets()
    elif a ==2:
        print_asset_corr()
    elif a ==3:
        print_individual_returns()
    elif a ==4:
        print_pf_returns()
    elif a ==5:
        print_drawdowns()
    elif a ==6:
        print_benchmark()
    elif a ==7:
        print_var()
    elif a == 8:
        print_beta()
    elif a ==9:
        print_treynor()
    elif a ==10:
        print_sharpe()    
    elif a ==11:
        print_pf_value()
    elif a ==12:
        print_assets()
        print_asset_corr()
        print_individual_returns()
        print_pf_returns()
        print_drawdowns()
        print_benchmark()
        print_var()
        print_beta()
        print_treynor()
        print_sharpe()
        print_pf_value()
        
         
        

