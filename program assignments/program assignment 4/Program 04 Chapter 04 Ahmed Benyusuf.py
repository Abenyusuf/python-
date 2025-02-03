# Name:Ahmed Benyusuf
# Class and Section:	CS 120 01
# Assignment:Program Assignment 04
# Due Date:10/20/2023
# Date Turned in:10/18/2023
# Program Description: determine the

Starting_number_of_organisms = int(input("Starting number of organisms: "))
Average_daily_increase = float(input("Average daily increase[%]: ").split("%")[0])/100.0
Number_of_days_to_multiply = int(input("Number of days to multiply: "))
one = True
print("Day Approximate\tPopulation")
for Number_of_days_to_multiply in range(Starting_number_of_organisms, Number_of_days_to_multiply + 1):
    if one:
        print(1, '\t', Starting_number_of_organisms)
        one = False
    add = Starting_number_of_organisms * Average_daily_increase
    Starting_number_of_organisms = Starting_number_of_organisms + add
    print(Number_of_days_to_multiply - 1, '\t', Starting_number_of_organisms)
