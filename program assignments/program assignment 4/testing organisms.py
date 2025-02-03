Starting_number_of_organisms = int(input("Starting number of organisms: "))
Average_daily_increase = float(input("Average daily increase[%]: "))/100.0
Number_of_days_to_multiply = int(input("Number of days to multiply: "))
print("Day Approximate\tPopulation")
for Number_of_days_to_multiply in range(Starting_number_of_organisms, Number_of_days_to_multiply + 1):
    First_calculation = Starting_number_of_organisms * Average_daily_increase
    Starting_number_of_organisms = Starting_number_of_organisms + First_calculation
    print(Number_of_days_to_multiply - 1, '\t', Starting_number_of_organisms)
