# Name:Ahmed Benyusuf
# Class and Section: CS 120 01
# Assignment:Program Assignment 05
# Due Date:11/3/2023
# Date Turned in:10/31/2023
# Program Description: determine the amount of money worth of tickets sold based on a user input.

def Main():
    SectionA, SectionB, SectionC = InputRead()
    CalculatingSales(SectionA, SectionB, SectionC)


def InputRead():
    SectionA = int(input("how many tickets were sold for the A section?"))
    SectionB = int(input("how many tickets were sold for the B section?"))
    SectionC = int(input("how many tickets were sold for the c section?"))
    return SectionA, SectionB, SectionC


def CalculatingSales(SectionA, SectionB, SectionC):
    SectionASales = SectionA * 20
    SectionBSales = SectionB * 15
    SectionCSales = SectionC * 10
    TotalSales = SectionASales + SectionBSales + SectionCSales
    print(f'The total amount of sales is ${TotalSales:.2f}')


Main()
