# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:00:54 2020

@author: SID
"""
from showanalysis import *



print("                         **##** WELCOME **##**")

print("\n\n\n   AVAIALABLE INFORMATION TO DISPLAY   \n\n")

print("1. PRINT ALL ASSETS IN THE PORTFOLIO")
print("2. PRINT ASSET CORRELATION IN A MATRIX")
print("3. SHOW INDIVIDUAL ASSET RETURNS ON A GRAPH")
print("4. PRINT PORTFOLIO ANNUALIZED RETURNS, AAR AND VOLATILITY")
print("5. PRINT PORTFOLIO AND BENCHMARK DRAWDOWNS")
print("6. PRINT PORTFOLIO RETURNS VS BENCHMARK RETURNS")
print("7. PRINT PORTFOLIO'S VALUE AT RISK AT 5% LEVEL")
print("8. PRINT BETA OF PORTFOLIO W.R.T. BENCHMARKS")
print("9. PRINT TREYNOR RATIO OF PORTFOLIO W.R.T. BENCHMARKS")
print("10. PRINT SHARPE RATIO OF PORTFOLIO")
print("11. PRINT THE VALUE OF PORTFOLIO WITH A GRAPH")
print("12. PRINT ALL INFORMATION")
#print("13. EXIT THE PROGRAM")

input_list = [1,2,3,4,5,6,7,8,9,10,11,12]



try:

    a = int(input("ENTER A SINGLE CHOICE: "))
    if a in input_list:
        print("\n\n")
        do_the_thing(a)
    else:
        print('enter correct value')

except ValueError:
    print("enter correct value")












