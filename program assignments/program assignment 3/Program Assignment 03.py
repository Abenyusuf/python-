# Name:Ahmed Benyusuf
# Class and Section:	CS 120 01
# Assignment:Program Assignment 03
# Due Date:10/4/2023
# Date Turned in:10/2/2023
# Program Description: determine the price of shipping a package

ShippingCharges = float(input('Please enter the weight of the package in pounds '))
PoundsTwoOrLess = 1.50
PoundsTwoToSix = 3.00
PoundsSixToTen = 4.00
PoundsTenOrMore = 4.75
if ShippingCharges <= 2.0:
    TotalPrice = PoundsTwoOrLess
elif ShippingCharges <= 6.0:
    TotalPrice = PoundsTwoToSix
elif ShippingCharges <= 10.0:
    TotalPrice = PoundsSixToTen
elif ShippingCharges >= 10.0:
    TotalPrice = PoundsTenOrMore
print(f'Your total price is ${TotalPrice:,.2f}.')
