#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------
# Project: Compound Interest Monthly Payment 

# Skills used: for loops, while loops, Bisection Search
# ----------------


"""
Calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
"""

# Test Case 1-1:
month = 12
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# for loop for a year
for i in range(month):
    # Minimum monthly payment = (Previous balance) x (Minimum monthly payment rate)
    mpayment = balance * monthlyPaymentRate
    # Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    unpaidbalance = balance - mpayment
    # Monthly interest rate= (Annual interest rate) / 12.0
    # Interest = Monthly interest rate * Monthly unpaid balance
    Interest = (annualInterestRate / 12.0) * unpaidbalance
    #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    balance = unpaidbalance + Interest

# At the end of 12 months, print out the remaining balance (two decimal digits)
print ("Remaining balance:", round(balance,2))


"""  
Calculate the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
"""

# Test Case 2-1:
month = 12
balance = 3329
annualInterestRate = 0.2

# set the lowest Payment to $10
LowestPayment = 10

# create a temp for original balance so it won't change during the calculation 
originalbalance = balance

# set a while loop, break after paying off (Balance is less than 0/ becomes negative)
while balance > 0:
    # reset to original balance
    balance = originalbalance
    # monthly payment set to be multiple of $10 and is the same for all months
    LowestPayment += 10
    # for loop for a year
    for i in range(12):
        unbalance = balance - LowestPayment
        Interest = (annualInterestRate / 12.0)* unbalance
        balance = unbalance + Interest
    
# lowest monthly payment that will pay off all debt in under 1 year
print ("Lowest Payment:", LowestPayment)


"""
Use binary search to optimize above case (minimum fixed monthly payment)
"""
# Test Case 3-1:
balance = 320000
annualInterestRate = 0.2

# create a temp for original balance so it won't change during the calculation 
originalbalance = balance
# Calculate Monthly Interest Rate: divided annual Interest rate by 12 months
MonthlyInterestRate = annualInterestRate/12.0

# Set the lower bound and upper bound
# lower bound = One-twelfth of the original balance
low = balance/12
# upper bound = one-twelfth of the balance, after having its interest compounded monthly for an entire year
upper = balance * ((1+MonthlyInterestRate)**12)/12.0
# set the mid point for lower and upper bound
midpoint = round((low+upper)/2,2)

# set a while loop, break when absolute value of the balance lower or equal to 0.1
while abs(balance) >= 0.1:
    # reset to original balance and midpoint
    balance = originalbalance
    midpoint = round((low+upper)/2,2)
    # for loop for a year
    for i in range(12):
        unbalance = balance - midpoint
        Interest = (annualInterestRate / 12.0)* unbalance
        balance = unbalance + Interest

    if balance <0:
        upper = midpoint
        
    else:
        low = midpoint
# lowest monthly payment that will pay off all debt in under 1 year
print ("Lowest Payment 2:", midpoint)




