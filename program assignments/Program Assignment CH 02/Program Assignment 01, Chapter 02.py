#Name: Ahmed Benyusuf
#Class and Section: CS 120 01
#Assignment: Program Assignment 01, Chapter 02
#Due Date : Friday, September 15, 2023 by 11:59pm
#Program : calculate the total price after tax

AmtPrch = float(input('enter the amount of purchase:'))
StateTax = 0.05
CountyTax= 0.025
TaxTotal = (AmtPrch) * (StateTax + CountyTax)
TotalCost = (TaxTotal) + (AmtPrch)
print (f'your total cost is ${TotalCost:,.2f}.')
